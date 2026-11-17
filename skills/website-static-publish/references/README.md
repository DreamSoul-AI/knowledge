# Website Static Publish

English | [简体中文](README_zh.md)

Publish an HTML file, static directory or ZIP to Alibaba Cloud ESA Pages or Cloudflare Pages, including first deployment and updates at the original URL. New configurations default to the China/ESA route. Both providers use CLI by default.

First use: install the skill → fill configuration → authorize the CLI → check and publish. Reuse configuration and authentication for later updates.

## Example requests

After setup, send a request to your agent. Replace paths, project names and URLs with your actual targets:

```text
Use $website-static-publish to check ./dist and my deployment configuration. List missing items; do not upload.
```

```text
Use $website-static-publish to update the existing ESA project my-demo from ./dist and verify the original URL.
```

```text
Use $website-static-publish to update the existing Cloudflare project my-site from ./dist and verify the original URL.
```

```text
Use $website-static-publish to update the configured ESA and Cloudflare projects from the same ./dist. Verify each original URL.
```

For a new project, explicitly request creation and specify its name. ESA standalone demos use separate projects and subdomains; small experiments can share a collection with stable paths. Collection updates start from the complete current site and preserve other experiments. See [demo organization](../SKILL.md#esa-demo-组织方式).

## Installation and requirements

Version 1.2.0 is on knowledge's `feature/migrate-website-static-publish` migration branch, pending integration into the release branch. Check out that branch and install from the local directory. Your agent needs file access, command execution and a browser for authorization. Installation request:

```text
Install the supplied website-static-publish into this project's .agents/skills/.
Copy the complete skill directory, exclude real CONFIG.md and private files, and include the knowledge root LICENSE.
Back up an existing installation and preserve its configuration. Only install in this task.
```

Preserve the license included in a distribution package. After installation, check the loaded path and version; reopen the chat if the skill is not recognized. Prepare tools for the selected provider:

| Tool | Version and purpose |
| --- | --- |
| Node.js / npm | Tested with Node.js 24.18.0; Wrangler 4.163.0 requires ≥22.12.0, ESA CLI requires ≥18 |
| Alibaba Cloud CLI | ESA OAuth uses 3.5.3; install using the [official guide](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli), add it to PATH and check `aliyun version` |
| ESA CLI | 1.0.14 for ESA uploads |
| Wrangler | 4.163.0 for Cloudflare Pages uploads |

Reuse existing pinned tools. If a tool is missing, run the required line from the deployment working directory:

```powershell
npm install --prefix .artifacts/esa-cli --save-exact --ignore-scripts --no-audit --no-fund esa-cli@1.0.14
npm install --prefix .artifacts/wrangler --save-exact --ignore-scripts --no-audit --no-fund wrangler@4.163.0
```

Add `.artifacts/` to the website project's ignore rules and keep tools outside public `dist/`. The PowerShell examples below use these local installation paths. Replace placeholders and complete the checks before running deployment commands.

## Initial configuration

Copy [assets/CONFIG.example.md](../assets/CONFIG.example.md) into the loaded skill's root as `CONFIG.md`, beside `SKILL.md`. Preserve an existing file. Edit only the value column; keep field names, the `字段` / `值` headers and every field row.

| Field | Value |
| --- | --- |
| `schemaVersion` | Keep `2`, the configuration format version; the skill release is 1.2.0 |
| `default.target` | Default `china`; alternatives are `overseas`, `both` and `ask`, meaning overseas, both providers, or ask when unspecified |
| `china.provider` | Keep `esa` for new configurations. china selects a provider route; check the actual acceleration region in the ESA site |
| `esa.project.deployMethod` | Default `cli`; ordinary upgrades preserve an existing console/github value |

The provider, project and environment specified in a request override defaults. Cloudflare uses Wrangler by default; the configuration table needs no additional deployment-method field. Fill only the selected provider's required values, using these sources after authentication:

| Provider | Required details and source |
| --- | --- |
| ESA identity | Set `esa.account.ramLogin` to the official RAM login and `esa.account.ownerId` to the resource owner's account ID. Verify RAM details against AccountId and Arn from `aliyun sts GetCallerIdentity` |
| ESA project | Set `esa.project.name` to the existing project and `environment` to `production` or `staging`, checked against the project list. CLI use can leave `productionBranch` empty |
| ESA long-term URL | Fill `esa.site.*` with site ID, name, actual region and `ns`/`cname` access type. Set `esa.domain.name` to the domain without protocol or path. Short-lived tests can leave these empty |
| Cloudflare identity | Set `cloudflare.account.id` to the 32-character Account ID and `email` to the actual operator email from `whoami --json`. Distinguish Account ID from Zone ID |
| Cloudflare project | Set `cloudflare.project.name`, `productionBranch` and `environment` to the existing Pages project, actual production branch and `production`/`preview`. Specify a separate branch for Preview |

Optional labels and unused providers' account/project values can remain empty. See [configuration.md](configuration.md) for all fields and legacy migration rules.

`CONFIG.md` stores identifiers and business defaults. Official tools manage authentication and credentials: Alibaba Cloud OAuth uses the local `~/.aliyun/config.json`; Wrangler uses its own user configuration. Pass CLI paths and OAuth profile names as command arguments. Keep passwords, keys, cookies and tokens out of the table and public artifacts.

## ESA first authorization and use

**1. Authorize.** A RAM administrator installs `official-cli` and allows the publishing user to access it. That user also needs permissions for the target ESA resources. Run:

```powershell
aliyun configure --mode OAuth --profile my-esa-profile
aliyun sts GetCallerIdentity --profile my-esa-profile
```

Select the China or international login site for the account, then complete official authorization and MFA. Verify RAMUser, the resource owner's AccountId and the username in Arn. Reuse this profile afterwards. See [OAuth authentication](esa-cli.md#oauth-认证) for manual browser mode.

**2. Prepare artifacts.** Build the complete static site into `dist/` and put `esa.jsonc` beside it:

```json
{"name":"my-demo","assets":{"directory":"./dist"}}
```

Before an update, save the complete live artifacts and preserve existing routing and domains. New projects need an available ESA compute service; long-term URLs need site, DNS and HTTPS configuration. See [ESA](esa.md).

**3. Verify the project.** Fill fixed arguments once and reuse them for queries and deployment. `--user` takes the RAM username portion; `--cli` takes an absolute path:

```powershell
$esaRunner = '<skill-directory>/scripts/esa-cli.mjs'
$esaArgs = @(
    '--profile', 'my-esa-profile',
    '--account', '<owner-account-ID>',
    '--user', '<RAM-username>',
    '--cli', (Resolve-Path '.artifacts/esa-cli/node_modules/esa-cli/bin/enter.cjs').Path,
    '--cwd', '<absolute-deployment-working-directory>'
)
node $esaRunner @esaArgs -- project list --keyword my-demo
node $esaRunner @esaArgs -- deployments list
node $esaRunner @esaArgs -- domain list
```

The last two queries read `esa.jsonc` in the working directory. Deploy after the queries succeed and the original project, environment and domain match. Resolve a missing update target before proceeding; do not create a replacement.

**4. Deploy and read back.** These commands update production:

```powershell
node $esaRunner @esaArgs -- deploy --name my-demo --assets ./dist --environment production --description release-001 --no-preview
node $esaRunner @esaArgs -- deployments list
```

The included runner checks identity and temporary STS credentials before invoking the official CLI. `--no-preview` omits the temporary preview link and suits an existing fixed domain. For a short-lived test URL, follow the [ESA CLI workflow](esa-cli.md).

## Cloudflare first authorization and use

**1. Log in.** Resolve Wrangler's absolute path from the tools installation directory, then inspect CLI identity:

```powershell
$wranglerPath = (Resolve-Path '.artifacts/wrangler/node_modules/wrangler/bin/wrangler.js').Path
node $wranglerPath --version
node $wranglerPath whoami --json
```

If unauthenticated, authorize once and run whoami again to verify the email and account:

```powershell
node $wranglerPath login --browser=false --scopes account:read user:read pages:write
node $wranglerPath whoami --json
```

Complete authorization at the command's official URL and wait for the CLI to finish. Version 4.163.0 adds `offline_access` for renewal automatically; pass only the three scopes above.

**2. Select the account and project.** Switch to the static deployment working directory. Check Wrangler configuration, `functions/` and `_worker.js` to exclude unrelated project settings and backend entry points. Select the account and query projects:

```powershell
$previousAccountId = $env:CLOUDFLARE_ACCOUNT_ID
$env:CLOUDFLARE_ACCOUNT_ID = '<verified Account ID>'
node $wranglerPath pages project list --json
```

Verify the existing project and its actual production branch. Replace the template's `main` when the cloud value differs. Resolve a missing update target first. For explicitly requested creation with an available name, use [project create](cloudflare-cli.md#新建与更新).

**3. Deploy and read back.** Upload the complete directory, using the project's actual production branch for production:

```powershell
node $wranglerPath pages deploy '<absolute-artifact-directory>' --project-name my-site --branch '<actual-production-branch>'
node $wranglerPath pages deployment list --project-name my-site
```

After completion or interruption, restore the original account environment variable in the same terminal. Automated callers should guarantee restoration with `try/finally`:

```powershell
$env:CLOUDFLARE_ACCOUNT_ID = $previousAccountId
```

Wrangler accepts a directory; extract ZIPs first. The per-file limit is 25 MiB and the Free-plan site limit is 20,000 files. See [Cloudflare limits](cloudflare.md#发布范围与平台限制) for paid quotas, project counts and Direct Upload restrictions.

## Preflight and visitor acceptance

1. Build with the website's existing commands and check the entry page, resources, routing and quotas. Upload public static files only, excluding private configuration, credentials and logs. Confirm backend, SSR or Functions requirements separately.
2. Preserve the complete current artifacts before updating. Both providers share one directory, with authentication, deployment and acceptance handled separately. If an upload fails or its state is unknown, query remote records before deciding whether to retry.
3. In a visitor session without provider login, check the new version at the original production URL, HTTPS, CSS/JS/images/JSON, interactions, Chinese paths, subpage refresh and expected 404 responses. Check every new and preserved experiment in a collection.
4. Deliver each provider's actual URL, version, project/environment, deployment record and access results, including the tested network. Use a verified custom domain for long-term ESA access and the original production URL for Cloudflare. For short-lived ESA test URLs, include full parameters and generation/expiry times according to the [delivery rules](esa.md#交付).

For later updates: rebuild the complete directory → publish to the same project, environment and domain → verify the original URL. Content hashes or versioned resource references help avoid mixing old and new assets. See [ESA CLI](esa-cli.md), [Wrangler](cloudflare-cli.md) and the full rules in [SKILL.md](../SKILL.md).

## Directory layout and responsibilities

| Source path | Purpose |
| --- | --- |
| `SKILL.md` | Invocation and shared execution rules |
| `agents/openai.yaml` | UI metadata |
| `assets/CONFIG.example.md` | Empty configuration template |
| `references/` | Bilingual guides, field rules and provider workflows; EdgeOne references support legacy configurations |
| `scripts/esa-cli.mjs` | ESA OAuth runner |
| `scripts/esa-cli.test.mjs` | Runner tests |
| `.gitignore` | Ignores private CONFIG.md beside it; retained on installation |

Create the real `CONFIG.md` in the installed skill's root. Keep website artifacts, CLIs, logs and validation output in the deployment working directory. Maintainers can run `node --test "<skill-directory>/scripts/esa-cli.test.mjs"`.

## Upgrades and validation scope

Back up the installation to a private location outside skill discovery directories. Update instructions, metadata, templates and scripts while preserving real CONFIG.md. Follow [migration rules](configuration.md#迁移与保留) for schema changes. The former root `CONFIG.example.md` and `tests/scripts/esa-cli.test.mjs` now live in assets and scripts; check and preserve local edits before removing old copies.

The new template defaults to china. Existing ask, both, overseas and ESA console/github values remain intact. To make ESA the default, set `default.target=china` and `china.provider=esa`; the configuration format remains 2.

Include the knowledge root MIT LICENSE in standalone installations and packages. Check the manifest and exclude CONFIG.md, USER.md, credentials, logs, screenshots, private backups and provider CLI packages. `.gitignore` protects new files; check packaging and already tracked files separately.

On 2026-11-17, Skill 1.2.0, ESA CLI 1.0.14 and Wrangler 4.163.0 deployed the same site to two existing projects and verified updates at their original URLs and visitor access. Versioned references resolved the ESA resource-version issue; some connections passed after targeted retries. CLI creation, collection deployment, restoration, unattended CI, checks across days and target-region networks remain unverified. See [validation status](../SKILL.md#验证状态).
