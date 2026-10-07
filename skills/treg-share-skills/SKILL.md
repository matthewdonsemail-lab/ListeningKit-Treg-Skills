---
name: treg-share-skills
description: Register keys wrapped in skills so teammates call without holding credentials.
---

# treg-share-skills

Bulk fast path - run in the directory the human names:
```bash
treg upload
```
New key/endpoint/CLI defaults to wrapped in a skill: proper SKILL.md (frontmatter matters - agents discover by it) + one example call, then treg skill init --dir ./posthog, review treg.json, treg skill add --dir ./posthog.
Never orphan a secret: a stored key nothing binds is dead weight. Bare endpoint only when a skill adds nothing (treg secret add + treg tool add with --auth-in/--auth-name as needed).
Secrets are write-only - the API never returns a stored value. A tool may bind a teammate-shared secret: delegated, org-scoped, logged against the caller's token.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
