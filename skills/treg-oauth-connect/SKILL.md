---
name: treg-oauth-connect
description: Hosted OAuth connect vs manual token upload; auto-refresh vs manual mode.
---

# treg-oauth-connect

Two ways to get the first OAuth token:
- Manual: own OAuth locally, then treg secret add gsc --file token.json --kind oauth.
- Hosted: treg oauth connect gsc --client-secret client_secret.json --scopes <scope> - prints consent URL, approve in browser, treg captures directly. One-time setup: add https://treg.to/oauth/callback to redirect URIs.
Auto mode: secret carries refresh_token + client_id + client_secret - treg refreshes before expiry, never re-upload. Manual mode: bare token injected as-is, re-upload on expiry. Same storage; credentials graduate with no migration.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
