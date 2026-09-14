---
name: mongodb-development
description: Set up, connect to, inspect, back up, restore, and troubleshoot MongoDB for development workflows. Use for MongoDB services, Compass, PyMongo, CRUD, indexes, or local data operations; do not apply local-development defaults to production systems.
---

# MongoDB Development

Determine whether the target is local, containerized, managed, or production
before proposing configuration. Prefer read-only diagnostics before mutations.

## Workflow

1. Inspect the server/client versions, service state, connection target, and authentication mode.
2. Verify connectivity with the least-privileged applicable identity.
3. Keep credentials and connection strings out of source control and command output.
4. For queries or writes, confirm database, collection, filter, and expected scope.
5. For performance work, inspect query shape and execution evidence before adding indexes.
6. For backup or restore, record namespaces and options, then verify the produced or restored data.

Dropping data, overwriting during restore, changing authentication, or modifying
a production deployment requires explicit confirmation of the exact target.
Version-sensitive commands should be checked against current official
documentation. The [MongoDB Wiki guide](../../wiki/mongodb/README.md) is
introductory background rather than production guidance.
