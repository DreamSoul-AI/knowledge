# Lark authorization reuse

[中文](README_zh.md) · [Skill](../SKILL.md) · [English](README.md)

Use `$lark-auth-reuse` to inspect an existing authorization, the actual execution identity and a failed call. It requires the existing `lark-cli` and `lark-shared` setup; the complete skill package provides diagnosis and continuation without a separate credential store.

**Multiple chats on one machine can reuse an existing authorization** when their CLI processes use the same actual operating-system user, application, profile and accessible credential environment. Changing chats does not itself require another sign-in. Workspace conventions can standardize checks and invocation, but do not change operating-system credential permissions.

Use this guide with the existing `lark-shared` skill and `lark-cli`. It adds no login skill, credential service or installation step. Consult the relevant Lark skill for business commands and retain the current task's read/write authorization.

## Reuse a working authorization

Check the existing login in the execution environment authorized for this task:

```powershell
lark-cli auth status --json --verify
lark-cli whoami --as user
```

Inspect server verification, the actual user and token status. An identity of `user` with a `missing` token is not a usable user login. Explicitly pass `--as user` on subsequent commands representing that user instead of relying on automatic identity selection.

When the identity and token are usable, continue with the existing login. The CLI handles valid-token reuse and supported refresh, without a separate token copy for each chat. A successful read establishes access to that resource, not to every resource or any additional write operation.

## Diagnose missing before signing in again

Compare the actual process identity and selected non-sensitive configuration fields:

```powershell
[System.Security.Principal.WindowsIdentity]::GetCurrent().Name
lark-cli --version
$larkReuseConfig = lark-cli config show | ConvertFrom-Json
$larkReuseConfig | Select-Object profile,profileSource,workspace,brand,appId
```

These fields are for local comparison. Some versions or configurations may not provide every field. Display only needed selected fields, never raw configuration, `appSecret`, tokens or other secrets. Remove real account, application and profile identifiers from shared diagnostic reports.

**Environment variables do not establish the actual process identity**. Matching `USERNAME` or `USERPROFILE` strings can coexist with different Windows users. A readable configuration file does not establish access to an existing credential store.

If the actual identity or credential environment differs, retain both sets of non-sensitive diagnostic results. When an operation needs existing user credentials, use the execution tool's normal approval process to run it in an authorized environment that can access those credentials. State the specific operation and its read/write effects. Verify identity again after approval and resume only the necessary failed operation, avoiding repeated successful writes.

Do not copy registry entries or tokens, disable isolation, silently switch to bot identity, or elevate every command unconditionally. Do not log out or request repeated scans merely to work around an execution-identity mismatch.

## Separate authorization from resource permissions

| Observation | Check |
| --- | --- |
| Different application or profile | Adopted project configuration and identity |
| Still missing or refresh fails in the same environment | Existing login and specific error |
| Valid user, missing scope | Application scopes and user consent |
| Valid user, resource access denied | Permissions on the target resource |

**Application scopes** determine which API capabilities the application has enabled. **User consent scopes** determine what the user has granted that application. **Resource permissions** determine what this user can access on a particular document, table or other object. Check them separately. Another sign-in does not repair a resource ACL.

Only request authorization when additional user consent is genuinely needed or an existing login cannot be recovered. Follow the current `lark-shared` incremental domain/scope flow, show the newly generated authorization link and QR code, and continue after the user finishes. Do not reuse expired links or request every permission by default. Route application configuration and resource access issues to the appropriate owner without silently changing accounts or expanding access.

## Mechanism and verified scope

The official `lark-cli` 1.0.93 implementation locates user credentials by application and user identity, not by chat ID. Its Windows backend uses the current user's HKCU and DPAPI, so the actual Windows identity affects credential access. See [credential lookup](https://github.com/larksuite/cli/blob/v1.0.93/internal/auth/token_store.go) and [Windows credential storage](https://github.com/larksuite/cli/blob/v1.0.93/internal/keychain/keychain_windows.go). Check the corresponding implementation for other versions.

Two independent normal processes on one machine used the same application, profile and user, passed server-side identity verification, and read the same existing resource. A restricted process had a different actual Windows identity and could not access the corresponding credential environment, reporting `missing`. No new login, logout, credential copying, permission change or business write was performed.

The official [user-token call and refresh implementation](https://github.com/larksuite/cli/blob/v1.0.93/internal/auth/uat_client.go) reuses valid tokens and refreshes when necessary, with account locking. Tokens were valid at the start of both actual runs. Refresh was checked in source only. Real expiration, concurrent refresh and recovery from long-expired authorization were not tested.

These results establish reuse by independent processes on one machine. They do not establish automatic selection of the correct environment by every desktop chat. Cross-device reuse, other operating-system users, and other applications or profiles were not tested. Check the actual current identity and follow the specific error rather than requesting unnecessary repeat authorization.
