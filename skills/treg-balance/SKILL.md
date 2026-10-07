---
name: treg-balance
description: Check prepaid balance and recent charges; recover from 402 out-of-balance.
---

# treg-balance

```bash
treg balance
```

HTTP 402 = out of balance with machine-actionable body (balance_micro, estimated_cost_micro, topup_url). Recovery: treg balance, top up in dashboard (Team Billing), or store the org's own key for that provider (own keys take priority automatically, never billed).
Cost discipline: quote per-call cost + total before running (e.g. '~$0.60 total' for a 254-ad scan).

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
