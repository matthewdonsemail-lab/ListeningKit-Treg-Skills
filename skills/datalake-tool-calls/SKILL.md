---
name: datalake-tool-calls
description: Log every Treg call with endpoint, params, cost and raw-data pointer.
---

# datalake-tool-calls

One row per call: endpoint id, params, cost_usd/charged_micro, status, raw output path. Read charged_micro off stored _treg documents for ledger-in-data (ui-kit source-motor-trade.ts pattern). No keys in logs or git - names of env vars only. Source: employmentArc treg/data-lake/TOOL_CALLS.md.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
