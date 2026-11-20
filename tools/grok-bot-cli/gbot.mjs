import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { checkWindowsRoster } from './windows-roster.mjs';

const toolDir = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const packageDir = args[0] === '--package-dir'
  ? args.splice(0, 2)[1]
  : join(toolDir, 'node_modules', 'grok-bot-cli');

try {
  if (!packageDir) throw new Error('--package-dir requires an installed package directory.');
  const root = resolve(packageDir);
  const metadata = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
  if (metadata.name !== 'grok-bot-cli') throw new Error('Expected the upstream grok-bot-cli package.');
  const bin = join(root, 'dist', 'bin');
  if (args[0] === '--windows-roster-fix') {
    if (args.length !== 1) throw new Error('--windows-roster-fix only supports the read-only Bot list.');
    process.exitCode = checkWindowsRoster(bin, metadata.version);
  } else {
    const result = spawnSync(process.execPath, [join(bin, 'gbot.mjs'), ...(args.length ? args : ['--help'])], { stdio: 'inherit' });
    if (result.error) throw result.error;
    if (result.signal) throw new Error(`Upstream exited on signal ${result.signal}.`);
    process.exitCode = result.status ?? 1;
  }
} catch (error) {
  console.error(`Grok Bot CLI: ${error.message}\nSee the tool README for installation.`);
  process.exitCode = 1;
}
