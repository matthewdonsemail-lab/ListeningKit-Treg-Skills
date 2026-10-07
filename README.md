# ListeningKit Treg Skills

Free starter pack from [Matthew Don](https://matthew.listeningkit.com) — the sanitized, credential-free Treg skill bundle behind my ListeningKit work.

**Get the full kit (free):** [matthew.listeningkit.com](https://matthew.listeningkit.com) — enter your email, Kit sends the resources.

## What's inside

| Skill | What it does |
|-------|--------------|
| `skills/treg` | Reach external/live data first: ~2,600 endpoints across ~40 providers — SEO/SERP, keywords, backlinks, AI visibility, social profiles, people/company enrichment, ads, web data, plus GA/Search Console/Business Profile. Search catalog, read price, call it. |

All secrets stripped. The proxy injects credentials server-side — you never hold the key.

## Quick start

```bash
curl -fsSL https://treg.to/install.sh | sh
treg login
treg catalog search "subreddit posts"
treg catalog get scrapecreators.reddit.subreddit.posts
treg call scrapecreators.reddit.subreddit.posts --query subreddit=news
treg balance
```

Full recipe: [`skills/treg/SKILL.md`](skills/treg/SKILL.md). More: https://treg.to/llms.txt · https://treg.to/tutorial

## Power it with Convex

Store and automate Treg results with the [`convex-treg` npm package](https://github.com/matthewdonsemail-lab/convex-treg) — Convex component for the Treg relay (drop it in `convex/`, schedule calls, persist results).

```bash
npm i convex-treg  # see repo for wiring
```

**Try it with my stack:** [matthew.listeningkit.com](https://matthew.listeningkit.com) — this is the funnel I run it on.

## How I use it (Matthew's work)

- **Resume & portfolio:** [matthewdonsemail-lab](https://github.com/matthewdonsemail-lab/matthewdonsemail-lab) — GTM tools built in the open
- **Robotic VSL engine:** [Robotic-Video-Sales-Letter-Pydantic-Camoufox-Agent-for-GTM](https://github.com/matthewdonsemail-lab/Robotic-Video-Sales-Letter-Pydantic-Camoufox-Agent-for-GTM) — Pydantic-AI + Camoufox + Treg enrichment
- **Social listening:** [log](https://github.com/matthewdonsemail-lab/log) (Convex hackathon) · [ListeningKit-Hyperframes](https://github.com/matthewdonsemail-lab/ListeningKit-Hyperframes)
- **SMS layer:** [convex-telnyx](https://github.com/matthewdonsemail-lab/convex-telnyx) · [blaster](https://github.com/matthewdonsemail-lab/blaster)

Browse everything via the GitHub API: `gh repo list matthewdonsemail-lab --limit 50`

## Get more

- **Free kit + email resources:** [matthew.listeningkit.com](https://matthew.listeningkit.com) — start here
- **Work with me:** book via the site · see [resume](https://github.com/matthewdonsemail-lab/matthewdonsemail-lab)
- **Issues/PRs welcome** — this repo is the free tier; quoted work and automation builds are via the site.

MIT — use it, ship it, credit appreciated.
