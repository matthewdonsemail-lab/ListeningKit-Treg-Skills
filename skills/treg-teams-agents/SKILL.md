---
name: treg-teams-agents
description: Orgs, roles, invites and per-agent tokens with caps, scopes and attribution.
---

# treg-teams-agents

```bash
treg org create "Team A"
treg org invite teammate@company.com --role member
treg org agent-new ci-bot
treg org agent-new ci-bot --tools stripe,gh --cap 500
treg health
treg health --run
```

Roles: owner > admin > member > viewer; members manage only what they created. Invitee signs in with invited email, runs treg accept. New invitees get a personal org so removal never locks them out.
Agent tokens (TREG_TOKEN env): call team tools + read only - never sign in, create teams, or own. Every call capped, scoped, logged as itself in treg calls. Give tools a health_check probe so treg can validate.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
