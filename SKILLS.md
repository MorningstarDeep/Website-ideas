# Claude skills, plugins and MCPs for building these sites

What is installed in the operator's Claude Code setup (checked 2026-11-13) and what each is
for. ⭐ = use on every site. Invoke a skill by name (`/impeccable`, `/seo-audit`, …) or let
Claude pick it up. Trading/finance skills are installed too and left out here.

## Design and frontend

| Skill | Use it for |
|---|---|
| ⭐ `impeccable` | Design, critique, polish, audit and harden UI — hierarchy, type, spacing, colour, motion, UX copy, a11y |
| ⭐ `frontend-design` | Distinctive production UI that does not look AI-generic |
| ⭐ `modern-web-guidance` | Current HTML/CSS/JS practice (dialogs, popovers, container queries, view transitions, INP). **Mandatory before any client JS** (portfolio rule 1) |
| `ui-ux-pro-max` | Palettes, font pairings, UX guidelines, style catalogue |
| `tailwind-4-docs` | Tailwind v4 docs snapshot — **project-scoped, install per site** (see below) |
| `dataviz` | Charts, stat tiles, dashboards |
| `run` | Launch the app and see a change working |

## Performance, accessibility, browser testing

| Skill | Use it for |
|---|---|
| ⭐ `web-perf` | Core Web Vitals work |
| ⭐ `chrome-devtools-mcp:*` | `debug-optimize-lcp`, `a11y-debugging`, `memory-leak-debugging`, `cookie-debugging`, `troubleshooting`, `chrome-devtools`, `chrome-devtools-cli` |
| ⭐ `accesslint:audit` · `scan` · `diff` | Accessibility audits |
| `browse:browser` | Browser automation — screenshots, forms, navigation |
| `anthropic-skills:chrome-browser` · `built-in-browser` · `computer-use` | Drive a real browser or the desktop |

## SEO — `claude-seo` plugin

| Skill | Use it for |
|---|---|
| ⭐ `seo-audit` · `seo-page` · `seo-technical` | Full-site, single-page and technical audits |
| ⭐ `seo-schema` · `seo-sitemap` · `seo-hreflang` | Structured data, sitemaps, multilingual |
| ⭐ `seo-content` · `seo-content-brief` | E-E-A-T, thin content, content briefs |
| ⭐ `seo-geo` | AI search — AI Overviews, ChatGPT, Perplexity citation |
| ⭐ `seo-sxo` | Why a well-optimised page still does not rank (intent vs page type) |
| `seo-cluster` · `seo-plan` · `seo-competitor-pages` | Topic clusters, strategy, comparison pages |
| `seo-drift` | Baseline at launch, catch regressions later |
| `seo-images` · `seo-image-gen` | Image SEO, OG images |
| `seo-google` | GSC / CrUX / GA4 data via APIs |
| `seo-flow` · `seo-programmatic` · `seo-backlinks` | Use with care — portfolio rules forbid link building and page farming |
| `seo-dataforseo` | Live SERP + keyword volume — needs a DataForSEO MCP (not configured) |
| `seo-local` · `seo-maps` · `seo-ecommerce` | Not relevant to tool sites |
| `last30days` | What Reddit, X, YouTube, HN say about a topic right now |
| `youtube-marketing` | YouTube as a traffic / AI-citation channel |

## Coding process — `superpowers` plugin and built-ins

| Skill | Use it for |
|---|---|
| ⭐ `superpowers:brainstorming` | Before building anything new |
| ⭐ `superpowers:systematic-debugging` | Root cause before any fix |
| ⭐ `superpowers:verification-before-completion` | Prove it works before calling it done |
| `superpowers:writing-plans` · `executing-plans` · `subagent-driven-development` | Multi-step work |
| `superpowers:test-driven-development` · `requesting-code-review` · `receiving-code-review` · `finishing-a-development-branch` · `using-git-worktrees` · `dispatching-parallel-agents` | Development workflow |
| ⭐ `code-review` · `simplify` · `security-review` | Review a diff for bugs, cleanups, security |
| `claude-mem:*` | `make-plan`, `do`, `smart-explore`, `learn-codebase`, `mem-search` — memory across sessions |
| `workflow-authoring` | Multi-agent workflows (only on request) |

## Cloudflare (hosting)

| Skill | Use it for |
|---|---|
| ⭐ `cloudflare` · ⭐ `wrangler` | Pages, Workers, DNS, rules — mandatory for Cloudflare work (portfolio rule 1) |
| `workers-best-practices` · `durable-objects` · `agents-sdk` · `sandbox-sdk` | Only if a site truly needs server code |
| `cloudflare-email-service` | Email Routing / sending, SPF / DKIM / DMARC |
| `turnstile-spin` | Bot protection for forms |

## Documentation MCPs — never write library code from memory

| MCP / skill | Notes |
|---|---|
| ⭐ `context7` | Docs for any npm library. Needs a one-time sign-in: `/mcp` in an interactive session |
| ⭐ `astro-docs` MCP | Astro docs — **project-scoped**, add per site (below) |
| `tailwind-4-docs` | as above |
| `claude-api` | Anthropic API |

## Behaviour and optimisation

| Skill | Use it for |
|---|---|
| ⭐ `ponytail` (+ `-audit` `-review` `-debt` `-gain` `-help`) | Laziest working solution, no over-engineering — on by default |
| `caveman` | Ultra-short replies, saves tokens |
| `the-fool` | Devil's advocate, pre-mortem, red-team a plan |
| `remember:remember` | Save session state for the next session |
| `self-improving-agent` | Promote memory notes into CLAUDE.md rules |
| `fewer-permission-prompts` · `update-config` · `claude-code-setup:claude-automation-recommender` | Tune Claude Code itself |

## Documents and research

`anthropic-skills:deep-research` · `docx` · `pdf` · `pptx` · `xlsx` · `docs` · `skill-creator`

## Per-site setup (project scope — never in this parent folder)

Run inside `websites/NN-slug/` after `git init` + the Astro scaffold:

```
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
npx skills add https://github.com/lombiq/tailwind-agent-skills --skill tailwind-4-docs
npx getdesign@latest add <design>      # a different design language per site
```

## Known connection issues (2026-11-13)

`context7` needs sign-in. The `accesslint`, `chrome-devtools` and `youtube` MCPs timed out on
one session start — the skills are installed; restarting Claude Code usually reconnects them.
