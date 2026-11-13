# Microtools portfolio

19 single-purpose tool websites, **one built per month**, monetised with display ads.
Each site owns one keyword cluster; 34 validated tools are distributed across the 19 sites.

## Layout

```
research/          strategy, evidence, generators
websites/NN-slug/  one folder per site — open this folder to build that site
_archive/          superseded research from an earlier track. Safe to delete.
```

## ⚠ Two repos — commit every change to the right one

This folder is shared with the team through **two** GitHub repos:

| What changed | Repo | Notes |
|---|---|---|
| Anything in this folder **outside** a built site — `CLAUDE.md`, `SKILLS.md`, `research/`, a site's briefs before it has its own repo | **`MorningstarDeep/Website-ideas`** (this repo, public, team-shared) | commit + push here |
| A built site's code — e.g. `websites/01-mouse-tester/` | **that site's own private repo** (`MorningstarDeep/mousetesteronline`) | Cloudflare Pages deploys from its `main`. Live site → branch → preview → merge |

A built site sits here as a **git submodule** (see `.gitmodules`). After pushing site
changes, update the pointer in this repo too: `git add websites/<slug>` → commit → push.
Teammates: `git clone --recurse-submodules`, or `git submodule update --init` (needs
collaborator access to the private site repo).

When a new site gets its own deploy repo, register it here as a submodule — from this root:
`git rm -r --cached websites/<folder>` then
`git submodule add https://github.com/MorningstarDeep/<repo>.git websites/<folder>`.

### "Done for the day"

When the operator says **"done for the day"**, push the day's work to **both** repos:

1. Site work that is **finished, gates green and checked on the Cloudflare branch preview** →
   merge to the deploy repo's `main` and push. **`main` is live on the internet the moment it
   is pushed — never put unfinished or unverified work there.**
2. **Unfinished** site work → commit on its feature branch and push **the branch only** (its
   preview is noindexed). Note in that site's `PROGRESS.md` which branch holds what.
3. This repo: commit + push every portfolio-file change, and move each site's submodule
   pointer — **only ever to a commit that is on the deploy repo's `main`**.
4. `PROGRESS.md` gets its session-log line and next task in the same push.

`SKILLS.md` lists the Claude skills, plugins and MCPs to use when building a site.

## Read these first

| File | What it is |
|---|---|
| `research/05-SITE-PLAN.md` | The 19 sites, build order, why that order |
| `research/04-TOOL-VALIDATION.md` | Per-seed evidence for all 34 tools — traffic, $/visit, geo, incumbents |
| `research/synonym-groups.md` | Keyword clusters with pre-built US-geo SERP links |
| `research/06-CROSS-LINKING.md` | Whether/how the 19 sites may link to each other |
| `websites/NN-slug/CLAUDE.md` | Per-site context, loaded automatically when that folder is open |

## Site briefs are edited by hand

`websites/*/BRIEF.md`, `SEO-BRIEF.md`, `CLAUDE.md` and `.vscode/` were created **once** by
`research/make_sites.py` (one-time setup). **Do not re-run it** — it rewrites every site
folder and would wipe the edits made since, including the live sites' hand-maintained files.
To change a rule for every site, edit each site's file directly (and this file).
`research/gen_links.py` still regenerates `research/synonym-groups.md` on its own.

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
