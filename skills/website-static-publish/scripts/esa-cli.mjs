#!/usr/bin/env node
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { parseArgs } from 'node:util';
import { spawnSync } from 'node:child_process';

const credentialKeys = [
  'ESA_ACCESS_KEY_ID', 'ESA_ACCESS_KEY_SECRET', 'ESA_SECURITY_TOKEN',
  'ALIBABA_CLOUD_ACCESS_KEY_ID', 'ALIBABA_CLOUD_ACCESS_KEY_SECRET', 'ALIBABA_CLOUD_SECURITY_TOKEN'
];
const secretFields = ['access_key_id', 'access_key_secret', 'sts_token', 'oauth_access_token', 'oauth_refresh_token'];

export function stsEnvironment(profile, parent = process.env, now = Date.now()) {
  if (profile?.mode !== 'OAuth') throw new Error('The selected profile must use OAuth.');
  for (const field of ['access_key_id', 'access_key_secret', 'sts_token']) {
    if (typeof profile[field] !== 'string' || !profile[field].trim()) throw new Error(`Missing STS field: ${field}`);
  }
  const expires = typeof profile.sts_expiration === 'number' ? profile.sts_expiration * 1000 : Date.parse(profile.sts_expiration);
  if (!Number.isFinite(expires) || expires <= now + 120000) throw new Error('STS is expired or expires within two minutes. Renew the OAuth profile before retrying.');
  const env = { ...parent };
  for (const key of credentialKeys) delete env[key];
  delete env.CUSTOM_ENDPOINT;
  return {
    ...env,
    ESA_NO_UPDATE_CHECK: '1',
    ALIBABA_CLOUD_ACCESS_KEY_ID: profile.access_key_id,
    ALIBABA_CLOUD_ACCESS_KEY_SECRET: profile.access_key_secret,
    ALIBABA_CLOUD_SECURITY_TOKEN: profile.sts_token
  };
}

export function checkIdentity(identity, account, user) {
  if (identity.IdentityType !== 'RAMUser' || String(identity.AccountId) !== account || identity.Arn !== `acs:ram::${account}:user/${user}`) {
    throw new Error('CLI identity differs from the expected RAM user or owner account; ESA was not started.');
  }
}

export function redact(text, profile) {
  return secretFields.reduce((out, key) => {
    const value = profile?.[key];
    return typeof value === 'string' && value ? out.split(value).join('[redacted]') : out;
  }, text);
}

export function runWithProfile(options, args, dependencies = {}) {
  const run = dependencies.run || spawnSync;
  const read = dependencies.read || (file => {
    try { return JSON.parse(fs.readFileSync(file, 'utf8')); }
    catch { throw new Error('Cannot read the official CLI configuration as JSON.'); }
  });
  const env = { ...(dependencies.env || process.env), ALIBABA_CLOUD_CLI_TELEMETRY_DISABLE: '1' };
  for (const key of credentialKeys) delete env[key];
  if (!options.profile || !/^\d+$/.test(options.account || '') || !options.user || !options.cli) throw new Error('Provide --profile, --account, --user, and --cli.');
  if (!args.length || args.some(a => /^--(?:access-key-id|access-key-secret|ak|sk|sts-token)(?:=|$)/.test(a))) throw new Error('Pass an ESA command after --; credential arguments are not accepted.');
  const profileFile = path.join(dependencies.home || os.homedir(), '.aliyun/config.json');
  const readProfile = () => {
    const matches = read(profileFile).profiles?.filter(p => p.name === options.profile);
    if (matches?.length !== 1 || matches[0].mode !== 'OAuth') throw new Error('A unique OAuth profile is required. Run aliyun configure --mode OAuth for this profile.');
    return matches[0];
  };
  const before = readProfile();
  const identityResult = run(options.aliyun || 'aliyun', ['sts', 'GetCallerIdentity', '--profile', options.profile], {
    env, encoding: 'utf8', timeout: 45000, maxBuffer: 1024 * 1024, windowsHide: true
  });
  if (identityResult.status !== 0 || identityResult.error) {
    throw new Error(redact(`OAuth identity check failed. ${identityResult.stderr || identityResult.error?.message || ''}`, before));
  }
  let identity;
  try { identity = JSON.parse(identityResult.stdout); } catch { throw new Error('CLI returned an invalid identity response.'); }
  checkIdentity(identity, options.account, options.user);
  // The official CLI refreshes its OAuth profile when needed. Read it again afterwards.
  const profile = readProfile();
  const result = run(process.execPath, [path.resolve(options.cli), ...args], {
    cwd: path.resolve(options.cwd || process.cwd()), env: stsEnvironment(profile, env), encoding: 'utf8',
    timeout: 600000, maxBuffer: 8 * 1024 * 1024, windowsHide: true
  });
  const output = redact(redact((result.stdout || '') + (result.stderr || ''), profile), before);
  if (result.error || result.signal) {
    return { status: 1, output: `${output}\nESA process stopped (${result.error?.code || result.signal}). Query deployment state before retrying.\n` };
  }
  return { status: Number.isInteger(result.status) ? result.status : 1, output };
}

function main() {
  const argv = process.argv.slice(2);
  const split = argv.indexOf('--');
  const { values } = parseArgs({ args: split < 0 ? argv : argv.slice(0, split), options: {
    profile: { type: 'string' }, account: { type: 'string' }, user: { type: 'string' },
    cli: { type: 'string' }, aliyun: { type: 'string' }, cwd: { type: 'string' }, help: { type: 'boolean' }
  }});
  if (values.help) {
    console.log('node esa-cli.mjs --profile PROFILE --account OWNER_ID --user RAM_USER --cli /path/to/esa-cli/bin/enter.cjs [--aliyun /path/to/aliyun] [--cwd /path/to/project] -- ESA_COMMAND [ARGS]\nUses the named local OAuth profile; secrets are passed only in the child environment.');
    return;
  }
  const result = runWithProfile(values, split < 0 ? [] : argv.slice(split + 1));
  process.stdout.write(result.output);
  process.exitCode = result.status;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 1; }
}
