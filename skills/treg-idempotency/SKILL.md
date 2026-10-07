---
name: treg-idempotency
description: Retry timed-out calls free with idempotency keys; never reuse a key for new work.
---

# treg-idempotency

Timed out or never saw the answer? Repeat with the same idempotency_key (MCP) or Idempotency-Key header (HTTP). Treg returns the stored answer, skips the provider, charges nothing. Result says replayed: true.
Only for genuine retries. Asking the same question again to see what changed is NEW work - new key or none, or you get the old answer. Reusing one key for a different request is refused. Failed calls were never billed anyway.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
