# Microtools portfolio

19 single-purpose tool websites, **one built per month**, monetised with display ads.
Each site owns one keyword cluster; 34 validated tools are distributed across the 19 sites.

## Layout

```
research/          strategy, evidence, generators
websites/NN-slug/  one folder per site — open this folder to build that site
_archive/          superseded research from an earlier track. Safe to delete.
```

## Read these first

| File | What it is |
|---|---|
| `research/05-SITE-PLAN.md` | The 19 sites, build order, why that order |
| `research/04-TOOL-VALIDATION.md` | Per-seed evidence for all 34 tools — traffic, $/visit, geo, incumbents |
| `research/synonym-groups.md` | Keyword clusters with pre-built US-geo SERP links |
| `research/06-CROSS-LINKING.md` | Whether/how the 19 sites may link to each other |
| `websites/NN-slug/CLAUDE.md` | Per-site context, loaded automatically when that folder is open |

## ⚠ Generated files — do not hand-edit

`websites/*/BRIEF.md`, `websites/*/SEO-BRIEF.md`, `websites/*/CLAUDE.md` and
`websites/*/.vscode/` are **generated**. Hand edits are wiped on the next run.

To change them, edit the source and regenerate:

```
python research/make_sites.py demo    # self-check: all 34 tools map to exactly one site
python research/make_sites.py         # regenerate all 19 folders
```

| Change this | To edit |
|---|---|
| `research/make_sites.py` | site list, build order, risk tiers, BRIEF body, CLAUDE.md body, .vscode config |
| `research/seo_brief_body.py` | the 15-section SEO brief shared by all sites |
| `research/gen_links.py` | keyword synonym groups, then `python gen_links.py` |

## Portfolio-wide rules

1. **Never write library code from memory.** `context7` MCP for any library; `cloudflare` /
   `wrangler` skills for Cloudflare; `modern-web-guidance` before client JS. Latest **stable**.
2. **MPA, never SPA.** Real URLs, full page loads, content in the initial HTML.
3. **Deploy day 1** to Cloudflare Pages with `noindex` headers; custom domain and GSC last.
4. **No backlink building, no directory submissions.** On-page and technical quality is the
   only lever — so it has to be perfect.
   **No cross-link network between the 19 sites.** Default state is **zero cross-links**.
   Only on the operator's explicit instruction, only when a site needs a boost, only within
   the same audience cluster, **never before month 4–5**, and **one at a time with ~3 months
   between**. Never on launch, never in a batch, never on an agent's initiative.
   Full policy + link ledger: `research/06-CROSS-LINKING.md`.
5. **Global from launch**, not US-only. These clusters are fragmented by geography and
   almost everyone optimises for US English.

## Research tooling

```
python research/serp.py            # list all 34 seeds
python research/serp.py 5          # open seed 5's synonyms as US-geo SERPs, incognito
python research/gen_links.py       # regenerate synonym-groups.md
```
