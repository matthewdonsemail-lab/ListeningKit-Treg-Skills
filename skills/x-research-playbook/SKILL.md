---
name: x-research-playbook
description: X audience research via Treg: timelines, comments, search, following with observed costs.
---

# x-research-playbook

Studies with receipts (employmentArc treg/workflows/X_RESEARCH.md):
- Top-post commenters: treg.x.user.posts + anyapi.x.user.posts.timeline (2 pages); treg.x.post.comments on 14 posts (~$0.002 + ~$0.007).
- RevOps X accounts: treg.x.search.posts via anyapi.x.search.posts ($0.00075/success).
- Sub-500 GTM accounts: anyapi.twitter.following, max 3 cursor pages x 13 accounts ($0.00045/call).
- Pricing proof: treg call treg.x.search.posts; catalog get (201,648 calls, 100%).
Caveat: follower counts absent on commenter objects - treg.x.user enrichment needed before reach-tiering.

---

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) - get the full kit there. Power automation with [convex-treg](https://github.com/matthewdonsemail-lab/convex-treg).
