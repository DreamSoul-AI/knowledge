# grok-bot-cli

[简体中文](README_zh.md)

This launcher runs the community [ScriptedAlchemy/grok-bot-cli](https://github.com/ScriptedAlchemy/grok-bot-cli) package, licensed upstream under MIT. Install the original package from npm. Desktop sessions remain managed by the local Grok Bot application.

From this directory, with Node.js 22.19.0 or later, install the version checked for this launcher and run its help:

```text
npm install --no-save --package-lock=false --ignore-scripts grok-bot-cli@0.12.5
node gbot.mjs --help
```

With an existing install, run `node gbot.mjs --package-dir <installed-package-directory> --help`. The directory contains the upstream `package.json`. Remaining arguments go to the installed CLI. Running the launcher without arguments shows help.

For live use, sign into the desktop app as the same operating system user and verify read access with `node gbot.mjs bots list --json`. Verify the target and authorization before writing or sending. For a routing 404, compare your version and symptoms with [upstream issue #168](https://github.com/ScriptedAlchemy/grok-bot-cli/issues/168). Verify installation, desktop authentication, and live messaging separately. The Windows MCP workaround is covered by the [connection guide](https://dreamsoul.feishu.cn/docx/Sqsdd69p7osKAqxx5UwcJeOEn1e).

For the roster 404 on Windows with 0.12.5, run `node gbot.mjs --windows-roster-fix`. With a global installation, place `--package-dir <installed-package-directory>` before that flag. The flag uses the tutorial's temporary isolated fix for the read-only list. It retains upstream account binding, desktop authentication, host validation, and timeouts. It leaves the installed package intact and does not send messages or configure MCP.

For Agent use, see the [Grok Bot CLI skill and bundled guide](../../skills/grok-bot-cli/SKILL.md). Keep installed dependencies, sessions, credentials, and test targets on the local machine.
