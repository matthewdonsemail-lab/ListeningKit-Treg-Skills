---
name: treg-price-check
description: Read exact price, params and reliability stats with catalog get before every call.
---

# treg-price-check

```bash
treg catalog get scrapecreators.reddit.subreddit.posts
```

Every endpoint page shows params, PRICE, COST/WORKS (observed success rate + sample size)/SPEED/LAST OK. Example seen in the wild: treg.x.search.posts served by anyapi.x.search.posts at `$0.00075/success`, 201,648 observed calls at 100%.

Say the price before you spend it. No published price = refused, connect your own key.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
