"""Choose read-only document actions from independent local/remote baselines.

This helper never transfers data or updates a baseline. A batch is an explicit
list, not a directory scan. Relative batch paths use the snapshot file's folder.
"""
import argparse
import json
import os
from pathlib import Path


def decide(direction, local, remote, baseline=None):
    if direction not in {'upload', 'download', 'both'}:
        raise ValueError('direction must be upload, download or both')
    if any(value is not None and (not isinstance(value, str) or not value) for value in (local, remote)):
        raise ValueError('content fingerprints must be nonempty strings or null')
    if baseline is not None:
        if not isinstance(baseline, dict) or any(not isinstance(baseline.get(side), str) or not baseline[side] for side in ('local', 'remote')):
            raise ValueError('baseline needs verified local and remote fingerprints')
        if local is None or remote is None:
            return {'action': 'needs_confirmation', 'reason': 'previously tracked side is missing; no deletion or recreation'}
        local_changed = local != baseline['local']
        remote_changed = remote != baseline['remote']
        if local_changed and remote_changed:
            return {'action': 'conflict', 'reason': 'both sides changed since the verified baseline'}
        if not local_changed and not remote_changed:
            return {'action': 'unchanged', 'reason': 'both sides match the verified baseline'}
        wanted = 'upload' if local_changed else 'download'
    else:
        if (local is None) == (remote is None):
            return {'action': 'needs_confirmation', 'reason': 'no baseline and no unique initial source'}
        wanted = 'upload' if local is not None else 'download'
    if direction not in {wanted, 'both'}:
        return {'action': 'needs_confirmation', 'reason': 'changed/source side is outside the requested direction'}
    return {'action': wanted, 'reason': 'single source or one-sided change permitted by direction'}


def decide_batch(items, base_dir='.'):
    """Reject ambiguous mappings first, then isolate per-document input errors.

    Each item needs id, local_path, receipt and a caller-verified remote_key.
    remote_key is case-sensitive: cloud identifiers are not Windows paths.
    """
    if not isinstance(items, list) or not items:
        raise ValueError('items must be a nonempty list')
    seen = {field: set() for field in ('id', 'local_path', 'receipt', 'remote_key')}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('each batch item must be an object')
        for field in seen:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip() or value != value.strip() or '\x00' in value:
                raise ValueError(f'each batch item needs a nonempty {field}')
            if field in ('local_path', 'receipt'):
                value = os.path.normcase(str((Path(base_dir) / value).resolve()))
            if value in seen[field]:
                raise ValueError(f'duplicate batch {field}')
            seen[field].add(value)
    for document in seen['local_path']:
        for receipt in seen['receipt']:
            try:
                shared = os.path.commonpath((document, receipt))
            except ValueError:
                continue  # Different drives cannot overlap.
            if shared in (document, receipt):
                raise ValueError('a batch receipt overlaps a local document path')
    results = []
    counts = {}
    for item in items:
        try:
            result = decide(item['direction'], item['local'], item['remote'], item.get('baseline'))
        except (KeyError, ValueError, TypeError) as error:
            result = {'action': 'failed', 'reason': str(error)}
        results.append({'id': item['id'], **result})
        counts[result['action']] = counts.get(result['action'], 0) + 1
    return {'items': results, 'counts': counts}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', help='JSON with direction/local/remote/baseline, or an explicit items list')
    args = parser.parse_args()
    try:
        path = Path(args.snapshot).resolve()
        with path.open(encoding='utf-8') as stream:
            snapshot = json.load(stream)
        if not isinstance(snapshot, dict):
            raise ValueError('snapshot must be an object')
        if 'items' in snapshot:
            if {'direction', 'local', 'remote', 'baseline'} & snapshot.keys():
                raise ValueError('do not mix single-document fields with items')
            result = decide_batch(snapshot['items'], path.parent)
        else:
            result = decide(snapshot['direction'], snapshot['local'], snapshot['remote'], snapshot.get('baseline'))
        print(json.dumps(result, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')
