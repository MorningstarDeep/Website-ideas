# Micro-tool opportunity research — method & data sources

## Why this method

Prior session's finding (2026-08-21, 22:25): 23 "obvious" tool keywords across 12 verticals
were all saturated (6–10 dedicated competitors each). Conclusion: **any keyword a
generalist tool-builder can guess is already built.** Confirmed again on first probe —
`weaving sett calculator` already has 8 dedicated calculators including AI-farm domains
(calcimator, textilecalculator, fibertools.app, yarnplot).

So the search must start from **vocabulary a generalist does not possess**: insider jargon
of trades, crafts, and professions. The filter is not "is this a good tool idea" but
"would a person outside this niche even know this word exists?"

## Data sources — what works, what doesn't

| Source | Status | Used for |
|---|---|---|
| Google Autocomplete (`/complete/search?client=chrome`) | ✅ works, unlimited | Real query language + demand floor |
| Bing Autocomplete (`api.bing.com/osjson.aspx`) | ✅ works | Cross-check |
| YouTube Autocomplete (`&ds=yt`) | ✅ works | Intent cross-check |
| DuckDuckGo HTML (`html.duckduckgo.com/html/`) | ✅ works, scriptable | Bulk SERP composition |
| Google Trends API (with cookie jar) | ✅ works (429 without cookies) | Relative demand, tier-2 terms only |
| WebSearch tool | ✅ works | Closest proxy to Google SERP |
| WebFetch / real Chrome | ✅ works (non-Google) | Competitor quality audit |
| vidIQ MCP `keyword_research` | ✅ works | YouTube volume as corroborating signal |
| Google SERP scrape (curl or automated Chrome) | ❌ JS shell / `/sorry` captcha | — |
| Ahrefs / Ubersuggest / SpyFu / Wordtracker / searchvolume.io free APIs | ❌ auth, Turnstile, or JS-only | — |

### Consequence for search volume

**No paid keyword tool is available, so no exact Google volumes exist in this research.**
Per the brief ("Do NOT invent numbers"), volume is reported as a **band with stated basis**,
never as a fake precise figure. Bands are derived from converging signals:

1. **Autocomplete presence** — Google suppresses queries below a popularity threshold from
   suggestions. A term appearing in autocomplete is a demand *floor*, not a number.
2. **Autocomplete breadth** — how many distinct completions an a–z expansion produces.
   Wide expansion = real cluster, not a one-off.
3. **Google Trends** — only resolves above ~1k/mo; useful to separate tier 1 from tier 2.
4. **vidIQ YouTube volume** — real integers, different intent pool, correlates for
   craft/DIY/trade topics.
5. **Community size** — subreddit subscribers, forum post counts = audience ceiling.
6. **Competitor count** — a niche with 8 dedicated tools has provable commercial demand.

Every idea in the final report carries an explicit confidence label on its volume band.

## Pipeline

```
Phase 1  jargon seeds (hand-built, domain knowledge)
Phase 2  harvest.py suggest   → real Google queries per seed
Phase 3  filter to tool-intent queries
Phase 4  harvest.py serp      → SERP composition per candidate
Phase 5  auto-score SERP weakness → shortlist
Phase 6  manual deep-dive: competitor UX audit, Reddit frustration, build cost
Phase 7  report per Requirements.md
```

## SERP weakness auto-score

Result kinds classified by `harvest.py:classify()`. A candidate scores well when the top 10
contains few `site` results that are *dedicated tools*, and many of:
forum / social-video / shop / pdf / edu-gov / wiki.

Auto-score is a **screen, not a verdict** — every shortlisted candidate gets manual SERP
review, because domain-name classification cannot tell a dedicated tool from a blog post.

## Files

- `harvest.py` — the harvester
- `seeds-jargon.txt` — Phase 1 seed vocabulary
- `data/` — JSONL outputs (gitignored-size, append-only, resumable)
