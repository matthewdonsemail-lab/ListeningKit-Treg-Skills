---
name: treg-call
description: Call a catalog endpoint or a team tool through the proxy; keys injected server-side.
---

# treg-call

```bash
treg call scrapecreators.reddit.subreddit.posts --query subreddit=news
treg call <endpoint> [--method POST] [--query k=v] [--data '{...}']
# team tool: <tool-name> + upstream path, exactly as its own docs say
treg call intercom conversations?per_page=5
```

Observed endpoints: google-analytics.report, treg.x.user.posts, anyapi.x.user.posts.timeline, treg.x.post.comments, treg.x.search.posts, anyapi.twitter.following ($0.00045/call), scrapecreators.x.v1-facebook-adlibrary-search-ads, google-search-console.
Over HTTP: GET https://treg.to/call/<tool-name>/<path> with X-Treg-Token header (stripped before upstream). The proxy relays, never models.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
