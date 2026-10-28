"""Choose a single-document action from independent local/remote baselines.

This helper never transfers data or updates a baseline. Hashes are comparable
only within the same side; Markdown bytes need not equal Feishu XML bytes.
"""
import argparse
import json


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', help='JSON containing direction, local, remote and optional baseline')
    args = parser.parse_args()
    try:
        with open(args.snapshot, encoding='utf-8') as stream:
            snapshot = json.load(stream)
        print(json.dumps(decide(snapshot['direction'], snapshot['local'], snapshot['remote'], snapshot.get('baseline')), ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')
