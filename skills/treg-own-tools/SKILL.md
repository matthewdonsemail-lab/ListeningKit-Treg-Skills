---
name: treg-own-tools
description: Call tools the team registered: start from what is registered, use the upstream API exactly.
---

# treg-own-tools

```bash
treg tool ls
treg call intercom conversations?per_page=5
```

Discover with treg tool ls / treg skill ls. Only tools this org registered resolve. No treg vocabulary, no special params - the upstream API exactly as its docs say. Calls on team tools spend nothing: that key belongs to them.
Programmatic pattern (ui-kit lib/template-sites/tomba.ts): spawn treg call ... --json, unwrap data/result, surface cost_usd. Same pattern in google-reviews.ts for dataforseo business-data endpoints.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
