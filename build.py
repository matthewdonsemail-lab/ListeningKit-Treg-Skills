import os
base = r"C:\Users\0\.buzz\.scratch\lk-treg-skills\skills"
FOOT = "\n\n---\n\nFree starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).\n"
skills = [
("treg-catalog-search", "Find the right endpoint before spending: search ~2,600 endpoints across ~40 providers by task.", """Search the catalog by what the job needs, not by provider name.

```bash
treg catalog search "subreddit posts"
treg catalog search "backlink gap"
treg catalog search "work email"
treg catalog search "tiktok profile"
```

Start from the task (backlinks, keyword volume, ad creative, enrichment) and let the catalog return candidate endpoint ids. Then price them with the treg-price-check skill before calling.
Source pattern: employmentArc treg/buzz-usage/CALL_PATTERNS.md - discovery before spend, every time."""),
("treg-price-check", "Read exact price, params and reliability stats with catalog get before every call.", """```bash
treg catalog get scrapecreators.reddit.subreddit.posts
```

Every endpoint page shows params, PRICE, COST/WORKS (observed success rate + sample size)/SPEED/LAST OK. Example seen in the wild: treg.x.search.posts served by anyapi.x.search.posts at `$0.00075/success`, 201,648 observed calls at 100%.

Say the price before you spend it. No published price = refused, connect your own key."""),
("treg-call", "Call a catalog endpoint or a team tool through the proxy; keys injected server-side.", """```bash
treg call scrapecreators.reddit.subreddit.posts --query subreddit=news
treg call <endpoint> [--method POST] [--query k=v] [--data '{...}']
# team tool: <tool-name> + upstream path, exactly as its own docs say
treg call intercom conversations?per_page=5
```

Observed endpoints: google-analytics.report, treg.x.user.posts, anyapi.x.user.posts.timeline, treg.x.post.comments, treg.x.search.posts, anyapi.twitter.following ($0.00045/call), scrapecreators.x.v1-facebook-adlibrary-search-ads, google-search-console.
Over HTTP: GET https://treg.to/call/<tool-name>/<path> with X-Treg-Token header (stripped before upstream). The proxy relays, never models."""),
("treg-balance", "Check prepaid balance and recent charges; recover from 402 out-of-balance.", """```bash
treg balance
```

HTTP 402 = out of balance with machine-actionable body (balance_micro, estimated_cost_micro, topup_url). Recovery: treg balance, top up in dashboard (Team Billing), or store the org's own key for that provider (own keys take priority automatically, never billed).
Cost discipline: quote per-call cost + total before running (e.g. '~$0.60 total' for a 254-ad scan)."""),
("treg-pick-provider", "Choose between providers of one capability: inputs first, then reliability, then price.", """Procedure from treg catalog get output:
1. Match the inputs you HAVE. An endpoint wanting profile_url is no substitute when you hold name+domain. Outranks price every time.
2. Reliability: high WORKS with real sample beats rounder number with tiny one - 99% (121) beats 100% (8).
3. Price. Spreads inside one capability reach 200x.
4. LAST OK breaks ties. Bare age = real call; check-mark age = catalog verification stamp, not live traffic; dash = unverified.
429/5xx/timeout: try the next provider. Never retry a 4xx elsewhere - 4xx is your params; fixing them is the fix.
treg does not choose or fail over for you. That is deliberate."""),
("treg-idempotency", "Retry timed-out calls free with idempotency keys; never reuse a key for new work.", """Timed out or never saw the answer? Repeat with the same idempotency_key (MCP) or Idempotency-Key header (HTTP). Treg returns the stored answer, skips the provider, charges nothing. Result says replayed: true.
Only for genuine retries. Asking the same question again to see what changed is NEW work - new key or none, or you get the old answer. Reusing one key for a different request is refused. Failed calls were never billed anyway."""),
("treg-own-tools", "Call tools the team registered: start from what is registered, use the upstream API exactly.", """```bash
treg tool ls
treg call intercom conversations?per_page=5
```

Discover with treg tool ls / treg skill ls. Only tools this org registered resolve. No treg vocabulary, no special params - the upstream API exactly as its docs say. Calls on team tools spend nothing: that key belongs to them.
Programmatic pattern (ui-kit lib/template-sites/tomba.ts): spawn treg call ... --json, unwrap data/result, surface cost_usd. Same pattern in google-reviews.ts for dataforseo business-data endpoints."""),
("treg-share-skills", "Register keys wrapped in skills so teammates call without holding credentials.", """Bulk fast path - run in the directory the human names:
```bash
treg upload
```
New key/endpoint/CLI defaults to wrapped in a skill: proper SKILL.md (frontmatter matters - agents discover by it) + one example call, then treg skill init --dir ./posthog, review treg.json, treg skill add --dir ./posthog.
Never orphan a secret: a stored key nothing binds is dead weight. Bare endpoint only when a skill adds nothing (treg secret add + treg tool add with --auth-in/--auth-name as needed).
Secrets are write-only - the API never returns a stored value. A tool may bind a teammate-shared secret: delegated, org-scoped, logged against the caller's token."""),
("treg-teams-agents", "Orgs, roles, invites and per-agent tokens with caps, scopes and attribution.", """```bash
treg org create "Team A"
treg org invite teammate@company.com --role member
treg org agent-new ci-bot
treg org agent-new ci-bot --tools stripe,gh --cap 500
treg health
treg health --run
```

Roles: owner > admin > member > viewer; members manage only what they created. Invitee signs in with invited email, runs treg accept. New invitees get a personal org so removal never locks them out.
Agent tokens (TREG_TOKEN env): call team tools + read only - never sign in, create teams, or own. Every call capped, scoped, logged as itself in treg calls. Give tools a health_check probe so treg can validate."""),
("treg-oauth-connect", "Hosted OAuth connect vs manual token upload; auto-refresh vs manual mode.", """Two ways to get the first OAuth token:
- Manual: own OAuth locally, then treg secret add gsc --file token.json --kind oauth.
- Hosted: treg oauth connect gsc --client-secret client_secret.json --scopes <scope> - prints consent URL, approve in browser, treg captures directly. One-time setup: add https://treg.to/oauth/callback to redirect URIs.
Auto mode: secret carries refresh_token + client_id + client_secret - treg refreshes before expiry, never re-upload. Manual mode: bare token injected as-is, re-upload on expiry. Same storage; credentials graduate with no migration."""),
("buzz-treg-call-patterns", "Treg CLI patterns as actually used in Buzz sessions: discovery, calls, outputs.", """Discovery: catalog search <keyword> (GA4, X, Ad Library, Serpstat/SpyFu); catalog get <endpoint> (routing + unit cost); catalog request "<name>" for gaps (e.g. Bing Webmaster Tools); treg connections to verify OAuth before GA4 calls.
Outputs: raw JSON lands under .scratch/ (e.g. .scratch/treg/q1..q6.out.json), curated results promoted to RESEARCH/*.md with endpoint + cost + raw-data pointer.
Source: employmentArc treg/buzz-usage/CALL_PATTERNS.md."""),
("buzz-treg-sessions", "How Treg work runs inside Buzz: scan channels for prior art before new calls.", """Before new spend, scan channel history for prior calls on the same job - richest veins observed: agency-recruitment-handoff (treg/ convention, 4 priced endpoints, per-provider READMEs), blaster (ICP hiring-signals job), ui-kit (treg-to-prospects pipeline).
Track sessions: what was called, endpoint + params, cost, where raw output landed. Source: employmentArc treg/buzz-usage/SESSIONS.md + treg/data-lake/CONVERSATIONS.md."""),
("x-research-playbook", "X audience research via Treg: timelines, comments, search, following with observed costs.", """Studies with receipts (employmentArc treg/workflows/X_RESEARCH.md):
- Top-post commenters: treg.x.user.posts + anyapi.x.user.posts.timeline (2 pages); treg.x.post.comments on 14 posts (~$0.002 + ~$0.007).
- RevOps X accounts: treg.x.search.posts via anyapi.x.search.posts ($0.00075/success).
- Sub-500 GTM accounts: anyapi.twitter.following, max 3 cursor pages x 13 accounts ($0.00045/call).
- Pricing proof: treg call treg.x.search.posts; catalog get (201,648 calls, 100%).
Caveat: follower counts absent on commenter objects - treg.x.user enrichment needed before reach-tiering."""),
("x-remote-roles-sourcing", "Source remote growth/GTM roles on X with tiered triage: direct-contact vs aggregator.", """20 queries via treg.x.search.posts (~$0.013) returned 236 posts; rules (remote + top-level + hiring words + role match + dedupe) cut to 33 distinct roles. Tier A: founder/company posts with direct apply (reply, DM, or email). Tier B: job-board/aggregator links.
Widen with date windows, more role words, remote synonyms (WFH, anywhere); pull boards directly (anyapi.linkedin.search.jobs) for same titles. Confirm remote flag on the listing - filters lie. Source: employmentArc research/xRemoteGrowthRoles.md."""),
("outreach-email-that-gets-replies", "Human-written cold email: candid, specific, outcomes first, video + site link.", """Match what the post says: email where it says email, DM where it says DM, never DM a no-DMs post. Where email: candid, specific, leading with outcomes, with a video and the site link (the Ordo growth-intern email got a CTO reply).
Template floor observed: $0.01 X template; Ordo hook call $0.0011. Sources: employmentArc research/ordoGrowthInternHook.md + xHumanWrittenEmailTemplate.md."""),
("ads-library-scan", "Scan competitor ads via Facebook Ad Library endpoints; quote total before running.", """```bash
treg call scrapecreators.x.v1-facebook-adlibrary-search-ads --query ...
treg call scrapecreators.x.v1-facebook-adlibrary-ad --query ...
```
Observed: ~$0.60 total quoted upfront for a 254-ad scan. Use for competitor creative, angles, and spend signals. Source: employmentArc treg/workflows/ADS_LIBRARY.md."""),
("ga4-access-treg", "Query GA4 through Treg via connected OAuth - verify connection first.", """```bash
treg connections
treg call google-analytics.report --query ...
```
Verify the google-analytics OAuth account is connected before calling. Request missing connectors via treg catalog request. Source: employmentArc treg/workflows/GA4_ACCESS.md."""),
("trades-copy-lang", "Copy language for trades and local-service offers: plain words that book jobs.", """Short, concrete, suburb + service + proof. No SaaS adjectives. CTA is call/book, not signup. Source: employmentArc treg/workflows/TRADES_COPY_LANG.md."""),
("datalake-sources", "Index every Treg call site: channels, project code, research corpus - with pointers.", """Survey three layers: (1) Buzz channel history (last-N scan per channel, hits + nature); (2) project code (CLI spawn sites, endpoint ids, costs); (3) research corpus (docs with endpoint + cost + raw-data pointers).
Keep raw pulls disposable (.scratch/), promote curated to indexed markdown. Channels with zero hits are findings too - record the gap. Source: employmentArc treg/data-lake/SOURCES.md."""),
("datalake-tool-calls", "Log every Treg call with endpoint, params, cost and raw-data pointer.", """One row per call: endpoint id, params, cost_usd/charged_micro, status, raw output path. Read charged_micro off stored _treg documents for ledger-in-data (ui-kit source-motor-trade.ts pattern). No keys in logs or git - names of env vars only. Source: employmentArc treg/data-lake/TOOL_CALLS.md."""),
("datalake-projects-gaps", "Map docs and assets to projects; record gaps explicitly so they steer what gets added.", """Per project: which docs, which assets, which implementation reflects them, what is missing. Gaps observed in the wild: DMs unscanned, Philippines-boards coverage, follower-count enrichment. A gap file (GAPS.md) steers the next catalog requests. Sources: employmentArc treg/data-lake/PROJECTS.md + GAPS.md."""),
("resource-tool-page", "Publish each skill or tool as a page: what it does, price, one example call, CTA.", """Page shape: name, one-line job, price, single example call, link to full recipe, CTA to the free kit (https://matthew.listeningkit.com) and the convex-treg package. Source: employmentArc treg/brand/RESOURCE_TOOL_PAGE.md."""),
("treg-implementation-map", "Lock the reusable discipline: search, get, state price, call --json, balance, log.", """Section order: (1) discipline - catalog search, get, state price, call --json, balance, log endpoint/params/cost; (2) per-project map - which docs+assets feed which build; (3) enriched-data rule - document object + match key first, upsert never blind-create, webhook pattern as live example. Source: employmentArc treg/IMPLEMENTATION.md."""),
]
count = 0
for name, desc, body in skills:
    d = os.path.join(base, name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write("---\nname: " + name + "\ndescription: " + desc + "\n---\n\n# " + name + "\n\n" + body + FOOT)
    count += 1
print("wrote", count)
print("total dirs", len([x for x in os.listdir(base) if os.path.isdir(os.path.join(base, x))]))
