"""Receive scoped Git/local learning sources as immutable bytes, with incremental identity.
No semantic classification, Git mutation, source deletion or remote network operation.
"""
import argparse
import contextlib
import fnmatch
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from datetime import datetime, timezone
from collections import Counter
from urllib.parse import unquote, urlsplit

EXCLUDED = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache",
            ".mypy_cache", ".ruff_cache", ".cache", "tmp", "temp", "build", "dist",
            "data", "models", "artifacts", "outputs", ".local", ".test-results"}
NAV = ["AGENTS.md", "REPO.md", "README.md", "README_zh.md", "docs/README.md"]
TEXT = {".md", ".markdown", ".txt", ".rst"}
LINK = re.compile(r"\]\((?:<([^>]+)>|([^\s)]+)(?:\s+[^)]*)?)\)")
SOURCE_DIR = re.compile(r"^(?:经验(?:\s+Learnings?)?|Learnings?|Experiences?)$", re.I)
SOURCE_FILE = re.compile(r"^(?:经验|Learnings?|Experiences?)(?:[ ._-].*)?\.(?:md|markdown|txt|rst)$", re.I)


def digest(b):
    return hashlib.sha256(b).hexdigest()


def stable(*parts):
    return digest(json.dumps(parts, ensure_ascii=False).encode())[:24]


def atomic(path, value):
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def safe_relative(path):
    p = PurePosixPath(path.replace("\\", "/"))
    if p.is_absolute() or ".." in p.parts or not p.parts or ":" in p.parts[0]:
        raise ValueError("Unsafe relative path: " + path)
    return p.as_posix()


def selected(path, declared):
    parts = PurePosixPath(path).parts
    return (any(path == p or path.startswith(p.rstrip("/") + "/") for p in declared)
            or any(SOURCE_DIR.fullmatch(p) for p in parts[:-1])
            or bool(SOURCE_FILE.fullmatch(parts[-1])))


def excluded(path, declared, patterns):
    # Explicit source paths may live inside ordinary caches; explicit user exclusions still win.
    if any(fnmatch.fnmatchcase(path, p) or (not any(c in p for c in '*?[')
                                         and path.startswith(p.rstrip('/') + '/')) for p in patterns):
        return True
    explicit = any(path == p or path.startswith(p.rstrip("/") + "/")
                   or p.startswith(path.rstrip("/") + "/") for p in declared)
    return not explicit and any(p.casefold() in EXCLUDED for p in PurePosixPath(path).parts)


def git(repo, *args):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    r = subprocess.run(["git", "-c", "safe.directory=" + str(repo), "-C", str(repo), *args],
                       capture_output=True, env=env)
    if r.returncode:
        raise RuntimeError(r.stderr.decode("utf-8", "replace").strip() or "Git command failed")
    return r.stdout


def git_text(repo, *args):
    return git(repo, *args).decode("utf-8").strip()


def worktrees(repo):
    rows, row = [], None
    for field in git(repo, "worktree", "list", "--porcelain", "-z").decode("utf-8").split("\0"):
        if field.startswith("worktree "):
            row = {"path": field[9:]}
            rows.append(row)
        elif row is not None and field.startswith("HEAD "):
            row["head"] = field[5:]
        elif row is not None and field.startswith("branch "):
            row["branch"] = field[7:]
        elif row is not None and field in ("bare", "detached", "prunable"):
            row[field] = True
    return rows


def text_content(b):
    return b.decode("utf-8-sig")


def redirected(path):
    return path.is_symlink() or bool(getattr(path.lstat(), "st_file_attributes", 0) & 1024)


def navigation(files, read, paths, scope):
    findings = []
    folded = {}
    for p in files:
        folded.setdefault(p.casefold(), []).append(p)
    for paths_same_case in folded.values():
        if len(paths_same_case) > 1:
            findings.append({"kind": "case-collision", "scope": scope, "paths": paths_same_case})
    for path in sorted(paths):
        if PurePosixPath(path).suffix.lower() not in TEXT:
            continue
        try:
            body = text_content(read(path))
        except (OSError, UnicodeError, RuntimeError) as e:
            findings.append({"kind": "navigation-unreadable", "scope": scope, "path": path, "error": str(e)})
            continue
        if re.search(r"^<<<<<<<(?: |$)", body, re.M) and re.search(r"^>>>>>>>(?: |$)", body, re.M):
            findings.append({"kind": "conflict-markers-candidate", "scope": scope, "path": path})
        for m in LINK.finditer(body):
            href = m[1] or m[2]
            if urlsplit(href).scheme or href.startswith(("#", "//", "/")):
                continue
            href = unquote(href.split("#", 1)[0].split("?", 1)[0])
            if not href:
                continue
            stack = list(PurePosixPath(path).parent.parts)
            for part in href.replace("\\", "/").split("/"):
                if part == "..":
                    if stack:
                        stack.pop()
                    else:
                        stack.append("..")
                elif part and part != ".":
                    stack.append(part)
            target = "/".join(stack)
            if target not in files and not any(p.startswith(target.rstrip("/") + "/") for p in files):
                findings.append({"kind": "missing-relative-target", "scope": scope, "path": path,
                                 "href": m[1] or m[2], "target": target})
    return findings


@contextlib.contextmanager
def writer(out):
    out.mkdir(parents=True, exist_ok=True)
    lock = out / ".intake.lock"
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.close(fd)
        indexfile = out / "index.json"
        if indexfile.exists():
            state = json.loads(indexfile.read_text(encoding="utf-8"))
            if state.get("version") != 1 or not isinstance(state.get("sources"), dict):
                raise ValueError("Unsupported or damaged intake index; preserve it before recovery")
        else:
            state = {"version": 1, "sources": {}}
        yield state
    finally:
        lock.unlink()


def receive(out, state, incoming, scopes, complete, errors, exclusions, findings, coverage):
    objects = out / "objects"
    objects.mkdir(exist_ok=True)
    old = state["sources"]
    previous = {sid: dict(row) for sid, row in old.items()}
    current_ids = {stable(r["repository"], r["scope"], r["path"]) for r, _ in incoming}
    arrivals = Counter((r["repository"], r["scope"], digest(b)) for r, b in incoming
                       if stable(r["repository"], r["scope"], r["path"]) not in previous)
    changes = []
    for row, content in incoming:
        h = digest(content)
        objectpath = objects / h
        if objectpath.exists():
            if objectpath.read_bytes() != content:
                raise ValueError("Corrupt immutable snapshot: " + h)
        else:
            objectpath.write_bytes(content)
        sid = stable(row["repository"], row["scope"], row["path"])
        before = previous.get(sid)
        change = "new"
        entry = sid
        prior_path = None
        history = []
        if before:
            entry = before["entry_id"]
            history = list(before["history"])
            change = "unchanged" if before["sha256"] == h else "changed"
        else:
            moves = [r for oid, r in previous.items()
                     if r["scope"] == row["scope"] and r["repository"] == row["repository"]
                     and oid not in current_ids and r["scope"] in complete and r["sha256"] == h
                     and r.get("present", True)]
            if len(moves) == 1 and arrivals[(row["repository"], row["scope"], h)] == 1:
                before = moves[0]
                entry, prior_path = before["entry_id"], before["path"]
                history = list(before["history"])
                change = "moved"
        version = {k: row.get(k) for k in ("commit", "path", "ref", "worktree", "kind")}
        version["sha256"] = h
        if not history or history[-1] != version:
            history.append(version)
        record = dict(row, sha256=h, bytes=len(content), entry_id=entry, history=history,
                      present=True, object="objects/" + h)
        old[sid] = record
        changes.append({"source_id": sid, "entry_id": entry, "change": change, "path": row["path"],
                        "scope": row["scope"], "sha256": h, "previous_path": prior_path})
    for sid, row in previous.items():
        if row["scope"] in complete and row["repository"] == coverage["repository"] and sid not in current_ids:
            old[sid]["present"] = False
            if row.get("present", True):
                changes.append({"source_id": sid, "entry_id": row["entry_id"], "change": "not-present",
                                "path": row["path"], "scope": row["scope"]})
    # Deduplicate bytes, never branch identity or semantic conclusions.
    duplicates = {}
    for sid, row in old.items():
        if row.get("present"):
            duplicates.setdefault(row["sha256"], []).append(sid)
    duplicate_groups = [ids for ids in duplicates.values() if len(ids) > 1]
    run = {"at": datetime.now(timezone.utc).isoformat(), "coverage": coverage, "scopes": scopes,
           "complete_scopes": sorted(complete), "errors": errors, "exclusions": exclusions,
           "changes": changes, "navigation": findings, "duplicate_content_groups": duplicate_groups}
    state["last_run"] = run
    atomic(out / "index.json", state)
    atomic(out / "last-run.json", run)
    lines = ["# 来源接收", "", "这里只记录来源及变化，不自动生成语义待办或认定正式采用。", ""]
    for c in changes:
        lines.append(f"- {c['change']} | {c['scope']} | {c['path']} | entry {c['entry_id']}")
    (out / "intake.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"sources": len(incoming), "coverage_complete": not errors and set(scopes).issubset(complete), "changes": {c: sum(x["change"] == c for x in changes)
            for c in sorted({x["change"] for x in changes})},
            "errors": len(errors), "navigation_findings": len(findings),
            "duplicate_content_groups": len(duplicate_groups)}


def collect(args):
    repo, out = Path(args.repo).resolve(), Path(args.out).resolve()
    declared = [safe_relative(p) for p in args.source_path]
    rows = [] if args.no_worktrees else worktrees(repo)
    # Reject output inside a candidate source directory to prevent self-intake.
    roots = [repo] + [Path(w["path"]).resolve() for w in rows if not w.get("bare")]
    for root in roots:
        if out == root or (out.is_relative_to(root) and selected(out.relative_to(root).as_posix(), declared)):
            raise ValueError("Receipt output cannot be inside a scanned learning source or checkout root")
    incoming, errors, exclusions, findings, scopes, complete = [], [], [], [], [], set()
    refs = args.ref or ["HEAD"]
    for ref in dict.fromkeys(refs):
        scope = "ref:" + ref
        scopes.append(scope)
        try:
            commit = git_text(repo, "rev-parse", "--verify", ref + "^{commit}")
            tree = git(repo, "ls-tree", "-rz", "--full-tree", commit)
            entries = {}
            for field in tree.split(b"\0"):
                if not field:
                    continue
                meta, path = field.split(b"\t", 1)
                mode, typ, oid = meta.decode().split()
                entries[path.decode("utf-8")] = (mode, typ, oid)
            files = set(entries)
            read = lambda p: git(repo, "cat-file", "blob", entries[p][2])
            candidates = set()
            for path, (mode, typ, oid) in entries.items():
                if not selected(path, declared):
                    continue
                if excluded(path, declared, args.exclude):
                    exclusions.append({"scope": scope, "path": path, "reason": "excluded path"})
                    continue
                if typ != "blob" or mode == "120000":
                    exclusions.append({"scope": scope, "path": path, "reason": "symlink or non-blob"})
                    continue
                candidates.add(path)
                incoming.append(({"repository": args.name, "scope": scope, "kind": "git",
                                  "ref": ref, "commit": commit, "path": path, "repo_path": str(repo),
                                  "role": "document" if PurePosixPath(path).suffix.lower() in TEXT else "asset"}, read(path)))
            findings += navigation(files, read, candidates | (set(NAV + args.nav) & files), scope)
            complete.add(scope)
        except (OSError, ValueError, RuntimeError, UnicodeError) as e:
            errors.append({"scope": scope, "error": str(e)})
    for wt in rows:
        if wt.get("bare"):
            exclusions.append({"path": wt["path"], "reason": "bare worktree"})
            continue
        root = Path(wt["path"]).resolve()
        scope = "worktree:" + os.path.normcase(str(root))
        scopes.append(scope)
        files, had_error = set(), [False]
        def onerror(e):
            had_error[0] = True
            errors.append({"scope": scope, "path": e.filename, "error": str(e)})
        if not root.is_dir():
            onerror(FileNotFoundError("Registered worktree is unavailable", str(root)))
            continue
        for parent, dirs, names in os.walk(root, followlinks=False, onerror=onerror):
            for d in list(dirs):
                path = Path(parent) / d
                rel = path.relative_to(root).as_posix()
                if excluded(rel, declared, args.exclude) or redirected(path):
                    dirs.remove(d)
                    exclusions.append({"scope": scope, "path": rel, "reason": "cache/excluded/redirected directory"})
            for name in names:
                p = Path(parent) / name
                rel = p.relative_to(root).as_posix()
                files.add(rel)
        candidates = set()
        for path in sorted(files):
            if not selected(path, declared):
                continue
            if excluded(path, declared, args.exclude):
                exclusions.append({"scope": scope, "path": path, "reason": "excluded path"})
                continue
            p = root / path
            if p.is_symlink():
                exclusions.append({"scope": scope, "path": path, "reason": "symlink file"})
                continue
            try:
                content = p.read_bytes()
                # Original bytes are the version for dirty and ignored files; HEAD is only a baseline.
                ignored = subprocess.run(["git", "-c", "safe.directory=" + str(root), "-C", str(root),
                                          "check-ignore", "--no-index", "--", path], capture_output=True)
                if ignored.returncode not in (0, 1):
                    raise RuntimeError(ignored.stderr.decode("utf-8", "replace"))
                incoming.append(({"repository": args.name, "scope": scope, "kind": "worktree",
                                  "worktree": str(root), "ref": wt.get("branch", "detached"),
                                  "commit": wt.get("head"), "path": path, "ignored": ignored.returncode == 0,
                                  "role": "document" if p.suffix.lower() in TEXT else "asset"}, content))
                candidates.add(path)
            except (OSError, RuntimeError) as e:
                onerror(e)
        findings += navigation(files, lambda p: (root / p).read_bytes(),
                               candidates | (set(NAV + args.nav) & files), scope)
        if not had_error[0]:
            complete.add(scope)
    with writer(out) as state:
        result = receive(out, state, incoming, scopes, complete, errors, exclusions, findings,
                         {"repository": args.name, "repo": str(repo), "refs": refs,
                          "worktrees": rows, "declared_paths": declared, "exclusions": args.exclude})
    return result


def ingest(args):
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    incoming = []
    for row in manifest["sources"]:
        # The Agent resolves GitHub pages/trees and saves complete bytes, not excerpts.
        for key in ("repository", "ref", "commit", "path", "file", "sha256"):
            if not isinstance(row.get(key), str) or not row[key]:
                raise ValueError("Manifest missing " + key)
        if not re.fullmatch("[a-fA-F0-9]{40,64}", row["commit"]):
            raise ValueError("A fixed full commit is required")
        row["path"] = safe_relative(row["path"])
        content = (Path(args.manifest).resolve().parent / row["file"]).read_bytes()
        if digest(content) != row["sha256"]:
            raise ValueError("Manifest bytes/hash mismatch")
        metadata = {k: v for k, v in row.items() if k not in ("file", "sha256")}
        metadata.update(kind="remote", scope="ref:" + row["ref"])
        incoming.append((metadata, content))
    repos = {r["repository"] for r, _ in incoming}
    if manifest.get("repository"):
        repos.add(manifest["repository"])
    if len(repos) != 1:
        raise ValueError("Ingest one repository per invocation; reuse the same output for others")
    heads = manifest.get("heads", {})
    complete = set()
    for ref in manifest.get("complete_refs", []):
        if not re.fullmatch("[a-fA-F0-9]{40,64}", heads.get(ref, "")):
            raise ValueError("Complete remote scopes require fixed heads")
        if any(r["ref"] == ref and r["commit"] != heads[ref] for r, _ in incoming):
            raise ValueError("Mixed source commits in complete scope")
        complete.add("ref:" + ref)
    with writer(Path(args.out)) as state:
        return receive(Path(args.out), state, incoming, sorted({r["scope"] for r, _ in incoming} | complete),
                       complete, manifest.get("errors", []), manifest.get("exclusions", []), manifest.get("navigation", []),
                       {"repository": next(iter(repos)), "manifest": str(Path(args.manifest).resolve()),
                        "complete_scope": bool(complete), "heads": heads})


def source(args):
    state = json.loads((Path(args.out) / "index.json").read_text(encoding="utf-8"))
    row = state["sources"][args.source_id]
    content = (Path(args.out) / row["object"]).read_bytes()
    if digest(content) != row["sha256"]:
        raise ValueError("Received original is missing or corrupt; source cleanup forbidden")
    return row, content


def restore(args):
    row, content = source(args)
    root = Path(args.dest).resolve()
    relative = PurePosixPath(safe_relative(row["path"]))
    dest = root / relative
    # Inspect every existing component before creating any directory. is_symlink()
    # alone does not recognize Windows directory junctions/reparse points.
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if os.path.lexists(cursor):
            info = cursor.lstat()
            redirected = cursor.is_symlink() or bool(
                getattr(info, "st_file_attributes", 0) & 1024)
            if redirected or not cursor.resolve().is_relative_to(root):
                raise ValueError("Restore destination escapes its root or uses a redirected component")
    if not dest.resolve().is_relative_to(root):
        raise ValueError("Restore destination escapes its root")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.resolve().is_relative_to(root):
        raise ValueError("Restore path changed; stop and inspect concurrent changes")
    if dest.exists() and dest.read_bytes() != content:
        raise ValueError("Restore target has different content; preserving it")
    if not dest.exists():
        with dest.open("xb") as f:
            f.write(content)
    return {"restored": str(dest), "sha256": digest(content)}


def cleanup_check(args):
    row, content = source(args)
    if row["kind"] == "git":
        repo = Path(row["repo_path"])
        tip = git_text(repo, "rev-parse", "--verify", row["ref"] + "^{commit}")
        if tip != row["commit"]:
            return {"eligible": False, "reason": "source branch moved; receive/review its current version"}
        current = git(repo, "show", tip + ":" + row["path"])
    elif row["kind"] == "worktree":
        p = Path(row["worktree"]) / safe_relative(row["path"])
        if p.is_symlink() or not p.resolve().is_relative_to(Path(row["worktree"]).resolve()):
            return {"eligible": False, "reason": "source path redirected"}
        current = p.read_bytes()
    else:
        return {"eligible": False, "reason": "remote source requires fresh platform read and branch check"}
    ok = current == content
    return {"eligible": ok, "reason": "bytes unchanged; adoption, durable recovery and authorization still required"
            if ok else "source changed; original preserved, receive/review new content first",
            "current_sha256": digest(current), "received_sha256": row["sha256"],
            "deletion_performed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("collect")
    p.add_argument("--repo", required=True)
    p.add_argument("--name", required=True, help="Stable repository identity, e.g. owner/repository")
    p.add_argument("--ref", action="append", default=[])
    p.add_argument("--source-path", action="append", default=[], help="Source path confirmed from project conventions")
    p.add_argument("--exclude", action="append", default=[])
    p.add_argument("--nav", action="append", default=[])
    p.add_argument("--no-worktrees", action="store_true")
    p.add_argument("--out", required=True)
    p = sub.add_parser("ingest")
    p.add_argument("--manifest", required=True)
    p.add_argument("--out", required=True)
    for name in ("restore", "check-cleanup"):
        p = sub.add_parser(name)
        p.add_argument("--out", required=True)
        p.add_argument("--source-id", required=True)
        if name == "restore":
            p.add_argument("--dest", required=True)
    args = parser.parse_args()
    try:
        result = {"collect": collect, "ingest": ingest, "restore": restore,
                  "check-cleanup": cleanup_check}[args.command](args)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, RuntimeError, KeyError, json.JSONDecodeError) as e:
        print(json.dumps({"error": str(e), "mutation": "no source deletion performed"}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
