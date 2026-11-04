# Interim findings — Phase 1/2

Status: discovery running. 97 jargon seeds expanded (9,700+ real Google queries),
3,117 Omni calculator topics queued for Keyword Planner volume.

---

## Finding 1 — the formula-calculator market is closed

Every "X calculator" where X is a **documented formula** is already taken. Not by one
competitor — by a layer of high-authority generic farms that have systematically
covered the entire space of published formulas:

- omnicalculator.com — **3,875 English calculators** (confirmed by sitemap)
- calculator.net, calctool.org, calculatorshub.net, inchcalculator.com,
  calculatorsoup, gigacalculator, easycalculation, calculator.academy
- plus a 2025–26 wave of AI-generated calculator farms (calcimator.com,
  textilecalculator.com, yarnplot.com, riatto.ovh, fibertools.app …)

Two live tests confirmed this reaches far deeper than expected:

| Test query | Expectation | Reality |
|---|---|---|
| `weaving sett calculator` | obscure fiber-craft jargon | **8 dedicated calculators** incl. 4 AI farms |
| `wing cube loading calculator` | obscure RC-aviation jargon | **10 tools** incl. Omni, CalcTool, CalculatorsHub, MATLAB, 3 club sites |

If a formula is written down anywhere, assume the farms have it. Jargon alone is no
longer a moat — the farms scrape jargon too.

## Finding 2 — three things the farms structurally cannot copy

The farms generate **formula cards**: inputs → a number → boilerplate prose. Their
whole production model breaks on three classes of tool:

**Moat A — cross-vendor equivalence data.**
Each vendor publishes only *their own* crosswalk, as a PDF, biased toward their own
products. Nobody has commercial incentive to build the neutral N×N tool. Farms can't
generate it because the data isn't a formula.

**Moat B — combinatorial search over a device-specific dataset.**
Not "apply formula", but "search all valid combinations of the parts *this specific
machine* has". Requires per-model datasets and a solver.

**Moat C — the output is a drawing, not a number.**
A printable pattern, cut layout, ring diagram, flat development, dieline. Farms output
text; they have no geometry pipeline.

A fourth, weaker one: **file in → analysis out** (upload PDF/image/CSV). Farms don't
process uploads. Weaker because dedicated file-tool sites do exist.

## Finding 3 — the strongest gap found so far

**Query family:** `lee to rosco gel conversion` / `rosco to lee equivalent` /
`gam to rosco` / `e colour to rosco` + per-gel long tail (~250 gel numbers).

**What Google shows today** (verified):

| # | Result | Kind |
|---|---|---|
| 1 | scribd.com — "LEE to ROSCO Equivalents" | **paywalled PDF scan** |
| 2 | us.rosco.com/en/lee-rosco-equivalents | vendor page, Rosco-biased |
| 3 | leefilters.com gel-comparator | vendor tool, Lee-biased |
| 4 | lightmoves.com.au | **PDF** |
| 5 | controlbooth.com | **forum thread** |
| 6 | lightmoves.com.au | **PDF** |
| 7 | us.rosco.com …Conversion_Chart.pdf | **PDF** |
| 8 | barriemacarthur.com/funlights/lgtgelLto.htm | **1990s personal page, plain HTTP** |
| 9 | us.rosco.com resource | vendor page |
| 10 | wikipedia | encyclopedia |

Four PDFs, one Scribd paywall, one forum, one 1990s page, zero neutral cross-brand
interactive tools. This is a textbook Google Search Gap and it matches Moat A exactly.

Audience: theatre/film/church/school lighting techs — US/UK/CA/AU heavy, repeat use
(every show), non-YMYL, no E-E-A-T burden. Long tail is naturally large and genuine
(each gel number has real distinct data: colour swatch, transmission %, mired shift).

**Not yet validated:** search volume (pending Keyword Planner).

## Finding 3b — second strong gap: garment transfer sizing & placement

**Query family:** `dtf transfer size chart` (+ `for shirts` / `youth` / `toddler` /
`back of shirt` / `in inches` / `pdf` / `pdf free download`) — 13 distinct tool-intent
variants harvested from Google autocomplete on one seed.

**What Google shows today** (verified): eight results, and **every single one is a DTF
printing vendor's own content-marketing page with a static table**:

transferkingdom.com · housedtf.com · dtfnewengland.com · indianadtfprint.com ·
dtfdatabase.com · uploaddtf.com · samsdtftransfers.com · dtfjersey.com

Zero interactive tools. Zero calculator farms. And the tables **contradict each other**
on adult width (10–12" vs 12–14" for 2XL+) and on collar drop (3–4" vs 2–3").

**Why the farms are absent:** it is not a formula. It is a garment × size × placement
lookup whose real answer is *visual* — "will my 11×14 design look right on a youth
medium, and how far below the collar does it sit?"

**The product gap:** nobody has built the obvious thing —
- pick garment type + size + placement → to-scale SVG shirt diagram with the design
  outline drawn on it and exact dimensions + collar drop
- **upload your design PNG → see it composited at true scale on the garment** (client-side
  canvas; no vendor has this)
- **print a 1:1 placement ruler / alignment template** — note the SERP itself surfaces
  "shirt placement ruler" as a physical product people buy; a free printable one is a
  strong hook and a natural link magnet

All client-side. No API. MVP is 1–3 days.

**Audience & money:** DTF/heat-press is a large US small-business and Etsy-seller trend
(also UK/CA/AU). Repeat use on every new design. Advertisers are heat presses, DTF film,
blanks, and print services — high-value display inventory. Non-YMYL, no E-E-A-T burden.

**Risk:** vendors have commercial incentive and will keep publishing charts. But they are
shops — their SEO effort goes to product pages, and none has built a tool in years.

**Not yet validated:** search volume (pending).

## Finding 4 — Moat A is *not* open everywhere

Same pattern, different niche, opposite result:

- `embroidery thread conversion isacord madeira robison-anton` → **already solved**:
  royal-present.com converter, EmbroideryNerd.io (36,000-thread database),
  AllThreads (23,000 colours, 60 thread lines), Needlepointers (80+ charts).
- `glaze unity molecular formula` → **already solved**: Glazy, Insight,
  HyperGlaze, online-glaze-calculator.com, Ceramic Materials Workshop.

Why those closed and gels didn't: both have **direct e-commerce pull-through** (thread
and glaze materials are consumables sold online), so someone had a reason to build the
tool. Stage lighting gel is bought through trade distributors, not consumer e-comm.

→ **Refined filter: look for Moat A/B/C niches with weak e-commerce pull-through.**

---

## Finding 5 — THE KEY RESULT: farm density is an inverse opportunity signal

A 26-query controlled SERP scan produced the sharpest signal in the whole project.

**Formula-shaped queries are carpet-bombed by a 2026 wave of AI-generated calculator
farms.** Not one or two — five to eight per SERP, all built recently, all thin:

| Query | AI calculator farms in top 10 |
|---|---|
| `came lead glass calculator` | **8** — calcimator, hqcalculator, usecalcpro, superglobalcalculator ×2, fullcalculator, bencritt … |
| `stone mm to carat calculator` | **8** |
| `kiln ramp hold schedule calculator` | **7** — calculatorlib, completecalculators, usecalcpro, calcimator, enbilex ×2, claycalc, agentcalc |
| `letter height viewing distance calculator` | **7** — niftool ×2, everycalculators, jcalculator, found-tools, ultimatefinancecalculator |
| `hair developer volume ratio calculator` | **7** |
| `ferguson zone uvi calculator` | **6** |
| `subtitle characters per second calculator` | **6** |
| `dmx address calculator` | **5** |
| `wing cube loading calculator` | **5** |
| `balloon garland length calculator` | **4** — planevent.app, partycalcs.uk, mycalcbuddy, calculatorcorp |
| `saddle stitch creep calculator` | 2 + 3 more thin tools |

**Dataset-shaped queries have zero.**

| Query | Farms | What ranks instead |
|---|---|---|
| `lee to rosco gel conversion` | **0** | vendor pages, 2 Scribd PDFs, distributor lists, a 1990s personal site |
| `pull compensation embroidery` | **0** | industry blogs, software vendor docs |

**Why:** the farms generate *formula cards* — inputs, an equation, boilerplate prose.
That pipeline runs at zero marginal cost over any published formula. It cannot produce
a verified 250-row cross-reference table, a per-machine parts dataset, or a geometric
drawing. Those need real data entry and real code.

### The operational rule this produces

> **Count the AI calculator farms in the top 10. That count is your competition score,
> and it is a proxy for "is this task a formula?"**
>
> - 4+ farms → the task is a formula, it is infinitely cloneable, it is already cloned. **Reject.**
> - 0 farms + PDFs/forums/vendor pages → nobody could auto-generate it. **Investigate.**

This is now automated in `score.py` (`shape: FORMULA (cloned)` vs `dataset/gap`) and
runs over every candidate. It is a much better screen than domain authority, because a
farm has no authority — it wins only because nothing better exists, which means it
also loses the moment something better does.

**Caveat on the scan:** rows sourced from Bing (`eng: bing`) are lower confidence —
Bing broad-matches when it has no exact results, which inflates the gap score. Those
need re-checking on DDG before being trusted.

## Candidate pool (raw, unvalidated — volume pending)

Harvested from real Google autocomplete on jargon seeds.

| Candidate | Moat | Why interesting | Evidence from autocomplete |
|---|---|---|---|
| Stage-lighting gel cross-reference | A | see Finding 3 | — |
| Dividing-head indexing solver | B | plate/hole-circle search per head model | 61 queries incl. `dividing head calculator app`, `40 1 dividing head chart pdf`, `cincinnati dividing head chart`, `ellis dividing head chart` |
| Lathe change-gear solver | B | gear-train search per lathe model | `lathe change gear calculator app`, `mini lathe change gear chart`, `atlas 10 lathe change gear chart` |
| Segmented-bowl ring planner | C | ring diagram + cut list, not a number | 57 queries; **`segmented bowl calculator free online`**, `…calculator excel`, `…calculator app iphone` = explicit demand for a free web version |
| Sheet-metal cone/transition development | C | printable/DXF flat pattern | `sheet metal cone flat pattern calculator`, `flat pattern generator` |
| Packaging dieline generator | C | parametric SVG/PDF box template | ~30 tool queries: `dieline generator free/online/from image`, `dieline maker`, `dieline visualizer`, `dieline to mockup generator` |
| Booklet imposition tool | C+file | page-order + creep for saddle stitch | `booklet imposition calculator/tool`, `free booklet imposition tool`, `pdf booklet imposition online` |
| Upholstery yardage estimator | A-ish | furniture-type dataset, today only supplier PDFs | `sofa upholstery yardage chart pdf`, `auto upholstery yardage chart`, `upholstery fabric estimator charts` |
| Channel-letter LED/weight estimator | B | LED module count per stroke area, sign-trade | `channel letter led calculator`, `channel letter weight calculator`, `channel letter estimator` |
| Spot-colour separation from image | file | screen-print separations, client-side | `spot color separation online free` |
| Image → craft pattern (tufting / punch needle / latch hook) | C+file | colour-quantise to a griddable pattern | `maii punch needle portrait generator`, `printable punch needle template` |
| PDF sewing/cosplay pattern tiler & rescaler | file | A0↔A4 tiling at true scale | `eva foam helmet template free`, template-print cluster |

## Rejected so far (with reason)

| Idea | Reason |
|---|---|
| Weaving sett / EPI | 8 dedicated tools incl. 4 AI farms |
| Wing cube loading | 10 tools incl. Omni + CalcTool |
| Embroidery thread conversion | 3 large databases already |
| Glaze unity molecular formula | Glazy + 4 desktop/web apps |
| Book spine width | KDP, IngramSpark, Blurb all ship one |
| Chipload / feeds & speeds | FSWizard, CNCCookbook, Amana charts |
| Cut list optimizer | cutlistoptimizer.com owns it |
| Pinch-pleat drapery | 8 dedicated calculators (verified SERP) |
| Bias binding / continuous binding | quilting blogs answer it fully |
| Corset pattern drafting | intent is PDFs and books, not a tool |
| Bleed & slug, dot gain | intent is "what is it", not "compute it" |
| Segmented bowl / ring planner | Omni + **blocklayer.com** (which already does printable diagrams well) + terican + GeoGebra + constructioncalculators |
| Sheet-metal cone / transition development | 6+ dedicated tools **with DXF export** (caldereriaonline, conelayout, pipecalculators, buildercalc, miniwebtool) |
| Packaging dieline generator | **9** dedicated free no-signup tools with SVG/DXF/PDF (diecutstudio, dielinelab, diecutmaker, packmyman, pacdora …) |
| PDF sewing-pattern tiler / rescaler | patternsplit + gridprint, both good and free |
| Dividing-head indexing | 3 web tools (cgtk, bilar, engineer-data) — weak/dated, but tiny audience; hold pending volume |
| Kiln ramp/hold, came lead glass, stone mm→carat, hair developer, balloon garland, letter height, Ferguson zone UVI, subtitle CPS, DMX address | **4–8 AI calculator farms each** — see Finding 5 |

**Note on blocklayer.com:** worth knowing as a competitor class of its own. It occupies
Moat C (printable, to-scale diagrams and templates) across construction and woodworking
and does it well. Check it before pursuing any geometry/template idea.

---

## Next

1. Keyword Planner → real volume bands for 3,117 Omni topics + harvested jargon queries.
2. Filter to 100–9,999/mo.
3. SERP-check survivors; find the "Omni ranks alone / only farms rank" set.
4. Deep competitor audit on finalists.
