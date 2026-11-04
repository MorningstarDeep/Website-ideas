"""Generate ../websites/NN-slug/BRIEF.md for all 19 sites.

  python make_sites.py

The brief body is IDENTICAL across all 19 by design — end goal, stack, SEO approach and
workflow are portfolio-wide decisions, not per-site ones. Only the small facts header
differs, and it is generated from data already in the research (no per-site planning).

Re-runnable: rewrites BRIEF.md, never touches anything else in a site folder.
"""
import os, sys
from gen_links import GROUPS, SERP
import urllib.parse

SYN = {name: syns for _, seeds in GROUPS for name, syns in seeds}

# (order, slug, display, primary seed, absorbed seeds, RPM, pool, incumbents)
SITES = [
    (1, "mouse-tester", "Mouse Tester", "Mouse Tester", [],
     "$9.83", "144K",
     "onlinemictest.com/mouse-test 76.5K · redragonshop.com 49K (0→45K in 2mo) · "
     "codepen.io/blink172 13.9K — **a CodePen pen holds #1 for `double click test`** · "
     "cpstest.org 13.6K · **mouseaccuracy.com 10.3K, $0.505/visit, 56% tier-1** (gaming/aim "
     "angle) · **atk.store 8.6K, $0.038/visit, ~9% tier-1 — ranks #4-8, soft target**"),
    (2, "webcam-test", "Webcam Test", "Webcam Test", [],
     "$4.41", "511.8K",
     "webcamtests.com 511.8K — holds the cluster, 40% tier-1 geo"),
    (3, "favicon-generator", "Favicon Generator", "Favicon Generator", [],
     "$6.48", "212K",
     "favicon.io 118.9K · realfavicongenerator.net 93K (+67% in 5mo) — **fragmented, neither owns it**"),
    (4, "image-color-picker", "Image Colour Picker", "Image Color Picker",
     ["Color Palette Generator", "Color Palette From Image", "Hex to RGB Converter",
      "Image Color Changer"],
     "$10.56", "1.7M",
     "imagecolorpicker.com 753.6K · coolors.co 975.2K · **Figma ranks #2** · "
     "photoaid.com took `eyedropper online` off the leader"),
    (5, "redirect-checker", "Redirect Checker", "Redirect Checker", ["HTTP Status Checker"],
     "$16.62", "52K",
     "wheregoes.com 22.2K ($1.108/visit, highest measured) · redirect-checker.org 29.8K · "
     "httpstatus.io 9.5K — **fragmented, no giant, no brand moat**"),
    (6, "url-encoder-decoder", "URL Encoder / Decoder", "URL Encoder / Decoder", [],
     "$16.43", "68.5K",
     "meyerweb.com/eric/tools/dencoder 68.5K — **a 2005 personal-blog page**, growing · urlencoder.org 10.2K"),
    (7, "website-legit-checker", "Website Legit Checker", "Website Legitimacy Checker", [],
     "$15.00", "141K",
     "urlvoid.com 81K · scamwise.com 60K (**0→60K in 2 months**) · ssltrust.com 8.6K (100% US) · "
     "**Google Safe Browsing ranks #1** for `website checker`"),
    (8, "website-down-checker", "Website Down Checker", "Website Down Checker", [],
     "$12.30", "161.3K",
     "isitdownrightnow.com 161.3K — holds all 5 synonyms but **declining 220K→165K (−25%)**, brand moat only 3.6K"),
    (9, "svg-tools", "SVG Tools", "SVG Viewer", ["SVG Optimizer", "SVG to PNG"],
     "$7.61", "256K",
     "svgviewer.dev 54.6K · svgtopng.com 201.5K (EMD, declining 23%) · svgomg.net 9.7K"),
    (10, "refresh-rate-test", "Refresh Rate Test", "Refresh Rate Test", [],
     "$3.65", "117.6K",
     "testufo.com 117.6K + /refreshrate 31.7K — one site, two pages, no brand moat. "
     "**9 exact-match domains rank below it**"),
    (11, "youtube-tools", "YouTube Tools", "YouTube Transcript",
     ["YouTube Thumbnail Downloader", "YouTube Thumbnail Tester", "YouTube Tag Generator"],
     "$2.82", "495.1K",
     "youtubetotranscript.com 495.1K (growing) · youtube-transcript.io 194.1K (growing) · "
     "thumbnail side: youtube-thumbnail-grabber.com 481.5K. **17% tier-1 geo — thin per visit**"),
    (12, "microphone-test", "Microphone Test", "Microphone Test", [],
     "$2.02", "703.3K",
     "mictests.com 703.3K — **all 5 synonyms at #1 in the US**. onlinemictest.com bundles mic "
     "but loses to it"),
    (13, "merge-images", "Merge Images", "Merge Images", [],
     "$2.25", "204.3K",
     "pinetools.com/merge-images 204.3K — all 5 at #1, but **India 76% / US 10%**"),
    (14, "audio-test", "Audio Test", "Speaker Test", ["Headphone Test", "Surround Sound Test"],
     "$2.22", "135K",
     "onlinemictest.com/sound-test 88.8K · audiocheck.net 46.3K (one page ranks for 3 synonyms) · "
     "soundtest.io 2.9K (**0→2.9K in ~1 month, took #1 from xbitlabs**). "
     "3 of 5 synonyms are **video-topped SERPs**"),
    (15, "screen-test", "Screen Test", "Dead Pixel Test", ["Monitor Test", "Touchscreen Test"],
     "$1.77", "128K",
     "displaytech.org 100.6K (**30K→100.6K in 4 months**) · eizo.be 27.2K (a monitor "
     "brand's marketing page) · touch: onlinemictest.com/touch-screen-test 30.1K · "
     "**screendetect.com** — a *screen*-branded site that won `ghost touch test`"),
    (16, "pdf-page-tools", "PDF Page Tools", "Split PDF", ["Extract Pages From PDF"],
     "$1.56", "1.8M",
     "ilovepdf.com/split_pdf 1.8M (**8.7M/mo brand search**) · smallpdf.com 57.4K · Adobe. "
     "**Suite-locked, 4% tier-1. Scrap play: 1% of the cluster ≈ 5.6K visits**"),
    (17, "gamepad-tester", "Gamepad Tester", "Gamepad Tester", [],
     "$1.32", "441.7K",
     "hardwaretester.com/gamepad 441.7K — all 5 at #1. **3 exact-match domains rank below it**"),
    (18, "keyboard-tester", "Keyboard Tester", "Keyboard Tester", [],
     "$0.88", "574.3K",
     "keyboardtester.com 574.3K (4 of 5 synonyms) · keyboardchecker.com 117.9K "
     "(**the EMD beat a 5x larger site on `keyboard checker`**) · key-test.ru owns SEA, absent from US"),
    (19, "font-identifier", "Font Identifier", "Font Identifier", [],
     "$1.98", "2.3M",
     "myfonts.com/whatthefont 2.3M (**+117% in 4 months, 144K brand search**) · "
     "fontsquirrel.com 267K (−33%). **Needs a real ML model — hardest build in the portfolio**"),
    (20, "pomodoro-timer", "Pomodoro Timer", "Pomodoro Timer",
     ["Aesthetic Timer", "Visual Timer", "Duration Timer"],
     "$1.70", "119.1K",
     "**pomodorotimer.online 119.1K, $13.4K value, $0.113/visit** — US 29 · Spain 19 · "
     "Brazil 12 · India 7. **~50K flat Apr-Jun then 119K by Aug: more than doubled in two "
     "months.** Ranks #10 `timer` (2.9M) · **#4 `pomodoro timer` (74K)** · #9 `pomodoro` "
     "(107K) · #7 `study timer` (5.1K) · #11 `25 minute timer` (50K) — **#1 on nothing, "
     "yet 119.1K. The widget does NOT eat all the clicks.** Also: stagetimer.io #1 for "
     "`30 minute timer` via `/go/30-minutes/` · tiimoapp.com (visual/ADHD, an app not a "
     "web tool — **the gap**) · vclock.com · stopwatchtimers.com · 4 of top-10 are YouTube"),
    (21, "stage-timer", "Stage Timer", "Stage Timer", [],
     "TBD", "TBD",
     "Split out from site 20 — event/AV professionals are a different audience and a "
     "different product (remote control, multi-display, speaker cues). **Widget-proof and "
     "higher commercial intent.** stagetimer.io (Slush, YC Startup School, Munich Security "
     "Conference) · presentationtimer.org · timedflow.com · eventtimer.io · letstimeit.com"),
]


# How hard it is for Google to replace the tool with its own SERP widget.
# Derived from seed 16: `hex to rgb` died because Google renders a colour picker inline.
RISK = {
    "mouse-tester": ("HARDWARE", "Needs the visitor's own mouse. Google cannot render this."),
    "webcam-test": ("HARDWARE", "Needs camera permission on the visitor's device."),
    "microphone-test": ("HARDWARE", "Needs mic permission on the visitor's device."),
    "audio-test": ("HARDWARE", "Needs the visitor's speakers/headphones."),
    "screen-test": ("HARDWARE", "Needs the visitor's own panel and touch digitiser."),
    "refresh-rate-test": ("HARDWARE", "Needs the visitor's display timing."),
    "gamepad-tester": ("HARDWARE", "Needs a connected controller."),
    "keyboard-tester": ("HARDWARE", "Needs the visitor's physical keys."),
    "image-color-picker": ("USER FILE", "Needs the visitor's own image."),
    "svg-tools": ("USER FILE", "Needs the visitor's own SVG."),
    "favicon-generator": ("USER FILE", "Needs the visitor's own logo, returns a file bundle."),
    "merge-images": ("USER FILE", "Needs multiple images from the visitor."),
    "pdf-page-tools": ("USER FILE", "Needs the visitor's own PDF."),
    "font-identifier": ("USER FILE", "Needs the visitor's own image."),
    "redirect-checker": ("LIVE FETCH", "Google COULD widget this. Defend with depth: chains, bulk, CSV, headers."),
    "website-down-checker": ("LIVE FETCH", "Google COULD widget this. Defend with history, multi-region checks."),
    "website-legit-checker": ("LIVE FETCH", "Google already ranks its own Safe Browsing #1. Defend with explanation, not verdicts."),
    "url-encoder-decoder": ("STRING", "HIGHEST replacement risk - pure computation, like hex-to-rgb. Defend with batch, presets, code snippets, explain-what-changed."),
    "pomodoro-timer": ("WIDGET-CONTESTED", "Google shows its own timer widget above every "
                       "duration query and YouTube holds ~4 of the top 10 - BUT "
                       "pomodorotimer.online proves real clicks survive below it (119.1K "
                       "while ranking #4-#11, #1 on nothing). Volume play, not a value play: "
                       "$0.113/visit."),
    "stage-timer": ("WIDGET-PROOF", "Google cannot do remote control, multi-display or "
                    "speaker cues. Real commercial audience, no widget. 5 real competitors."),
    "youtube-tools": ("API", "Depends on YouTube data. Defend with formats, search, timestamps, export."),
}

# BUILD ORDER drives the folder numbers: websites/NN-slug where NN = build position.
# The SLUG is the permanent identity - GitHub repo and Cloudflare project are named after
# the slug ONLY, never the number, so reordering never touches anything deployed.
# Reorder this list and re-run make_sites.py; it renames nothing, so rename folders to match.
BUILD_ORDER = [
    1,   # Mouse Tester        - softest target found (a CodePen pen at #1), $9.83 RPM
    2,   # Webcam Test         - simple build, 511.8K pool, $0.294/visit, 40% tier-1
    20,  # Pomodoro Timer      - niche consolidating NOW (incumbent 50K->119K in 2 months)
    3,   # Favicon Generator   - fragmented, neither incumbent owns it
    4,   # Image Colour Picker - absorbs 4 tools, 1.7M pool
    5,   # Redirect Checker    - highest RPM measured
    6,   # URL Encoder         - incumbent is a 2005 blog page
    7,   # Website Legit       - biggest URL cluster
    8,   # Website Down        - incumbent declining 25%
    9,   # SVG Tools
    21,  # Stage Timer         - widget-proof, commercial; after 20 proves the timer engine
    10,  # Refresh Rate Test
    11,  # YouTube Tools
    12,  # Microphone Test
    13,  # Merge Images
    14,  # Audio Test
    15,  # Screen Test
    16,  # PDF Page Tools
    17,  # Gamepad Tester
    18,  # Keyboard Tester
    19,  # Font Identifier     - needs an ML model, hardest build
]

# Per-site notes rendered into BRIEF.md. Only where a site needs something the shared
# body cannot say. Keep short - detailed planning happens inside the site folder.
NOTES = {
    "pomodoro-timer": """
**Themes are a setting, not pages.** One timer page with a theme switcher (cityscapes,
nature, earth, space). Do NOT create a page per theme - pages differing only by background
image are near-duplicates and land in "Crawled - currently not indexed".

### How many pages is safe - the actual rule

The risk is **doorway pages**: pages created mainly to capture query variants that all funnel
to the same destination. Google enforces this. The test is not page count, it is whether each
page **independently earns its listing**.

| Earns a page | Does not |
|---|---|
| Distinct intent, distinct answer | Same answer, different wording |
| Content that could not sit on another page | A template with a number swapped |
| Someone landing there is fully served | Landing there, you still need the main page |

**Duration pages are the live question here.** `stagetimer.io` runs `/go/30-minutes/` and
ranks #1, so the pattern is tolerated - but only when the page genuinely serves the query:
timer pre-set and running on load, plus content specific to *that* duration (what 30 minutes
suits, why that interval, its own FAQ). A page that is the 25-minute page with "25" replaced
by "45" is a doorway page.

**Modifier variants never get their own page.** `set a 30 minute timer`, `30 minute timer
google` and `30 minute timer` are one intent - one page, variants appear naturally in copy.

### Decide it empirically, do not guess

1. Launch a **small set**: home + 3-4 highest-volume durations + 2-3 genuine guides
   (flow state, the pomodoro method, focus science) + the 4 AdSense pages.
2. Watch **GSC Pages** for 3-4 weeks. If they index and hold, the pattern is accepted.
3. **Expand only then**, a few at a time.
4. **Stop signal:** new pages landing in "Crawled - currently not indexed". That is Google
   saying these add nothing - adding more will not fix it, and volume of thin pages is what
   turns a tolerated pattern into a site-wide quality problem.

This also solves AdSense: guides plus real duration pages reach the ~15-20 substantive pages
reviewers expect (section 19), without padding.
""",
}

# Cross-links AUTHORISED by the operator, per site. Default: none.
# Policy: zero by default; only on the operator's explicit instruction; earliest 4-5 months
# after the receiving site launched; one at a time with ~3 months between; same audience
# cluster only. Adding an entry here is what authorises it - a site session must never
# invent one.
#   slug: [(target_url, placement, anchor_text, why)]
CROSSLINKS = {}

# Confirmed AVAILABLE in the RDAP sweep 2026-08-22. Re-verify before buying.
DOMAINS = {
    "redirect-checker": ["httpstatuschecker.com"],
    "url-encoder-decoder": ["urlencoderdecoder.com"],
    "image-color-picker": ["screenshotcolorpicker.com", "imagecolorpicker.io"],
    "svg-tools": ["viewsvg.com", "svginspector.com"],
    "youtube-tools": ["transcriptyoutube.com"],
    "pdf-page-tools": ["pdfpageextractor.com"],
    "font-identifier": ["fontidentifierfromimage.com", "fontfinderfromimage.com"],
}

PROGRESS_MD = """<!-- NOT generated. This file is yours to edit. make_sites.py never overwrites it. -->

# {display} — progress

**Status:** not started
**Last session:** —
**Next task:** Step 0 — pick target competitor + domain

## Decisions (fill these in, they are referenced by every later session)

| Decision | Value |
|---|---|
| Target competitor | |
| Why beatable | |
| Domain (qualified EMD) | |
| Domain bought? | no |
| Design language | vercel (default) |
| Locales shipped | en |
| **GitHub account** (operator has 3 — confirm!) | |
| GitHub repo (must be **private**) | |
| **LIVE? (custom domain connected)** | **no** — while `no`, commit straight to `main`. Once `yes`, branch-preview-merge is mandatory |
| Launch date | |
| Cloudflare Pages URL | |

## Phases

- [ ] **Step 0** — competitor chosen + weaknesses documented, domain decided
- [ ] **Setup** — git init, GitHub repo, Astro scaffold, Cloudflare Pages live, noindex headers
- [ ] **Skills** — astro-docs MCP, tailwind-4-docs, getdesign vercel installed in this folder
- [ ] **Core tool** — working, client-side, above the fold
- [ ] **PAA research** — 15-25 questions recorded verbatim in docs/paa-research.md
- [ ] **Pages** — one per distinct intent, internally linked
- [ ] **Content** — 800-1200 words per tool page
- [ ] **FAQ + JSON-LD** — 10-15 PAA-sourced questions
- [ ] **Required pages** — about, contact, privacy, terms, 404, 500
- [ ] **Assets** — logo, favicon set, OG images
- [ ] **Technical** — sitemap, robots (incl. AI bots), canonicals, schema
- [ ] **i18n** — locales added, hreflang reciprocal
- [ ] **Performance** — CrUX targets met, Lighthouse 100 mobile
- [ ] **Accessibility** — accesslint clean
- [ ] **Pre-launch gate** — every box in SEO-BRIEF section 12
- [ ] **Launch** — domain connected, noindex removed, GSC + Bing verified
- [ ] **Post-launch** — AEO baseline recorded, GSC annotation added

## Session log

<!-- one line per session: date - what changed - what is next -->
"""

from seo_brief_body import SEO_BODY

BODY = """
## ⚠ IRON RULES — read before writing any code

### 1. Never write library code from memory. Always fetch current docs first.

Model training data goes stale and frameworks ship breaking changes across majors. Astro's
config shape, integration names, i18n routing API and adapter setup have **all** changed
between versions. Tailwind v4 dropped the JS config entirely. Guessing produces code that
looks right and fails.

**Before touching any library, framework, SDK, CLI or cloud service:**

```
context7: resolve-library-id  ->  query-docs
```

Use it for **Astro, Tailwind, Cloudflare Pages/Workers, Wrangler, every npm package** — even
ones that feel familiar. Prefer it over web search for library documentation.

| Domain | Fetch from |
|---|---|
| **Tailwind CSS v4** | **`tailwind-4-docs` skill** — installed per-project in setup below |
| Astro, and any other npm package | **context7 MCP** |
| Cloudflare Pages / Workers / KV / R2 | `cloudflare` skill, `wrangler` skill — both retrieval-first |
| Web platform APIs (Canvas, WebRTC, File, Gamepad, Pointer) | `modern-web-guidance` skill — **mandatory before client JS** |
| Visual design language | **`DESIGN.md`** in this folder — installed per-project in setup below |
| Anything Claude/Anthropic API related | `claude-api` skill |

**If documentation and memory disagree, documentation wins.** No exceptions.

**Latest applies to everything**, not just Astro — Tailwind (v4 dropped the JS config
entirely), any CSS or JS library, and the HTML/CSS platform features themselves. Check
current baseline support before using a modern CSS feature; do not assume the polyfill
advice you remember still applies.

### 2. Latest stable, never bleeding edge.

- Start every site from the **current stable major**, not whatever was current when a blog
  post was written.
- **Never** ship an alpha, beta, RC or nightly to production.
- Check the actual installed version (`npm ls astro`) before using an API — not the latest
  release notes.
- Pin exact versions in `package.json`. Reproducible beats convenient.
- Read the migration guide before bumping a major, mid-portfolio.

### 3. "Best" means fewest moving parts that does the job.

Latest and best are not the same as most. The winning sites in this research are plain,
fast pages. Prefer a platform feature over a library, a library over a framework, and ten
lines over a dependency. `ponytail` is active — every dependency added is a thing that can
break at 3am across 19 sites.

### 4. Repos are ALWAYS private. No exceptions, ever.

`gh repo create <slug> --private`. Never public, never flipped to public later. Cloudflare
Pages builds from private repos without any issue.

Verify after creating, and again before launch:

```
gh repo view --json visibility        # must be PRIVATE
```

### 5. Once live: never commit directly to `main`. Branch, preview, then merge.

**This rule activates when the site goes live** — custom domain connected and submitted to
GSC. Before that point there is no production to protect: `pages.dev` is noindexed, nobody is
looking, and branching every change is pure overhead. **During the initial build, commit
straight to `main` and move fast.**

**After launch it is mandatory and has no exceptions.** The repo is wired to Cloudflare Pages,
so every push to `main` deploys to production worldwide, instantly. There is no staging step
and no undo faster than revert-and-redeploy.

From launch onward, every change — new feature, content edit, new locale, bug fix, dependency
bump — happens on a branch:

```
git switch -c feat/mouse-button-test     # one branch per task
# ... commit per finished step ...
git push -u origin feat/mouse-button-test
```

Cloudflare automatically builds a **preview deployment** for every non-production branch, at
its own URL. **Verify there.** Preview deployments are auto-noindexed by Cloudflare, and the
`_headers` rule covers them too, so nothing leaks into search.

Only when the task is complete and verified on the preview URL:

```
git switch main
git merge feat/mouse-button-test
git push                                  # this is the moment it goes live
git branch -d feat/mouse-button-test
```

**Rules (post-launch):**

- **One branch per task**, matching the one-task-per-session rule.
- Branch names mirror the commit prefixes: `feat/` `seo/` `content/` `i18n/` `perf/` `fix/`.
- **`main` is always production and always deployable.** Never leave it broken, never use it
  as a scratch pad.
- Merging to `main` is a deliberate act — the equivalent of pressing publish.
- Delete the branch after merge so the list stays readable across 19 months.
- **Record in `PROGRESS.md` when the site goes live** — that is the moment this rule
  switches on, and a cold session needs to know which side of it you are on.


---

## How this project is worked — short, cold sessions

**The operator opens a new chat or runs `/clear` for every task, to save tokens.**
Assume **nothing carries over between sessions.** Design the work around that:

### Rules

1. **`PROGRESS.md` is the memory.** Read it at the start of every session, before anything
   else. It holds the target competitor, the domain, locales shipped, phase status, and what
   comes next.
2. **Write decisions down the moment they are made** — not at the end. A domain choice,
   a competitor weakness, a locale decision that exists only in the chat is gone when the
   session closes.
3. **Update `PROGRESS.md` before the session ends.** Status, one session-log line, and the
   next task. If a session is interrupted, the log line is what saves the next one.
4. **One task per session.** "Build the tool" and "write the content" are separate sessions.
   Scope creep costs tokens and produces half-finished work in two places.
5. **Read only what the task needs** — see the reading map in `CLAUDE.md`. `SEO-BRIEF.md` is
   ~640 lines; loading it whole for a CSS tweak wastes a third of the budget.
6. **Commit after every finished step** — see Git discipline below. Never end a session
   with uncommitted work.

### What NOT to do

- Do not re-read all three briefs at the start of every session.
- Do not re-derive decisions already recorded in `PROGRESS.md` — trust them.
- Do not leave work in a broken state; the next session has no context for a half-refactor.

### Git discipline — commit per step, not per session

**Commit every time a step or feature is finished and working.** Not at the end of the
session, not in one big lump.

Why it matters here specifically:

- **Granular revert.** If a change tanks Core Web Vitals or breaks the tool on mobile, you
  revert *that* commit — not a day's work.
- **The log is memory.** A cold session reads `git log --oneline` and knows what actually
  happened, independently of `PROGRESS.md`.
- **Each push redeploys the branch preview.** Cloudflare builds a preview deployment for
  every non-production branch, so each commit is immediately checkable on that branch's own
  URL — which is where testing happens, not localhost. **Merging to `main` is what goes
  live** (Iron Rule 4).

**Rules:**

1. One logical change per commit. "Add scroll test" and "fix CLS" are two commits.
2. **Never commit a broken state.** The tool must work at every commit.
3. Push after each commit **to the branch**. Verify on the branch preview URL before
   moving on. Never push to `main` directly.
4. Short, scannable messages with a prefix so history reads at a glance:

```
feat:    mouse button + scroll test working
seo:     unique title, meta, OG on all pages
content: FAQ from PAA research (14 questions)
i18n:    add pt-BR locale + hreflang
perf:    reserve tool height, CLS 0.08 -> 0
fix:     double-click detection on Firefox
chore:   deploy script, .gitignore
```

5. `.gitignore` from the start: `node_modules/`, `dist/`, `.astro/`, `.env*`,
   `.wrangler/`, `.DS_Store`.
6. Commit `PROGRESS.md` updates with the work they describe, not separately.

---

## Step 0 — decide the domain and the target competitor FIRST

Nothing gets built until both are written down. Every downstream decision — page structure,
what "better" means, the creation prompt itself — references them.

### 1. Pick ONE target competitor

From the incumbents listed in "What this site is" above. **Pick the one you can realistically
displace, not automatically the #1.** A declining incumbent, a fragmented cluster, or a
CodePen page is a better target than the market leader.

Then study their page properly and write down:

- What they do well (do not regress on it)
- What they are missing — features, depth, mobile, speed, explanation
- Which of their keywords are weakest (position 5–15, where they are beatable)
- Their page structure and word count

**This URL goes straight into the build prompt.**

### 2. Decide the domain

**Qualified EMD** — full query phrase plus one qualifier, per the compilefuture pattern
(`realonlineruler.com`, `fontfinderai.com`). Clean exact-match `.com` is gone for nearly
every primary in this portfolio.

Check availability at **instantdomainsearch.com**. Candidates confirmed free as of
2026-08-22 are listed in **Domain candidates** in the facts section at the top of this file — **re-verify, they move.**

**Do not buy it yet.** The domain is purchased at launch, not at kickoff — the site is built
and verified on the free `pages.dev` URL first.

Registrars: Namecheap · Spaceship · BigRock · GoDaddy · Hostinger · Cloudflare.

---

## Reference implementation — read this before building

**<https://compilefuture.com/blog/making-50-lpa-from-my-own-ai-business/>**

The operator this portfolio's strategy is modelled on, documenting their exact build process.
**Read and analyse it in full at the start of every site**, then use the prompts and checklist
below — improvising or improving where this brief's requirements are stricter.

Much of it independently matches decisions already made here: AstroJS, Tailwind v4,
Cloudflare Pages, `DESIGN.md`, the `_headers` noindex trick, realfavicongenerator, Ahrefs
Keyword Generator, and the about/privacy/terms/contact page set.

### Their prompts — use these, adapted

**Build:**

> "I have initialized a new astrojs project, use astro docs mcp and tailwind-4-docs skill for
> creating the website."

...plus the target competitor URL from Step 0.

**On-page SEO:**

> "Do the On Page SEO of this Website for Main Keyword: `<primary keyword>`"

...with the supporting keywords from the cluster in "What this site is". Target
**800–1200 words** of on-page content about the tool.

**FAQ:**

> "add seo friendly FAQ section for these below questions"

...followed by ~13 real questions, with **"Use JSON-LD for FAQ SEO"**.

### Their checklist — additions this brief did not already cover

- **logofa.st** for logo and favicon, then run it through **realfavicongenerator**
- **500 error page** as well as 404
- **800–1200 words** of on-page content — a concrete target, not "some content"
- **Cloudflare mail routing** to Gmail, so `/contact/` has a real working address
- **Deploy script in `package.json`**
- Disable indexing on **`workers.dev`** too, not only `pages.dev`, if Workers are used

### Where this brief deliberately goes further

| Topic | compilefuture | Here |
|---|---|---|
| Analytics | Google Analytics | **Same — GA4.** An earlier draft here recommended Cloudflare Web Analytics to avoid a consent banner; that was wrong, because AdSense requires a CMP for EEA/UK traffic anyway. Revenue-per-page attribution decides it |
| Internationalisation | not covered | **Multilingual from launch** — the main differentiator, see SEO-BRIEF §14 |
| Core Web Vitals | not specified | **LCP < 1.2s · INP < 100ms · CLS 0**, field data |
| Competitor choice | "give competitor URL" | Pick the *beatable* one, with a documented weakness analysis |

---

## Workflow — live from day one, domain last

Build on a free Cloudflare URL from the first commit so every change is checkable on a real
live site. Buy the domain and touch Google only when the site is **finished**.

### Day 1 — before writing a single component

> **Name the repo and the Cloudflare project after the slug only, never the folder
> number.** The number is the build position and can change if the plan is reordered;
> the slug never does. Folder `03-pomodoro-timer` -> repo `pomodoro-timer`.

**One-time, machine-wide (already done, verify only):** GitHub CLI installed and
authenticated. `gh auth status` should show a logged-in host; if not, run `gh auth login`
(interactive, opens a browser — the operator must do this, an agent cannot).

#### ⚠ STOP — confirm the GitHub account before creating anything

**The operator has three GitHub accounts.** Creating the repo under the wrong one is
expensive to undo: the repo must be deleted or transferred, the git remote rewritten, and the
Cloudflare Pages connection rebuilt from scratch.

```
gh auth status                     # lists every logged-in account
gh auth switch --user <username>   # if the active one is wrong
```

**Then ask the operator to confirm, out loud, which account this site belongs to** — do not
infer it from the last site, they may differ. Record it in `PROGRESS.md` before running
`gh repo create`.

After creating, verify it landed correctly:

```
gh repo view --json owner,name,visibility    # visibility MUST be "PRIVATE"
```

Cloudflare Pages connects to a specific GitHub account or org, so **it must match the one
that owns this repo.**

```
git init
# .gitignore: node_modules, dist, .astro, .env, .wrangler
gh repo create <slug-without-number> --private --source=. --remote=origin   # ALWAYS --private
# e.g. folder 03-pomodoro-timer  ->  repo `pomodoro-timer`
# scaffold Astro, first commit
git push -u origin main
```

Then in the Cloudflare dashboard: **Workers & Pages → connect to Git → select the repo.**
Every push to `main` auto-deploys in ~30 seconds to a free
`https://<project>.pages.dev`.

No domain. No DNS. No cost. Nothing submitted to Google.

*(Verify current Cloudflare free-tier limits and Pages setup with the `cloudflare` and
`wrangler` skills — per Iron Rule 1, do not trust remembered numbers.)*

### Day 1 — project-scoped skills and design system

Run these **inside this site folder**, and **only after `git init` + the Astro scaffold
exist**. Both are project-scope on purpose — each site gets its own copy so they can diverge.

```
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
npx skills add https://github.com/lombiq/tailwind-agent-skills --skill tailwind-4-docs
npx getdesign@latest add vercel
```

**All three are per-site, project scope. Never install them in the parent `microtools/`
folder** — that folder is strategy and portfolio management only. Each site owns its own
copy so they can diverge and so nothing leaks between builds.

**⚠ `getdesign` walks *up* the directory tree looking for a project root.** With no
`package.json` or `.git` present it writes `DESIGN.md` several levels above where you are —
verified, it escaped 8 directories in testing. **Scaffold first, then run it**, and confirm
`DESIGN.md` landed in this folder before continuing.

### DESIGN.md is the design authority

`npx getdesign@latest add vercel` writes a ~740-line `DESIGN.md` containing a full design
language: colour tokens, typography scale, spacing, surfaces, motion, component patterns.

**Read `DESIGN.md` before writing any UI.**

**Pick a distinct design language for each site.** Vercel is the suggested starting point —
clean, developer-facing, high-contrast, fast, and it suits tool sites — but **do not ship the
same one across the portfolio.** Each site is its own project and should look like it.

Check `PROGRESS.md` in the other site folders to see which languages are already used, and
choose a different one.

**Swapping it:** if a particular site genuinely needs a different look, browse
**[getdesign.md](https://getdesign.md)** — it catalogues design languages (Vercel, Apple,
Claude, and others) — then install that one instead:

```
npx getdesign@latest add <name>
```

One design per site, chosen deliberately, never mixed. Do not hand-roll a design language
when a curated one exists.

**Pick whatever suits this tool.** Vercel is a good default for developer-facing utilities,
but there is no obligation to match anything — this site is its own project.

Customise `DESIGN.md` as the site evolves; it is a project file, not a locked dependency.

### ⚠ PERMANENTLY noindex pages.dev / workers.dev — never remove it

Cloudflare noindexes *preview* deployments automatically, but the **production
`<project>.pages.dev` URL is indexable by default.** Two separate problems:

1. **During build** - Google indexes a half-finished site.
2. **Forever after** - once the custom domain is live, `project.pages.dev` still resolves and
   serves **byte-identical content**. That is duplicate content, permanently, splitting
   signals between two hostnames.

**So this rule is permanent. It is never deleted.**

Create `public/_headers` in the very first commit - this is the pattern from Cloudflare's own
docs, using `:project` / `:version` **named placeholders** so nothing is hardcoded:

```
https://:project.pages.dev/*
	X-Robots-Tag: noindex

https://:version.:project.pages.dev/*
	X-Robots-Tag: noindex
```

**Why this single file covers both phases:** the rule is scoped to the `pages.dev` hostname.
Before launch that is the only hostname, so the whole site is noindexed. After the custom
domain is connected, the custom domain is unaffected and indexes normally while `pages.dev`
stays blocked. **Nothing changes at launch - you add the domain, you do not edit this file.**

Indent the header lines with tabs or spaces; both are accepted.

**Also required:**

- **Canonical always points to the custom domain**, on every page, from day one. If anyone
  links to a `pages.dev` URL, the canonical still names the real site.
- **If using Workers instead of Pages:** after adding the custom domain, **turn off the
  `workers.dev` route** in the Worker's settings. There is no `_headers` equivalent - it is a
  dashboard toggle.

*(Verified 2026-08-25 against developers.cloudflare.com/pages/configuration/headers - re-check
per Iron Rule 1.)*

### Build phase

- Every push is live. Check on a real device, real network, real HTTPS — not localhost.
- Small commits, one per feature. The repo is the build record.
- Run Lighthouse and CrUX-style checks against the **live pages.dev URL**, never localhost;
  localhost numbers are meaningless for CWV.
- Test the tool on a real phone via the pages.dev URL. Device APIs (camera, mic, gamepad,
  pointer) behave differently on real hardware and require HTTPS, which pages.dev provides.

### Launch sequence — only when the pre-launch gate fully passes

1. Buy the qualified EMD.
2. Cloudflare Pages → **Custom domains** → add it. DNS is automatic if the domain is on
   Cloudflare.
3. **Do NOT touch `public/_headers`.** The noindex rule is hostname-scoped to `pages.dev`
   and stays forever. Verify both sides:
   ```
   curl -I https://yourdomain.com        # NO X-Robots-Tag  -> indexable
   curl -I https://project.pages.dev     # X-Robots-Tag: noindex -> blocked
   ```
4. Confirm canonical tags point at the custom domain, not pages.dev. Check every page.
5. **Workers only:** turn off the `workers.dev` route in the Worker's settings now that the
   custom domain is live.
6. Verify Google Search Console by **DNS TXT** (survives host changes). Submit `sitemap-index.xml`.
7. Verify Bing Webmaster Tools — free, and it feeds ChatGPT search.
8. Baseline `claude-seo:seo-drift` so future regressions are detectable.

**Do not submit to GSC before the site is complete.** A thin, half-built site being crawled
wastes the first-impression pass and the crawl budget. Launch finished.

---

## End goal

A single-purpose tool site that owns its keyword cluster on **Google US**, monetised with
display ads.

| Target | Value |
|---|---|
| Page 1 on the primary keyword | by month 12 |
| Organic traffic | 10K+/month by month 12 |
| Revenue bar | **₹10,000/month** (~$118) |
| Hold period | 12 months, **checkpoint at month 4** |

One site per month across the portfolio. If this one is flat at month 4 it is unlikely to be
saved by month 12 — every live entrant observed in the research moved inside 2–5 months.

## Each site is its own project — only the process is shared

**These briefs describe a shared *method*, not a shared *product*.** Every site is built as a
separate standalone project. What is shared across the portfolio is the SEO standard, the
workflow and the toolchain. **What must NOT be shared is the site itself.**

| Shared across the portfolio | Different for every site |
|---|---|
| SEO requirements (`SEO-BRIEF.md`) | **Design language** — pick a distinct one per site |
| Workflow, git discipline, gates | **Layout and page structure** |
| Astro / Cloudflare toolchain | **Component design, spacing, type, colour** |
| GSC + AdSense account | **Copy voice and content** — written fresh, never find-and-replaced |
| | **Tool UX** — each solves a different problem, so each looks different |

Two sites should not be recognisable as siblings by looking at them. The only thing legitimately
linking them is the operator's GSC and AdSense account, which is not a violation of anything —
it is the operator's decision alone.

## Tech stack — the default, not a template

| Layer | Choice | Why |
|---|---|---|
| Framework | **Astro**, static output | Ships zero JS by default; islands only where the tool needs it. CWV is a ranking factor and these SERPs are won by fast, simple pages |
| Tool logic | **Vanilla JS/TS** | Almost every tool here is Canvas / WebRTC / File API / fetch. No React unless there is genuine shared state |
| Styling | **Tailwind** | Repeatable across 19 sites |
| Hosting | **Cloudflare Pages** | Free, global edge, instant deploys |
| Server bits | **Pages Functions / Workers** — only where unavoidable | URL fetching, YouTube API. Most sites need none |
| Analytics | **GA4**, linked to AdSense | Revenue **per page** via Monetization -> Publisher Ads. This is the feedback loop the whole business runs on. Load it *after* interactive. Cloudflare Web Analytics optional as a lightweight second view |
| Database | **none** unless the tool truly needs one | |

**Non-negotiable:** no signup, no account, no upload-to-server where the work can run in the
browser. In-browser processing is a real differentiator against these incumbents and a CTR
angle worth putting in the meta description.

## SEO strategy

1. **Domain — qualified EMD.** Clean exact-match `.com` is gone almost everywhere. Use the
   pattern that actually worked for compilefuture (`realonlineruler.com`, `fontfinderai.com`):
   full query phrase plus one qualifier. Verify availability before buying.
2. **Homepage targets the primary head term.** Tool above the fold, working on load, no
   JS spinner.
3. **One page per distinct intent — not per trivial variant.** Modifier variants
   (`X online`, `free X`, `X tool`) belong on the *same* page; Google treats them as one
   query. A synonym describing a genuinely different job gets its own page.
4. **Tool first, prose second, always.** Never a wall of text above the tool.
5. **Depth below the tool is what beats a bare tool page:** what the result means, how to
   read it, common failure modes, device/browser-specific notes.
6. **Schema:** `WebApplication` + `FAQPage`. **Plus:** sitemap-index.xml, robots.txt, OG image.
7. **Internal links between every tool page.**
8. **Country pages only if the data justifies them** — check the geo split in the facts above
   and in `04-TOOL-VALIDATION.md`. Several clusters are India/SEA-heavy and monetise poorly.
9. **No bought backlinks.** Authority here comes from the tool being genuinely worth linking to.

## Build checklist

- [ ] `git init` + GitHub repo + Cloudflare Pages connected **before any component**
- [ ] `public/_headers` noindexing `pages.dev` live from the first commit, and
      **still present after launch** — it is permanent, not a build-time flag
- [ ] Astro + Tailwind scaffold auto-deploying to `<project>.pages.dev`
- [ ] All testing done against the live pages.dev URL, never localhost
- [ ] Logo + favicon via **logofa.st**, then run through **realfavicongenerator**
- [ ] **800-1200 words** of on-page content per tool page
- [ ] **PAA research done first** — expand every People Also Ask box on all 5 synonym
      SERPs, record 15-25 questions verbatim (see SEO-BRIEF §5)
- [ ] FAQ section with **JSON-LD**, 10-15 questions, all sourced from PAA
- [ ] `/about/` `/contact/` `/privacy/` `/terms/` + **404 and 500** pages
- [ ] **Cloudflare mail routing** to Gmail so `/contact/` actually works
- [ ] Deploy script in `package.json`
- [ ] Re-check domain availability, buy the qualified EMD (**last step, not first**)
- [ ] Core tool working client-side, above the fold
- [ ] Lighthouse 100 / 100 / 100 / 100 on **mobile**
- [ ] One page per distinct intent, internally linked
- [ ] Schema, OG image, favicon, sitemap-index.xml, robots.txt
- [ ] Google Search Console + Bing Webmaster verified, sitemap submitted
- [ ] **GA4 installed and linked to AdSense**; script loads after interactive
- [ ] Ads only once traffic exists — AdSense needs real content anyway

## Skills to invoke in a fresh session

| When | Skill |
|---|---|
| Before building anything | `superpowers:brainstorming` |
| Any HTML/CSS/client JS | `modern-web-guidance` — **mandatory, run first** |
| UI design | `frontend-design` or `impeccable` |
| Core Web Vitals | `web-perf`, `chrome-devtools-mcp:debug-optimize-lcp` |
| Accessibility | `accesslint:audit` |
| Pre-launch | `claude-seo:seo-audit`, `claude-seo:seo-schema`, `claude-seo:seo-sitemap` |

`ponytail` is active by default — build the minimum that works, not the maximum that impresses.

## Judging months 1–6 without fooling yourself

Raw traffic is the wrong month-3 metric; every site looks like a failure at month 3.

1. **Average position trend per cluster.** 60 → 35 → 22 is success even at zero clicks.
   Flat at 35 for three months is the real failure signal.
2. **Count of keywords with any impressions** — should grow weekly early on.
3. **CTR where already top-10.** Under 3% at position 5–8 means the title/description is the
   problem, not the ranking.
4. **Time to first page-1 keyword** — predicts the rest of the portfolio better than anything else.

## Scope

**This folder is the whole project.** Everything needed to build, rank and launch this site is
in `BRIEF.md`, `SEO-BRIEF.md`, `PROGRESS.md` and `DESIGN.md`.

Portfolio-level research — the seed validation, competitive data and build order behind this
site's selection — is held separately by the operator and is **not needed here.** If something
about the strategy is unclear, ask; do not go looking for files outside this folder.
"""


def brief(order, slug, display, primary, absorbed, rpm, pool, incumbents):
    kws = [primary] + absorbed
    lines = [f"# {display} — build brief", ""]
    pos = BUILD_ORDER.index(order) + 1
    lines.append(f"> **Site {order}** in the microtools portfolio · "
                 f"**build position {pos} of {len(BUILD_ORDER)}**")
    lines.append("")
    lines.append("## What this site is")
    lines.append("")
    lines.append(f"**Primary tool (names the domain):** {primary}")
    if absorbed:
        lines.append("")
        lines.append("**Also ships (same site, own pages):** " + " · ".join(absorbed))
    lines.append("")
    lines.append(f"**Est. RPM** {rpm}  ·  **incumbent traffic pool** {pool}")
    lines.append("")
    lines.append(f"**Incumbents to study:** {incumbents}")
    lines.append("")
    lines.append("### Target keyword cluster")
    lines.append("")
    for k in kws:
        syns = SYN.get(k, [])
        lines.append(f"**{k}**")
        for s in syns:
            u = SERP.format(urllib.parse.quote_plus(s))
            lines.append(f"- [{s}]({u})")
        lines.append("")
    lines.append("*Links open the US SERP with personalisation off. Modifier variants of these"
                 " phrases share a page; the phrases themselves may not.*")
    lines.append("")
    lines.append("### Domain candidates")
    lines.append("")
    avail = DOMAINS.get(slug)
    if avail:
        lines.append("Confirmed **available** in the RDAP sweep of 2026-08-22 - "
                     "**re-verify before buying, availability moves**:")
        lines.append("")
        for dmn in avail:
            lines.append("- `" + dmn + "`")
    else:
        lines.append("No clean exact-match `.com` was free in the RDAP sweep of "
                     "2026-08-22. Use the **qualified-EMD** pattern - full query phrase "
                     "plus one qualifier (`free`, `online`, `real`, `my`, `pro`, or a "
                     "verb) - and check availability at instantdomainsearch.com.")
    lines.append("")
    lines.append("### Cross-links authorised for this site")
    lines.append("")
    cls = CROSSLINKS.get(slug)
    if cls:
        lines.append("The operator has authorised the following, and **only** the "
                     "following. Add exactly these, nothing more:")
        lines.append("")
        lines.append("| Target URL | Placement | Anchor | Why |")
        lines.append("|---|---|---|---|")
        for url, place, anchor, why in cls:
            lines.append("| " + url + " | " + place + " | " + anchor + " | " + why + " |")
    else:
        lines.append("**None.** Do not link to any other site in this portfolio. "
                     "If a link is ever authorised it will appear in this table - "
                     "an empty table means the answer is no.")
    note = NOTES.get(slug)
    if note:
        lines.append("")
        lines.append("### Notes specific to this site")
        lines.append(note.strip())
    return "\n".join(lines) + "\n" + BODY


GENERATED = ("<!-- GENERATED by research/make_sites.py - do not edit by hand. "
             "Edit make_sites.py / seo_brief_body.py and re-run. -->")

# Astro's VS Code extension ships Prettier formatting for .astro by default
# (verified against withastro/docs editor-setup, 2026-08-24).
VSCODE_EXTENSIONS = """{
  "recommendations": [
    "astro-build.astro-vscode",
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint"
  ]
}
"""

VSCODE_SETTINGS = """{
  "editor.formatOnSave": true,
  "[astro]": { "editor.defaultFormatter": "astro-build.astro-vscode" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[css]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "files.associations": { "*.astro": "astro" },
  "emmet.includeLanguages": { "astro": "html" }
}
"""


def claude_md(order, display, primary, absorbed, tier, why):
    pos = BUILD_ORDER.index(order) + 1
    total = len(BUILD_ORDER)
    also = (" + " + " + ".join(absorbed)) if absorbed else ""
    return f"""{GENERATED}

# {display}

**Site {order}** · build position {pos} of {total}
Build: **{primary}**{also}

> **SERP-replacement risk: {tier}.** {why}

**Read `BRIEF.md` (what to build, keyword cluster, incumbents) and `SEO-BRIEF.md`
(15-section SEO spec) before writing anything.**

**Also read <https://compilefuture.com/blog/making-50-lpa-from-my-own-ai-business/> in full**
— the reference build process this portfolio models. Use its prompts and checklist; improve
where `BRIEF.md` is stricter.

**Step 0, before any code:** decide the **target competitor** (pick the beatable one from the
incumbent list, document their weaknesses) and the **domain** (qualified EMD, check
instantdomainsearch.com, do not buy until launch). See `BRIEF.md` -> Step 0.

## Non-negotiables

1. **Never write library code from memory.** `context7` MCP for Astro / Tailwind / any npm
   package; `cloudflare` + `wrangler` skills for Cloudflare; `modern-web-guidance` before any
   client JS. **Latest stable only** — never alpha/beta/RC. Docs beat memory, always.
2. **MPA, never SPA.** Real URLs, full page loads, no `<ClientRouter />`. All content,
   headings, links, meta and schema in the initial HTML — only the tool itself is JS.
3. **Deploy day 1.** `git init` -> GitHub repo -> Cloudflare Pages, *before* any component.
   **First run `gh auth status` and confirm with the operator WHICH GitHub account to use —
   they have three.** Record it in `PROGRESS.md`. Wrong account means rebuilding the repo and
   the Cloudflare connection.
   `public/_headers` noindexing `pages.dev` from the **first commit, permanently** — it is
   hostname-scoped, so it never gets removed. Workers: disable the `workers.dev` route once
   the custom domain is live. Prevents permanent duplicate content.
   Test against the live `pages.dev` URL, **never localhost**.
4. **Core Web Vitals:** LCP < 1.2s, INP < 100ms, CLS 0 — field data, not lab scores.
5. **Multilingual from launch** — English + the top 2-3 non-English markets in `BRIEF.md`.
   Subdirectories, reciprocal hreflang, no IP redirects.
6. **No signup, no accounts, no upload-to-server** where it can run in the browser.
7. **Domain last.** Custom domain + GSC only once the pre-launch gate fully passes.
8. Separate real pages for `/about/`, `/contact/`, `/privacy/`, `/terms/`.
   Privacy is **required for AdSense**.
9. **FAQ questions come from Google "People Also Ask" — never invented.** Expand every PAA
   box on all five synonym SERPs (the links are in `BRIEF.md` -> Target keyword cluster),
   record 15-25 verbatim, keep 10-15. Repeat per locale — PAA differs by country. SEO-BRIEF §5.

10. **Every session starts cold** — the operator uses a new chat or `/clear` per task to
    save tokens. **Nothing is remembered between sessions.** Read `PROGRESS.md` first, write
    every decision into it, and update it **before the session ends**. A decision that only
    exists in the conversation is lost.
11. **Never add a link to another site in this portfolio** unless `BRIEF.md` ->
    *Cross-links authorised for this site* lists it explicitly. **An empty table means no.**
    Never add one on your own initiative, never on launch, never in a batch.
12. **The repo is ALWAYS private.** `gh repo create --private`. Never public, never made
    public later. Verify with `gh repo view --json visibility`.
13. **Once the site is LIVE, never commit to `main`.** Branch -> verify on the Cloudflare
    branch preview URL -> merge. Every push to `main` deploys to production worldwide.
    **Before launch this does not apply** — commit straight to `main` and move fast, there is
    nothing live to protect. Check `PROGRESS.md` for whether this site has launched.
14. **Commit after every completed step or feature — not once per session.** One logical
    change per commit, always in a working state. Granular history is what makes a clean
    revert possible, and the log is the second memory a cold session reads.

## Read only what the task needs

`SEO-BRIEF.md` is ~640 lines. Do not load it whole for a CSS fix.

| Task | Read |
|---|---|
| Starting the site | `PROGRESS.md` + `BRIEF.md` (whole) |
| Building the tool / UI | `PROGRESS.md` + `DESIGN.md` |
| On-page SEO pass | `SEO-BRIEF.md` sections 1-7 |
| Content + FAQ | `SEO-BRIEF.md` section 5 |
| Adding a language | `SEO-BRIEF.md` section 14 |
| AEO / AI citation | `SEO-BRIEF.md` section 16 |
| GSC setup | `SEO-BRIEF.md` section 11 |
| Pre-launch | `SEO-BRIEF.md` section 12 |
| Anything touching a library | fetch docs first — Iron Rule 1 |

## Stack

Astro (static MPA) · vanilla JS islands · Tailwind v4 · Cloudflare Pages
Workers/Pages Functions only where a server is genuinely unavoidable.

**This is the toolchain, not a template.** Every site is a separate project: **different
design language, different layout, different page structure, freshly written copy.** The
briefs share a *method*; the sites must not look like siblings. Pick a design from
[getdesign.md](https://getdesign.md) that other sites in the portfolio are not using.

## Project setup — run inside this folder, after `git init` + Astro scaffold

```
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
npx skills add https://github.com/lombiq/tailwind-agent-skills --skill tailwind-4-docs
npx getdesign@latest add vercel
```

**All three are per-site, project scope. Never install them in the parent `microtools/`
folder** — that folder is strategy and portfolio management only. Each site owns its own
copy so they can diverge and so nothing leaks between builds.

Project scope, per site. **`getdesign` walks *up* the tree for a project root — scaffold
first or `DESIGN.md` lands several directories above you.**

**`DESIGN.md` is the design authority. Read it before writing any UI.** Vercel is the
portfolio default; to use a different language, browse
**[getdesign.md](https://getdesign.md)** (Vercel, Apple, Claude, others) and
`npx getdesign@latest add <name>`. One design per site, never mixed.

## Editor

The **Astro VS Code extension** (`astro-build.astro-vscode`) is the recommended setup and
**includes Prettier formatting for `.astro` by default** — no extra config needed in-editor.
`.vscode/extensions.json` and `.vscode/settings.json` are already in this folder.

For formatting outside the editor (CLI / CI), add:

```
npm install --save-dev --save-exact prettier prettier-plugin-astro
```

`.prettierrc`:

```json
{{
  "plugins": ["prettier-plugin-astro"],
  "overrides": [{{ "files": "*.astro", "options": {{ "parser": "astro" }} }}]
}}
```

Then `npx prettier . --write`.

## Scope

**This folder is the entire project.** `BRIEF.md`, `SEO-BRIEF.md`, `PROGRESS.md` and
`DESIGN.md` contain everything needed. Do not look for files outside it — portfolio-level
research lives elsewhere and is not required here. If strategy is unclear, ask the operator.
"""


def main():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "websites")
    root = os.path.normpath(root)
    nl = chr(10)
    for order, slug, display, primary, absorbed, rpm, pool, inc in SITES:
        pos = BUILD_ORDER.index(order) + 1
        d = os.path.join(root, f"{pos:02d}-{slug}")   # number = build order, slug = identity
        os.makedirs(d, exist_ok=True)
        tier, why = RISK[slug]

        with open(os.path.join(d, "BRIEF.md"), "w", encoding="utf-8") as f:
            f.write(GENERATED + nl + nl
                    + brief(order, slug, display, primary, absorbed, rpm, pool, inc))

        with open(os.path.join(d, "SEO-BRIEF.md"), "w", encoding="utf-8") as f:
            head = GENERATED + nl + nl + "# " + display + " - SEO brief" + nl + nl
            head += "> **SERP-replacement risk: " + tier + ".** " + why + nl
            f.write(head + SEO_BODY)

        with open(os.path.join(d, "CLAUDE.md"), "w", encoding="utf-8") as f:
            f.write(claude_md(order, display, primary, absorbed, tier, why))

        pm = os.path.join(d, "PROGRESS.md")
        if not os.path.exists(pm):          # never clobber real progress
            with open(pm, "w", encoding="utf-8") as f:
                f.write(PROGRESS_MD.format(display=display))

        vs = os.path.join(d, ".vscode")
        os.makedirs(vs, exist_ok=True)
        for fn, content in (("extensions.json", VSCODE_EXTENSIONS),
                            ("settings.json", VSCODE_SETTINGS)):
            with open(os.path.join(vs, fn), "w", encoding="utf-8") as f:
                f.write(content)

        print(f"  {pos:02d}-{slug}  [{tier}]")
    print(f"{len(SITES)} site folders -> {root}")


def demo():
    assert len(SITES) == 21, len(SITES)
    orders = [s[0] for s in SITES]
    assert orders == sorted(orders), "build order must be ascending"
    # every one of the 34 seeds must land in exactly one site
    seen = []
    for _, _, _, primary, absorbed, *_ in SITES:
        seen += [primary] + absorbed
    assert len(seen) == 39, f"{len(seen)} seeds mapped, expected 39"
    assert len(set(seen)) == 39, "a seed is mapped to two sites"
    missing = set(SYN) - set(seen)
    assert not missing, f"seeds not mapped to any site: {missing}"
    slugs = {s[1] for s in SITES}
    assert set(DOMAINS) <= slugs, set(DOMAINS) - slugs
    assert set(NOTES) <= slugs, set(NOTES) - slugs
    ids = {x[0] for x in SITES}
    assert sorted(BUILD_ORDER) == sorted(ids), "BUILD_ORDER must list every site once"
    assert slugs == set(RISK), f"RISK/SITES mismatch: {slugs ^ set(RISK)}"
    print("ok")


if __name__ == "__main__":
    (demo if len(sys.argv) > 1 and sys.argv[1] == "demo" else main)()
