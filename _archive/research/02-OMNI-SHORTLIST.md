# Omni Calculator shortlist — highest-probability targets

Source: omnicalculator.com sitemap, **3,875 English calculators**, extracted 2026-08-22.
Filtered to **3,117** after removing YMYL. This document ranks what survives.

**No search-volume data is used here.** Volume is the one thing I could not obtain for
free. Every ranking below is from SERP shape, task shape, competitor structure, and
build feasibility. Run the free validation checklist (§4) on each before building.

---

## 1. What was cut, and why

| Category | Count | Verdict |
|---|---|---|
| `finance` | 606 | **Cut 323** as YMYL (loan/tax/mortgage/investment/retirement/insurance). The ~283 survivors are corporate-accounting formula cards owned by Investopedia / CFI / WallStreetPrep — massive E-E-A-T domains. **Cut the rest too.** |
| `health` | 435 | **All cut.** YMYL by definition. |
| `conversion` | 327 | **Almost all cut.** Google answers unit conversion with its own on-SERP widget — the brief's explicit rejection criterion "Google itself directly satisfies the query". Handful of practitioner exceptions noted in §3. |
| `math`, `statistics` | 873 | **Cut.** Homework intent, dominated by academic domains + Google's own widgets, near-zero advertiser value. |
| `physics`, `chemistry`, `biology` | 754 | **Mostly cut.** Same reason. A few practitioner ones survive (optics, acoustics). |
| `construction` | 156 | **Best category.** Real money, DIY intent, strong advertisers, layout-shaped problems. |
| `everyday-life` | 287 | **Second best**, but half is date arithmetic (Google answers directly) — cut those. |
| `other` | 225 | Mixed. Good pockets: photo/video, logistics, AV, gaming. |
| `food` | 68 | Small but good — event/catering planning is layout-shaped. |
| `sports` | 110 | Mostly YMYL-adjacent fitness. A few spatial ones survive. |
| `ecology` | 34 | Cut — activism content, weak commercial intent. |

## 2. The selection rule

Omni pages are **formula cards**: inputs → one number → boilerplate prose. They rank by
domain strength, not by being good. So the targets are topics where:

1. **The true answer is not one number** — it is a layout, a diagram, a cut list, a
   printable template, or a plan. Omni structurally cannot serve this, and neither can
   the AI calculator farms (see `01-INTERIM-FINDINGS.md` Finding 5).
2. **Real-world money is attached** → DIY, trade, event, or equipment advertisers.
3. **The task has a workflow**, not a single input set — presets, multiple rooms/pieces,
   save/compare.
4. **Natural long-tail** across materials, sizes, brands, or room types.

> The single best signal: **the user's real question ends in "…and show me where."**
> Omni can never answer that.

---

## 3. The shortlist

`★` = my confidence that this matches your criteria. Check each yourself with §4.

### Tier A — layout & template problems (strongest)

The answer is a diagram or a printable, and the DIY/trade audience has advertisers.

| # | Omni topic | ★ | Why Omni is weak here | What to build instead |
|---|---|---|---|---|
| 1 | `board-and-batten` | ★★★★★ | Huge current DIY trend. Real question is "where do my battens go so spacing is even?" Omni gives a count. | Visual wall elevation: enter wall width/height + batten width + desired spacing → SVG wall with every batten positioned, exact mark-out list in inches, printable cut list. Handle doors/windows/outlets. |
| 2 | `wainscoting` | ★★★★★ | Same shape, same audience, harder geometry (panel + stile + rail proportions). Omni gives a number. | Panel layout generator with a true elevation drawing + mark-out tape-measure list. |
| 3 | `spindle-spacing` / `baluster` | ★★★★☆ | Code-constrained (4" sphere rule) *and* an even-spacing layout problem. | Railing layout: post-to-post span → exact baluster positions, code check, printable mark-out strip. |
| 4 | `recessed-lighting` | ★★★★☆ | Ceiling grid layout. Omni gives "how many lights". Real question is the grid + wall offsets. | Ceiling plan generator: room dims → light positions, spacing/offset rules, printable ceiling plan. |
| 5 | `bolt-circle` | ★★★★☆ | Machinist/fabricator. Needs coordinates, not a diameter. | X/Y coordinate table + to-scale printable drill template + DXF. |
| 6 | `circle-skirt` | ★★★★☆ | Sewing. Answer is a **pattern**, not a radius. | Radius math + printable 1:1 tiled pattern piece with seam allowance. |
| 7 | `projector` (throw distance) | ★★★★☆ | Answer is a room diagram: where to mount, image size at that distance. | Side-elevation room diagram + mount position + screen size, per projector throw ratio. |
| 8 | `rug-size` | ★★★☆☆ | Answer is "how does it look under my furniture". | Top-down room planner with furniture blocks + rug overlay. |
| 9 | `pool-table-room-size` | ★★★☆☆ | Clearance/fit problem — visual. | Room fit diagram with cue clearance envelope, pass/fail per table size. |
| 10 | `spiral-staircase` | ★★★☆☆ | Genuinely 3D. Omni card is inadequate. | Plan + elevation view, tread angles, printable tread template. |
| 11 | `birdsmouth-cut` | ★★★☆☆ | Carpentry cut layout. | To-scale cut diagram + printable rafter marking guide. |
| 12 | `rolling-offset` | ★★★☆☆ | Pipefitting jargon, trade audience. | Isometric diagram + cut lengths, fitting-angle presets. |

### Tier B — dataset / lookup problems (farms structurally can't do these)

Requires curated reference data, not a formula. Verify nobody has built it.

| # | Omni topic | ★ | Why | What to build |
|---|---|---|---|---|
| 13 | `box-fill` | ★★★★☆ | NEC electrical box-fill is a **code table** lookup, not arithmetic. | Conductor/device picker → fill calc + code citation + box recommendation. |
| 14 | `metric-to-sae` | ★★★★☆ | Practitioner conversion Google does *not* widget. Wrench/socket cross-reference. | Nearest-fit socket/wrench cross-reference with tolerance warnings ("close but will round the bolt"). |
| 15 | `mesh-to-micron-converter` | ★★★☆☆ | Industrial sieve/abrasive/filter jargon. Real table, multiple standards. | Cross-standard sieve table (US/Tyler/ISO) + abrasive grit equivalence. |
| 16 | `hardness-conversion` | ★★★☆☆ | Rockwell/Brinell/Vickers cross-reference — a **standards table** (ASTM E140). | Full cross-reference with material caveats. |
| 17 | `freight-class` | ★★★☆☆ | NMFC class lookup — density + commodity table. | Density calc → class + commodity search. |
| 18 | `din-ski` | ★★☆☆☆ | Chart lookup, but **safety-adjacent** — bindings. Include disclaimers or skip. | — |
| 19 | `paper-quantity` / `paper-weight` | ★★★☆☆ | Basis-weight (text/cover/bond/index) is a genuinely confusing **cross-standard table**. | gsm ↔ lb converter that asks *which* stock type — the thing every existing tool gets wrong. |
| 20 | `linear-inches` | ★★★☆☆ | Airline baggage limits = a **carrier dataset** that changes. | Bag dims → pass/fail per airline, with cabin/checked rules. |

### Tier C — packing / fit problems (visual, genuinely hard, low competition)

| # | Omni topic | ★ | What to build |
|---|---|---|---|
| 21 | `pallet` | ★★★★☆ | Ti-Hi pallet pattern **diagram** — box dims → optimal layers/orientation, top-down pattern drawing, overhang warnings. |
| 22 | `container-loading` / `cbm-shipping` | ★★★☆☆ | 3D load plan visual, not a CBM number. |
| 23 | `classroom-spacing` | ★★☆☆☆ | Desk layout diagram for a room. Narrow but unserved. |
| 24 | `bbq-grill-size` | ★★☆☆☆ | Grill surface fit — burgers/racks laid out visually. |

### Tier D — event & quantity planning (strong ad value, weak current tools)

| # | Omni topic | ★ | Note |
|---|---|---|---|
| 25 | `cake-serving` + `cake-pans` | ★★★★☆ | Wilton owns the static chart. Nobody has a **tier planner**: pick tier sizes → servings + a rendered cake elevation + dowel/support plan. Big Etsy/home-baker audience. |
| 26 | `wedding-alcohol` / `party-drink` | ★★★☆☆ | Guest count → full shopping list by bottle, not a number. High advertiser value. |
| 27 | `tent-size` / `how-many-tables` | ★★★☆☆ | Event layout diagram — tables inside a tent footprint. |
| 28 | `helium-balloons` / `balloon-arch` | ★★☆☆☆ | Already farm-infested (verified: 4 farms). Only worth it as a visual arch designer. |

### Tier E — technical practitioner niches

| # | Omni topic | ★ | Note |
|---|---|---|---|
| 29 | `ground-sample-distance` | ★★★★☆ | Drone-mapping jargon (GSD). Real workflow: sensor + altitude → GSD + flight plan overlap. Growing audience, weak tools. |
| 30 | `speaker-box` + `port-length` | ★★★☆☆ | Subwoofer enclosure design — needs a **box drawing + cut sheet**, which Omni has no way to give. Verify competition (several exist). |
| 31 | `wheel-offset` | ★★★☆☆ | Visual fitment comparison — old vs new wheel overlay diagram. Big car audience. |
| 32 | `edpi` | ★★☆☆☆ | Gaming mouse sensitivity. Huge audience, but low ad value and several tools exist. |
| 33 | `time-lapse` | ★★★☆☆ | Interval → clip length → card space → battery. Multi-output workflow, not one number. |
| 34 | `hammock-hang` | ★★☆☆☆ | Genuine physics + diagram. Small but devoted audience. |
| 35 | `aquarium-glass-thickness` | ★★☆☆☆ | Safety-adjacent (tank failure) — needs care. |

### Explicitly avoid despite looking attractive

`minecraft-circle` (huge traffic, near-zero ad value, saturated) · `roman-numerals`,
`binary`, `hex-to-rgb`, `base64` (Google widgets + thousands of clones) · all
`*-to-*` unit conversions (Google's own widget sits above every result) · all date
arithmetic (`days-between-dates`, `age`, every `*-countdown`) · `tip`, `gpa`, `grade`
(saturated + Google widget) · `beam-deflection`, `floor-joist`, `wood-beam-span`,
`door-header-size`, `snow-load` (**structural — safety-critical engineering, explicitly
excluded by your brief**).

---

## 4. Free validation checklist — run per idea

No paid tools. In order; stop at the first fail.

**Step 1 — Real query language + cluster breadth** (free, this is Google's own data)
```
https://www.google.com/complete/search?client=chrome&hl=en&gl=us&q=<topic>
```
Also run `<topic> a`, `<topic> b`, … `<topic> z`. A term only appears in autocomplete if
it clears Google's popularity threshold — **presence is a demand floor**. Many distinct
completions = a real cluster, not a one-off.
*(`harvest.py suggest` in this repo automates exactly this.)*

**Step 2 — Farm count (the highest-value 30 seconds)**
Search `<topic> calculator` on Google. Count results whose domain contains *calc* or
*tool* and that you have never heard of — `usecalcpro`, `calcimator`, `enbilex`,
`niftool`, `found-tools`, `everycalculators`, `mycalcbuddy`, `agentcalc`, `claycalc`…

- **4+ farms → REJECT.** The task is a formula; it is infinitely cloneable and already
  cloned. (Verified across 26 queries — see Finding 5.)
- **0 farms, and you see PDFs / forums / vendor pages / Scribd → INVESTIGATE.** Nobody
  could auto-generate it.

**Step 3 — Is Omni alone?**
If Omni ranks and there is **no dedicated site** for the topic, that is your opening —
a thin formula card from a generalist is weak competition regardless of domain rating.
If 3+ *dedicated* sites already exist, reject.

**Step 4 — The "show me where" test**
Ask: does the user's real question end in *"…and where does it go?"* / *"…what does it
look like?"* / *"…give me something I can print?"* If yes, you can build something Omni
and the farms structurally cannot. If the honest answer is one number, walk away.

**Step 5 — Tier check (free, coarse)**
[Google Trends](https://trends.google.com) — compare the term against a known reference.
If it returns **no data**, you are likely under ~1,000/mo (your Tier 1, which is fine).
If it shows a stable line, you are likely Tier 2+.

**Step 6 — Money check**
Would a heat press / lumber yard / lighting brand / event supplier bid on this? If the
audience is students or hobbyists with nothing to buy, RPM will be poor even if traffic
is good.

---

## 5. Two candidates found *outside* Omni that beat most of this list

Both came from jargon mining, not the catalog, and both have verified SERPs. Details in
`01-INTERIM-FINDINGS.md`.

- **DTF transfer size & placement** — SERP is **8 vendor blog posts with static tables
  that contradict each other**, zero tools, zero farms. Build: to-scale garment diagram,
  upload-your-design true-scale preview, printable 1:1 placement ruler.
- **Stage-lighting gel cross-reference (Lee ↔ Rosco ↔ GAM ↔ Apollo)** — SERP is
  4 PDFs, a Scribd paywall, a forum, and a 1990s personal page. Zero neutral tools,
  zero farms. Each vendor ships only its own biased chart.
