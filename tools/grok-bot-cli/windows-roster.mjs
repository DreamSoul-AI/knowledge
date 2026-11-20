import { spawnSync } from 'node:child_process';
import { copyFileSync, mkdtempSync, readFileSync, rmdirSync, unlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

// The read-only subset of the existing DreamSoul tutorial's #168 workaround.
const original = [
  '            const data = await gatewayCall(session, "listAgents", {}, {',
  '                signal',
  '            });',
  '            return unwrapList(data).map(asRecord).filter((r)=>r && r.id);',
].join('\n');

const repaired = `            const state = reconnectStates.get(session);
            if (!state?.accountKey) throw new GatewayError("Grok Bot desktop account unavailable");
            const credentials = (0, _app_session_js__rspack_import_2.gF)({
                ...state.appSessionOptions, expectedAccountKey: state.accountKey
            });
            if (!credentials?.accessToken) throw new GatewayError("Grok Bot desktop login unavailable");
            const base = (0, _url_policy_js__rspack_import_4.Re)(backendBase(), { kind: "backend" });
            const headers = (0, _headers_js__rspack_import_1._6)(credentials.accessToken);
            headers["x-client-version"] = headers["x-cursor-client-version"];
            if (credentials.teamId !== undefined) headers["x-cursor-team-id"] = credentials.teamId;
            const response = await fetch(base + "/aiserver.v1.GrokBotService/ListGrokBotAgents", {
                method: "POST", redirect: "error", signal: gatewayDeadline(signal),
                headers, body: JSON.stringify({})
            });
            if (!response.ok) throw new GatewayError("ListGrokBotAgents failed: HTTP " + response.status);
            const data = await readJson(response);
            if (!Array.isArray(data.agents)) throw new Error("Unexpected roster schema");
            return data.agents.map(asRecord).filter((agent) => agent?.id);`;

export function checkWindowsRoster(bin, version) {
  if (process.platform !== 'win32' || version !== '0.12.5') {
    throw new Error('The roster workaround requires Windows and grok-bot-cli 0.12.5.');
  }
  const source = readFileSync(join(bin, 'gbot-flight.mjs'), 'utf8');
  const newline = source.includes('\r\n') ? '\r\n' : '\n';
  const block = original.replaceAll('\n', newline);
  if (source.split(block).length !== 2) throw new Error('Unexpected upstream worker layout.');

  const temp = mkdtempSync(join(tmpdir(), 'knowledge-gbot-'));
  const cli = join(temp, 'gbot.mjs');
  const worker = join(temp, 'gbot-flight.mjs');
  try {
    copyFileSync(join(bin, 'gbot.mjs'), cli);
    writeFileSync(worker, source.replace(block, repaired.replaceAll('\n', newline)));
    const result = spawnSync(process.execPath, [cli, 'bots', 'list', '--json'], { stdio: 'inherit' });
    if (result.error) throw result.error;
    return result.status ?? 1;
  } finally {
    for (const file of [cli, worker]) {
      try { unlinkSync(file); } catch (error) { if (error.code !== 'ENOENT') throw error; }
    }
    rmdirSync(temp);
  }
}
