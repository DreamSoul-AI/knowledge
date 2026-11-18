import test from 'node:test';
import assert from 'node:assert/strict';
import { checkIdentity, stsEnvironment, runWithProfile } from './esa-cli.mjs';

const profile = () => ({ name: 'test', mode: 'OAuth', access_key_id: 'test-id', access_key_secret: 'test-secret', sts_token: 'test-token', oauth_refresh_token: 'test-refresh', sts_expiration: Math.floor(Date.now() / 1000) + 3600 });
const identity = { IdentityType: 'RAMUser', AccountId: '123', Arn: 'acs:ram::123:user/publisher' };
const options = { profile: 'test', account: '123', user: 'publisher', cli: '/test/esa/enter.cjs' };

test('content: reject a different owner, user, or main-account identity', () => {
  for (const item of [{ ...identity, AccountId: '456' }, { ...identity, Arn: 'acs:ram::123:user/admin' }, { ...identity, IdentityType: 'Account' }]) {
    assert.throws(() => checkIdentity(item, '123', 'publisher'), /differs/);
  }
});

test('content: incomplete and expired credentials cannot reach ESA', () => {
  for (const change of [{ sts_token: '' }, { sts_expiration: 0 }, { sts_expiration: 'invalid' }, { mode: 'AK' }]) {
    assert.throws(() => stsEnvironment({ ...profile(), ...change }));
  }
});

test('content: selected profile replaces inherited credential groups without mutating the parent', () => {
  const parent = { ESA_ACCESS_KEY_ID: 'other-id', ESA_ACCESS_KEY_SECRET: 'other-secret', ALIBABA_CLOUD_SECURITY_TOKEN: 'other-token', CUSTOM_ENDPOINT: 'unexpected', KEEP: 'yes' };
  const env = stsEnvironment(profile(), parent);
  assert.equal(env.ESA_ACCESS_KEY_ID, undefined);
  assert.equal(env.ESA_ACCESS_KEY_SECRET, undefined);
  assert.equal(env.CUSTOM_ENDPOINT, undefined);
  assert.equal(env.ALIBABA_CLOUD_SECURITY_TOKEN, 'test-token');
  assert.equal(env.KEEP, 'yes');
  assert.equal(parent.ESA_ACCESS_KEY_ID, 'other-id');
});

test('integration content: refreshed profile is used; secrets never enter arguments or output', () => {
  let reads = 0;
  const calls = [];
  const refreshed = { ...profile(), access_key_secret: 'fresh-secret', sts_token: 'fresh-token' };
  const result = runWithProfile(options, ['deploy', '--no-preview'], {
    env: {}, read: () => ({ profiles: [++reads === 1 ? profile() : refreshed] }),
    run: (file, args, settings) => {
      calls.push({ file, args, settings });
      return calls.length === 1 ? { status: 0, stdout: JSON.stringify(identity) } : { status: 0, stdout: 'fresh-secret fresh-token test-secret test-refresh' };
    }
  });
  assert.equal(calls[1].settings.env.ALIBABA_CLOUD_ACCESS_KEY_SECRET, 'fresh-secret');
  assert.equal(JSON.stringify(calls.map(c => c.args)).includes('fresh-secret'), false);
  assert.equal(result.output, '[redacted] [redacted] [redacted] [redacted]');
  assert.equal(result.status, 0);
});

test('integration content: identity failure stops before the ESA child starts', () => {
  let calls = 0;
  assert.throws(() => runWithProfile(options, ['deploy'], {
    env: {}, read: () => ({ profiles: [profile()] }),
    run: () => { calls++; return { status: 0, stdout: JSON.stringify({ ...identity, AccountId: '456' }) }; }
  }), /differs/);
  assert.equal(calls, 1);
});

test('integration content: ESA failures preserve status; timeout directs state inspection without retry', () => {
  for (const failure of [{ status: 7, stderr: 'denied' }, { status: null, error: { code: 'ETIMEDOUT' }, stdout: 'upload began' }]) {
    let calls = 0;
    const result = runWithProfile(options, ['deploy'], {
      env: {}, read: () => ({ profiles: [profile()] }),
      run: () => ++calls === 1 ? { status: 0, stdout: JSON.stringify(identity) } : failure
    });
    assert.equal(calls, 2);
    assert.equal(result.status, failure.status || 1);
    if (!failure.status) assert.match(result.output, /Query deployment state/);
  }
});
