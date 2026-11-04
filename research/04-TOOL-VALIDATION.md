# Micro-tool validation — 33 shortlisted ideas

Generated 2026-08-22. Sources: Google autocomplete (cluster depth), Bing SERP scrape
(`harvest.py`), WebSearch (SERPs where Bing collapsed). Scored by `score_tools.py`.

## What this measures, and what it does not

| Half | Status |
|---|---|
| **Keyword cluster** — real query language per tool | ✅ done, 11,039 queries / 6,013 verbatim. **Source: Google autocomplete** |
| **Competition** — who ranks, how many are dedicated, EMD held? | ⚠️ done, all 33 — but **Bing + WebSearch, NOT Google** |
| **Search volume + KD** | ❌ **missing — needs Ahrefs.** No paid API in session. |

> **Engine caveat.** The cluster half is genuine Google data. The competition half is not —
> Google SERP scraping is captcha-walled (see `00-METHOD.md`). Competitor *sets* overlap
> heavily across engines for tool queries, but **positions and inclusion differ**, so treat
> the `ded` / `EMD?` columns as directional.

## Primary method: incumbent traffic (supersedes the scraped columns)

Google the seed manually → take the #1 result → paste into **Ahrefs free traffic checker**
(`mode=exact`, "Only specified URL"). Free, real Google rankings, real traffic estimates.
This answers the only question that matters: *how much traffic does winning this niche pay?*

**Do this for all 33**, across the 3–4 synonyms in `synonym-groups.txt`. It outranks every
scraped column in this file.

### Why synonyms, not modifiers

Phrase-match walks *modifiers* (`gamepad tester online`, `gamepad tester ps5`). The cluster
actually lives across *synonyms*. `hardwaretester.com/gamepad` ranks #1 for `gamepad tester`
(26K), `controller tester` (21K), `controller test` (5.1K), `stick drift test` (3.9K) —
**57.2K US, and phrase-match on "gamepad tester" showed none of the last three.**

The `verb` column in the table below has this same defect. It undercounts any cluster whose
demand is split across different words for the same thing. Treat it as a floor.

### Convergence vs fragmentation — the real read

Running 3–4 synonyms tells you more than "is demand real." It tells you **whether one site
already owns the cluster**:

| Pattern | Meaning | Action |
|---|---|---|
| Same site ranks #1 across all synonyms | Entrenched incumbent — it consolidated the cluster already | Hard. Needs a real product edge |
| A different site wins each synonym | **Cluster is fragmented — nobody owns the whole thing** | **Best case.** One site covering all synonyms takes the lot |
| Some synonyms have no dedicated tool | Partial gap | Enter on the unowned synonym, expand |

`gamepad tester` is the first pattern: hardwaretester.com holds position 1 on all five.
That is the hardest shape, and it is why traffic size alone is not the verdict.

**Rank by `$/visit`, not traffic.** Traffic value ÷ organic traffic is the best free
monetization proxy we have. It varies 5x across seeds and reorders the list.

| # | Seed | Incumbent URL | Organic/mo | Traffic value | **$/visit** | Tier-1 geo | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 3 | webcam test | webcamtests.com | 511.8K | **$150.7K** | **$0.294** | **40%** | pending synonyms |
| 4 | microphone test | mictests.com | **703.3K** | $94.6K | $0.135 | 27% | **ENTRENCHED** |
| 5 | speaker test | onlinemictest.com/sound-test | 88.8K | $13.1K | $0.148 | **48%** | FRAGMENTED + **video SERP** |
| 5b | speaker test | audiocheck.net/audiotests | 46.3K | $6.8K | $0.147 | 30% | (2nd) |
| 6 | headphone test | webcammictest.com/headphones | **10.5K** | $2.3K | $0.219 | 31% | **UMBRELLA — fold into 5** |
| 7 | surround sound test | soundtest.io/surround-sound-test | 2.9K | $401 | $0.138 | **84%** | **UMBRELLA — fold into 5** |
| 8 | monitor test | eizo.be/monitor-test | 27.2K | $3.2K | $0.118 | **11%** | weak incumbent, poor prize |
| 9 | dead pixel test | displaytech.org/en/tests/dead.pixel | 100.6K | $6K | **$0.0596** | 16% | **ENTRENCHED** (all 5 at #1) |

| 10 | refresh rate test | testufo.com (+ /refreshrate) | 117.6K + 31.7K | $28.6K + $4.8K | $0.243 / $0.151 | 24% | **ENTRENCHED** |

| 11 | mouse tester | 4-way split | 76.5K / 49K / 13.9K / 13.6K | $11.3K / $9K / $9.1K / $970 | **$0.655** (codepen) | 10–19% | **FRAGMENTED — best signal in set** |

> ### Seed 11 is the strongest opportunity found so far
>
> **A CodePen pen ranks #1 for `double click test`.** `codepen.io/blink172/pen/vERyxK` — a
> throwaway demo — holds #1 for `double click test` 1.7K, `mouse double click test` 400,
> `double click tester` 200, `double click mouse test` 150. **Google has nothing better than
> a CodePen sketch.** No brand, no EMD, no dedicated tool, no links. Strongest weak-SERP
> signal in all 11 seeds.
>
> **And it earns $0.655/visit — 2.2x webcam, highest in the dataset.**
>
> **Why:** `double click test` is a *purchase-intent* query. Your mouse double-clicks → it is
> broken → you are about to buy one. Confirmed by competitor #2: **`redragonshop.com`, a
> gaming-mouse retailer, built a free mouse-tester page and went 0 → 45K in two months.** A
> hardware seller does not build a diagnostic tool for fun.
>
> | Site | Organic | $/visit | Tier-1 | Owns |
> |---|---:|---:|---:|---|
> | onlinemictest.com/mouse-test | 76.5K | $0.148 | 10% | mouse test 7K #1 · mouse tester 2.8K #1 |
> | redragonshop.com/pages/mouse-tester | 49K ↗ | $0.184 | 19% | mouse tester 10K #1 · mouse click test 2.7K #1 |
> | codepen.io/blink172/pen | 13.9K | **$0.655** | 13% | double click test 1.7K #1 |
> | cpstest.org/polling-rate-test | 13.6K | $0.071 | 16% | mouse hz test 3.8K #1 · polling rate test 1.3K #1 |
>
> **Implication beyond display ads:** a mouse-test site has a natural affiliate path (test
> fails → buy a mouse). Redragon is already monetising exactly that way. Affiliate RPM on
> purchase-intent hardware traffic beats display ads substantially. Worth pricing separately
> from the $/visit column.
>
> **Caveat:** $0.655 comes off 13.9K visits, so the estimate is noisier than the large-sample
> ones. The redragonshop evidence corroborates it independently.

> ### EMD scoreboard — runs against the domain thesis
>
> | Seed | EMDs present | Winner |
> |---|---|---|
> | gamepad tester | gamepad-tester.net, controllertest.io, controllertester.co | **hardwaretester.com** (non-EMD) |
> | refresh rate test | screenhz, whatismyrefreshrate, fpstest.org, refreshratetester + 5 | **testufo.com** (non-EMD) |
> | keyboard tester | keyboardchecker.com | **EMD won its own term** over a 5x larger site |
>
> Two losses, one win. Nine exact-match refresh-rate domains all sit below a non-EMD brand.
> **The domain lever wins a specific term, not a cluster.** Weaker than the compilefuture
> framing implies.

> **Seed 9 is the category in one number.** `displaytech.org` is #1 on every keyword in its
> cluster, tripled traffic in four months, and pulls 100.6K visits/mo. At 16% tier-1 and
> $0.0596/visit that is **~$115/month**. Total uncontested victory in a device-test niche
> pays almost nothing.

### 7–9 notes

**`soundtest.io` — live proof the strategy works.** Flat ~0 until July, **2.9K by August**,
while `xbitlabs.com` crashed 3.4K → 1.7K in the same window. soundtest.io took #1 for
`surround sound test` and pushed xbitlabs to #2 in roughly one month. It also appears in the
speaker and headphone SERPs — a single-purpose audio-test site taking the cluster piece by
piece, right now. **Study this site closely; it is a better model than compilefuture because
it is current and observable.**

**How it entered — via the undefended tail.** It holds `7.1 surround sound test` 350,
`test surround sound` 90, `surround test` 50, `7.1 surround test` 30 — terms nobody defends —
*then* took the 1.4K head term. Entry through low-competition keywords, then upward.

**`displaytech.org` — second instance of the same pattern.** 30K (Apr) → 100.6K (Aug).

**`audiocheck.net/audiotests_stereo`: one page ranks for `channel test`, `left right
headphone test`, and `left right speaker test`.** Cheapest possible cluster coverage.

**Surround has the best geo in the dataset** — soundtest.io 84% tier-1, xbitlabs 87%. Home
theatre = wealthy Western markets. Tiny traffic, high value per visit.

| 12 | touchscreen test | onlinemictest.com/touch-screen-test | 30.1K | $4.7K | $0.156 | ~15% | onlinemictest 4/5 · **UMBRELLA** |

> ### THE KEY FINDING: dedicated beats umbrella, every time
>
> `onlinemictest.com` runs the umbrella model with pages for mic, sound, mouse, touchscreen
> and webcam. **It loses every term where a dedicated site exists, and wins every term where
> one does not.**
>
> | Term | onlinemictest page? | Winner |
> |---|---|---|
> | microphone test | yes | **mictests.com** (dedicated) |
> | webcam test | yes | **webcamtests.com** (dedicated) |
> | sound / speaker test | yes | onlinemictest — no dedicated rival, until `soundtest.io` arrived |
> | mouse test | yes | onlinemictest — but `redragonshop` went 0→45K in 2 months |
> | touchscreen test | yes | onlinemictest — no dedicated rival yet |
>
> In both categories where a dedicated entrant has *just* appeared (soundtest.io, redragon),
> the umbrella is being displaced live.
>
> **This is stronger evidence for the single-purpose thesis than the EMD scoreboard, which
> was mixed. It is not the domain name that wins — it is the dedicated page with a whole
> site behind it.** Build single-purpose; the domain is secondary.

## VERDICT: Device diagnostics is winnable, and most of it clears the bar

> **Threshold: ₹10,000/month (~$115).** Operator is India-based; that is real money, not a
> rounding error. An earlier draft of this file judged the category against an unstated
> US-freelancer threshold and wrongly wrote it off. Corrected below.

Entry is demonstrably possible — two sites (`soundtest.io`, `displaytech.org`) are doing it
live. Incumbent earnings **at #1**, at ~₹85/$:

| Seed | USD/mo | ₹/mo | Clears ₹10k? |
|---|---:|---:|:--:|
| webcam test | $1,300–2,500 | ₹1.1–2.1 lakh | yes |
| microphone test | $1,000–2,100 | ₹85k–1.8L | yes |
| keyboard tester | $800–1,500 | ₹68k–1.3L | yes |
| gamepad tester | $400–900 | ₹34k–77k | yes |
| refresh rate test | $220–370 | ₹19k–31k | yes |
| speaker test | $200–400 | ₹17k–34k | yes |
| dead pixel test | $115 | ₹10k | borderline |
| monitor test | $30–50 | ₹2.5–4k | no |
| headphone test | $25–30 | ₹2–2.5k | no |
| surround sound | $10–20 | ₹1–1.7k | no |

**7 of 10 clear the bar at #1.** The caveat that survives: year-one is realistically a #3–#5
finish, i.e. a fraction of these. dead pixel at #1 pays ₹10k, so a #3 there pays ₹2–3k. But
webcam at #3 still pays ₹25–50k — which is why the ranking order holds even though the
kill-threshold moves.

### Device block complete — all 12, ranked by build value

| Rank | Seed | Organic | $/visit | Tier-1 | Pattern | Verdict |
|---:|---|---:|---:|---:|---|---|
| 1 | **webcam test** | 511.8K | **$0.294** | **40%** | pending synonyms | **BUILD** |
| 2 | **mouse tester** | 153K (4-way) | **$0.655** (dbl-click) | 10–19% | **FRAGMENTED** | **BUILD** — CodePen at #1, affiliate upside |
| 3 | microphone test | 703.3K | $0.135 | 27% | ENTRENCHED | big prize, hard entry |
| 4 | speaker test | 135K | $0.148 | 48% | FRAGMENTED | audio-site core |
| 5 | refresh rate test | 149K | $0.243 | 24% | ENTRENCHED | testufo strong |
| 6 | keyboard tester | 574.3K | $0.059 | 20% | US-entrenched | worst $/visit at scale |
| 7 | gamepad tester | 441.7K | $0.088 | 16% | ENTRENCHED | 3 EMDs already lost here |
| 8 | dead pixel test | 100.6K | $0.0596 | 16% | ENTRENCHED | ₹10k at #1 |
| — | monitor test | 27.2K | $0.118 | 11% | — | **fold into screen site** |
| — | touchscreen test | 30.1K | $0.156 | 15% | — | **fold** |
| — | headphone test | 10.5K | $0.219 | 31% | — | **fold into audio** |
| — | surround sound | 2.9K | $0.138 | 84% | — | **fold into audio** |

## COLORS BLOCK

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 13 | image color picker | imagecolorpicker.com | **753.6K** | **$417.6K** | **$0.554** | **50%** | ENTRENCHED (4/5) + **Figma #2** |
| 13b | ↳ eyedropper online | photoaid.com/en/tools/eyedropper | 2.7K | $1.9K | **$0.704** | **75%** | wins 1 synonym |
| 14 | color palette generator | coolors.co | 975.2K | $331.3K | $0.340 | 40% | **UMBRELLA** — no crack for standalone |

| 15 | color palette from image | coolors.co/image-picker | 40.2K | $12.3K | $0.306 | **71%** | **UMBRELLA** — coolors takes all 5 |

| 16 | hex to rgb | htmlcolorcodes.com/hex-to-rgb | 22.4K | $1.5K | **$0.067** | — | **UMBRELLA** — Google widget kills standalone |
| 18 | merge images | pinetools.com/merge-images | **204.3K** | $30.7K | $0.150 | **12%** | ENTRENCHED (5/5) · **India 76%** |
| 17 | image color changer | lunapic.com (replace-color) | 2.8K | $995 | $0.355 | 52% | **UMBRELLA — cluster too small** |
| 17b | ↳ recolor image | fotor.com/features/recolor-image | 1.8K | $792 | **$0.44** | **74%** | — |

### 17. Image color changer — UMBRELLA (fails on size, not competition)

Combined cluster traffic **~4.6K**. Volumes: recolor image 1.8K · color replacer 900 ·
replace color in image 900 · color replacement tool 800 · replace color online free 600.

$/visit is genuinely good ($0.355 / $0.44) and fotor is 74% tier-1 — but 4.6K visits at that
rate is **~$20–40/month**. Fold into the image-colour tool with seed 13.

Both incumbents are subpages of larger editors (LunaPic, Fotor), both flat-to-declining. No
dedicated site exists — an opening under the "dedicated beats umbrella" rule, but the prize
is too small to act on.

**Unresolved:** neither site holds #1 on the main terms (lunapic #2/#2/#3/#5/#3; fotor #2/#2,
#1 only on 250- and 90-volume terms). Something else owns the top slot — possibly Canva/Adobe
or an AI Overview. Does not change the verdict.

**vs ChatGPT research:** it rated Image Color Replacer #2 in the Image category, "🟢 Validated
and worth serious consideration." Actual: ~5K cluster, sub-3K incumbents, declining.
| 16b | ↳ color converter | w3schools.com/colors/colors_converter | 3.3K | $227 | $0.069 | 46% | #13 for hex to rgb 9.9K |

## URL / SEO BLOCK — highest-value territory found

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 21 | redirect checker | **wheregoes.com** | 22.2K | $24.6K | **$1.108** | **61%** | FRAGMENTED, small incumbents |
| 21b | ↳ | redirect-checker.org | 29.8K | $21.5K | **$0.721** | 31% | — |
| 22 | http status checker | httpstatus.io | **9.5K** | (hidden by tooltip) | — | 43% | **UMBRELLA — fold into 21** |
| **34** | **website down checker** ← NEW | isitdownrightnow.com | **161.3K** | $132.2K | **$0.820** | **57%** | **ADD TO LIST** |
| 23 | url encoder / decoder | **meyerweb.com/eric/tools/dencoder** | 68.5K ↗ | $75K | **$1.095** | 28% | STRONG — ancient page, growing |
| 23b | ↳ | urlencoder.org | 10.2K | $5.7K | $0.559 | 42% | — |
| 24 | website legitimacy checker | urlvoid.com | 81K | $45.9K | $0.567 | 55% | **LARGEST URL CLUSTER (~55K)** |
| 24b | ↳ | **scamwise.com** | **60K ↗** | $33.6K | $0.560 | 58% | **0 → 60K in 2 months** |
| 24c | ↳ | ssltrust.com/ssl-tools/website-security-check | 8.6K ↗ | $8.6K | **$1.00** | **100% US** | purest geo in dataset |

### 24. Website legitimacy checker — biggest cluster + proven fresh entry

**Live entry #4, and the fastest yet.** `scamwise.com` was flat at ~0 until June and hit
**60K by August**, taking #1 on website legit checker 6.9K · scam website checker 3K ·
scam checker 2.8K · website scam checker 1.4K.

**Cluster ~55K+ US volume** — 5x redirect checker:
website checker 17K · website safety checker 9K · website legit checker 6.9K ·
is this website safe 6.1K · is this site safe 4K · scam website checker 3K ·
site checker 2.9K · scam checker 2.8K · check website safety 1.9K ·
how to check if a website is legit 1.8K.

`ssltrust.com` is a notable outlier: **$1.00/visit at 100% US traffic** — purest tier-1
profile measured anywhere in this research.

**Risks:**

1. **Google ranks its own Safe Browsing #1** for `website checker` (17K). The head term
   belongs to Google.
2. **YMYL-adjacent.** The original brief excluded E-E-A-T-heavy topics, and "is this site
   safe" is advice people act on financially. ScamAdviser and URLVoid back verdicts with
   years of reputation data; a new entrant asserting safety judgements carries quality risk.

Counterweight: scamwise entered this exact SERP two months ago and took 60K.

### 23. URL encoder/decoder — STRONG

`meyerweb.com/eric/tools/dencoder` — Eric Meyer's personal CSS blog, an ancient minimal tool
page. **68.5K organic, $1.095/visit, growing 60K → 80K.** High domain authority, relic page.
Same shape as the CodePen finding at seed 11, but larger.

India cluster: url decoder 6.8K #1 · url decode 3.2K #1 · decode url 2.7K #1 ·
url decode online 1.7K #1 · url encoder 1.5K #1.

**Google's panel does NOT kill this.** The `percent encoding` SERP shows a "Common Examples"
box (Space→%20, Ampersand→%26) — but that answers the *reference* question and cannot encode
*your* string. Unlike `hex to rgb`, where Google's picker fully substituted for the tool, the
tool intent survives. Wikipedia, MDN, url-encode-decode.com, W3Schools all rank below.

> **Refinement: tier-1 is a proxy, not the driver.** meyerweb is only **28% tier-1** yet
> earns **$1.095/visit** — matching wheregoes at 61%. Dev-tool advertisers bid for Indian
> developers too. **"Who bids on this query" beats geo as the predictor.** Demote the tier-1
> correlation from rule to rough indicator.

*(Ignore `url encoder uploadarticle.com` 9.5K in the urlencoder.org panel — parasite/spam
artifact, not real demand.)*

### 22. HTTP status checker — UMBRELLA, but it surfaced a new candidate

`httpstatus.io` is small: **9.5K organic**, declining 14K → 10.5K. Cluster is thin —
url status 600 · http checker 500 · response checker 450 · bulk url checker 200 · brand 150.
~2–3K US volume. Folds into the redirect-checker site, as the ChatGPT research suspected.

*(Traffic value obscured by the UR tooltip in the capture; $/visit not computed.)*

### 34. Website down checker — NEW CANDIDATE, not in the original 33

`isitdownrightnow.com` — **161.3K organic, $132.2K value, $0.820/visit, 57% tier-1**
(US 31 · UK 13 · CA 8 · India 7 · AU 5).

US, all #1: is it down right now 9.4K · is this website down 5K · website down 4.8K ·
is this site down 4K · isitdownrightnow 3.6K (brand). **~27K US volume.**

- **2nd-highest $/visit measured**, on a cluster 3x larger than redirect checker
- **Incumbent declining hard: 220K → 165K over five months**
- Brand moat only 3.6K — small
- Sits inside the Website/URL category already being researched

**Added as seed 34.** Note the audience differs from redirect checker (consumer "is the site
broken?" vs SEO "audit my redirects"), so it is a separate site rather than a feature.

**Seed 34 confirmed (full synonym pass):** `isitdownrightnow.com` holds **all five at #1** —
is it down right now 9.4K · is this website down 5K · website down 4.8K · is this site down
4K · isitdownrightnow 3.6K (brand). US 31 · UK 13 · CA 8 · India 7 · AU 5 = **57% tier-1**.

Entrenched, but **declining 220K → 165K (−25% in five months)** with only a 3.6K brand moat.
An entrenched incumbent losing a quarter of its traffic is a different proposition from a
flat, defended one.

### 21. Redirect checker — BEST $/VISIT IN THE DATASET

`wheregoes.com` is the first site over **$1.00/visit**, on only 22.2K traffic.
US 54 · India 12 · UK 4 · Indonesia 3 · CA 3 = **61% tier-1**.
US keywords: wheregoes 1K #1 (brand) · link finder 1.3K #1 · redirect chain 800 #1 ·
reverse link search 600 #1 · where does this link go 400 #1.

`redirect-checker.org`: redirect checker 2.3K #1 · check redirect 800 #1 · redirect check
800 #1 · redirect test 600 #1 · 301 redirect checker 500 #1.

> ### MECHANISM: not "professional tools" — *who bids on the query*
>
> My earlier guess ("PDF/dev tools pay more") was wrong for PDF and right here. The variable
> is advertiser LTV:
>
> - `redirect checker` → Semrush, Ahrefs, Screaming Frog, Moz. SaaS, huge LTV, $10–50 CPC.
> - `split pdf` → nobody. Every PDF product is free.
> - `gamepad tester` → nobody. $0.01 CPC.
>
> **Ask "which company would pay to reach this searcher?" before anything else.**

> ### EFFICIENCY: small traffic, large revenue
>
> | | $/visit | Traffic needed for same revenue |
> |---|---:|---:|
> | wheregoes (redirect checker) | $1.108 | **1x** |
> | webcam test | $0.294 | 3.8x |
> | split pdf | $0.104 | 10.7x |
> | dead pixel test | $0.0596 | **18.6x** |
>
> wheregoes earns an est. **₹30–47k/mo on 22.2K visits**. displaytech.org needed **100.6K
> visits to make ₹10k**. For a new site, reaching 20–30K is vastly more achievable than 500K.
>
> **Rank the final shortlist by $/visit, not traffic.**

## SVG & ICONS BLOCK

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 26 | svg viewer | svgviewer.dev | 54.6K | $27.7K | **$0.507** | 25% | ENTRENCHED (5/5), small incumbent |
| 27 | svg optimizer | 4-way split, all tiny | 9.7K / 3.4K / 2.7K / 396 | $2.4K / $1.4K / $1.1K / $209 | $0.247–$0.528 | 20–51% | **UMBRELLA — fold into 26** |
| 28 | svg to png | **svgtopng.com** (EMD) | 201.5K ↓ | $31.4K | $0.156 | ~18% | EMD wins outright, declining 23% |

### 28. SVG to PNG — big traffic, commodity economics

`svgtopng.com` holds svg to png 38K #1 · svg to png converter 3K #1 · png svg 400 #1 ·
svgtopng 150 #1 · convert svg to png 8.3K #2. **201.5K organic** — 3.7x the SVG viewer.

But **$0.156/visit**, US 13%, **declining 260K → 200K (−23%)**. Converter economics: big
volume, commodity intent, minimal advertiser interest. Same shape as merge images and split pdf.

> ### EMD SCOREBOARD — now 2–2
>
> | Seed | EMD present | Outcome |
> |---|---|---|
> | gamepad tester | 3 EMDs | **lost** to hardwaretester.com |
> | refresh rate test | 9 EMDs | **lost** to testufo.com |
> | keyboard tester | keyboardchecker.com | **won** its own term |
> | svg to png | svgtopng.com | **won** the whole cluster |
>
> **Fitted pattern:** EMDs win where the query *is* the transformation (`svg to png`,
> `keyboard checker`) and lose where the query names a category someone branded better
> (`gamepad tester` → hardwaretester).

| 29 | favicon generator | favicon.io | 118.9K | $48.5K | $0.408 | 21% | **FRAGMENTED** |
| 29b | ↳ | realfavicongenerator.net | 93K **↑67%** | $40.2K | $0.432 | 19% | live mover #5 |

### 29. Favicon generator — FRAGMENTED, solid mid-tier standalone

Neither site owns the cluster. favicon.io holds favicon.ico 11K #1 · favicon maker 1.3K #1 ·
create favicon 900 #1, but sits **#2** for favicon 22K and favicon generator 8.1K.
realfavicongenerator holds favicon generator 11K #1 (India) but is **#5** on favicon.ico and
**#6** on favicon. Same split shape as keyboard and mouse.

**Cluster ~45K US volume.** realfavicongenerator **grew 67%** Apr→Aug (60K → 100K) — fifth
live mover caught in this research.

Downside: **tier-1 only 19–21%**, so $/visit is $0.43 rather than the $1.00+ of the URL block.
Bigger traffic, cheaper traffic.

Ranks above device / PDF / fonts; below all four URL seeds.

### SVG BLOCK RESOLVES TO ONE SITE (26–28)

Primary = **svg viewer** ($0.507/visit, best economics, most defensible). Features: PNG
conversion (201.5K traffic but $0.156) and optimizer (~16K). Combined traffic-value pool ~$64K.

### 27. SVG optimizer — UMBRELLA (smallest cluster in the run)

| Site | Organic | $/visit | Tier-1 | Owns |
|---|---:|---:|---:|---|
| svgomg.net | 9.7K | $0.247 | ~21% | svg optimizer 600 #1 · optimize svg 90 #1 |
| iloveimg.com/compress-svg | 3.4K | $0.412 | 20% | svg compressor 1K #1 (India) |
| vecta.io/nano | 2.7K | $0.407 | 42% | svg compressor 800 #1 (US) |
| svgminify.com | 396 | $0.528 | 51% | svg minifier 100 #1 |

~16K combined traffic on a **~3–4K US volume** cluster. Fragmented four ways, but winning
100% of it pays **₹4–7k/mo** — below the bar even at total victory.

> **Validates the autocomplete metric.** This was flagged at `verbatim=35` — thinnest of all
> 33 seeds — before any traffic data existed. It is indeed the smallest cluster in the run.

Folds into seed 26: svgviewer.dev already ships an optimizer beside its viewer. Same file,
same drop zone, same developer.

### 26. SVG viewer — solid mid-tier

`svgviewer.dev` holds all five: svg viewer 5.3K · svg editor 3.6K · svg editor online 1.2K ·
svg viewer online 1.1K · online svg editor 700 (India volumes). ~12K cluster. Flat/slight growth.

**$0.507/visit at only 25% tier-1** — third confirmation that the advertiser pool beats geo
(meyerweb 28% → $1.095; svgviewer 25% → $0.507). Dev tools pay regardless of where the
developer sits.

Softer incumbent than MyFonts or iLovePDF — 54.6K, no giant, no brand moat in top keywords.
But one site holds the whole cluster, which is worse than the URL block's 2- and 3-way splits.

Ranks above everything in device and PDF; below all four URL seeds.

## YOUTUBE BLOCK

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 30 | youtube transcript | youtubetotranscript.com | **495.1K ↑** | $93.3K | **$0.188** | 17% | 2 large growing incumbents |
| 30b | ↳ | youtube-transcript.io | 194.1K ↑ | $34.1K | $0.176 | 17% | — |
| 31 | youtube thumbnail downloader | youtube-thumbnail-grabber.com | **481.5K** | $91.9K | $0.191 | **7%** | **worst geo in run** |
| 31b | ↳ | youtubethumbnaildownloader.com | 190.3K | $18.8K | **$0.099** | 7% | Pakistan 66% |
| 31c | ↳ | get-youtube-thumbnail.com | 6.7K | $2K | $0.299 | 23% | Vietnam 27% |

### 31. YouTube thumbnail downloader — UMBRELLA, worst geo economics

Tier-1 **7%**. `youtubethumbnaildownloader.com` pulls 190.3K visits worth only $18.8K
($0.099/visit, third-lowest measured). The 481.5K leader earns an est. **₹16–33k/mo** on half
a million visits.

South Asian cluster is huge — youtube thumbnail download 113K · thumbnail downloader 85K ·
youtube thumbnail downloader 79K · thumbnail download 75K · yt thumbnail downloader 31K.

> **Reconciles a discrepancy in this research.** The autocomplete pass flagged this at
> `verbatim=14` and called it single-keyword. That was `gl=us` autocomplete and it was
> **correct about the US** — the 400K+ volume is India/Pakistan phrasings. Thin in the US,
> enormous in South Asia. Both readings true of different markets.

**Fourth ChatGPT top-pick contradicted** (rated 9.0/10).

| 32 | youtube thumbnail tester | testmythumbnails.com | 5.4K ↑ | $1.7K | **$0.315** | 41% | **UMBRELLA — cluster ~4.6K** |
| 32b | ↳ | thumbnailpreview.com | 1.9K ↓ | $453 | $0.238 | 43% | #2/#3 on everything |
| 33 | youtube tag generator | not measured | — | — | — | — | **UMBRELLA** — not building; vidIQ/TubeBuddy/RapidTags own it |

### 32. YouTube thumbnail tester — UMBRELLA (best YouTube economics, tiny cluster)

`testmythumbnails.com` holds all five at #1: thumbnail preview 2K · thumbnail tester 1K ·
thumbnail checker 900 · thumbnail viewer 350 · test my thumbnail 350. `thumbnailpreview.com`
sits #2/#3 on the same terms and is declining.

**Cluster ~4.6K. Combined traffic 7.3K.** Even total victory pays ~₹2–4k/mo.

> **Partial hit on the prediction.** I expected this to be the one YouTube seed above $0.40
> because it targets creators (who vidIQ/TubeBuddy bid on) rather than viewers. It came in at
> **$0.315 and 41% tier-1** — best in the YouTube block by a wide margin ($0.099–$0.191
> elsewhere), but short of $0.40. Right about the mechanism, wrong about the magnitude.

### YOUTUBE BLOCK VERDICT: no builds

| Seed | $/visit | Tier-1 |
|---|---:|---:|
| 32 thumbnail tester | $0.315 | 41% |
| 30 transcript | $0.188 | 17% |
| 31 thumbnail downloader | $0.099–0.191 | **7%** |

Largest clusters in the research, worst geo, lowest per-visit value. Seeds 30 and 31 have
big *growing* incumbents; seed 32's cluster is too small to matter.

### 30. YouTube transcript — huge cluster, device-block economics

Cluster ≈ **370K India volume**: youtube to transcript 153K · youtube transcript 121K ·
yt transcript 43K · youtube transcript generator 30K · youtube video transcript 22K.

**$0.188/visit at 17% tier-1** (India 44 · US 17 · Pakistan 9). Both incumbents **growing**.

To match what `wheregoes.com` earns from 22.2K visits you would need ~**131K transcript
visits**, while fighting two rising incumbents.

> **Third ChatGPT top-pick contradicted.** It rated this **9.5/10, "the strongest validated
> opportunity."** Its traffic figures were accurate; per-visit value was never checked.

> ### CONFIRMED: cluster size and $/visit are inversely related
>
> | Cluster | Size | $/visit |
> |---|---:|---:|
> | split pdf | 563K | $0.104 |
> | youtube transcript | ~370K | $0.188 |
> | font identifier | ~350K | $0.106 |
> | website legit | ~55K | $0.56–1.00 |
> | **redirect checker** | **~10K** | **$1.108** |
>
> Big clusters attract consolidators and serve broad consumer audiences advertisers do not
> pay for. Small high-value clusters serve professionals and go unnoticed.

## FONTS BLOCK

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 25 | font identifier | **myfonts.com/pages/whatthefont** | **2.3M ↑↑** | $244.4K | **$0.106** | ~22% | **ENTRENCHED — 144K brand moat** |
| 25b | ↳ | fontsquirrel.com/matcherator | 267K ↓ | $35.2K | $0.132 | 30% | declining 33% |

### 25. Font identifier — biggest cluster, clearest reject

**Cluster ~350K US volume** — largest measured: what the font 123K · font finder 78K ·
what font is this 52K · font identifier 43K · whatthefont 21K · font finder by image 15K ·
font detector 13K · font matcher 4.7K.

Everything else is wrong:

1. **$0.106/visit** — device-block economics. Font curiosity is not commercial intent.
   MyFonts monetises by *selling fonts*, not ads.
2. **MyFonts holds #1 on all five** and roughly **doubled Apr→Jul (1.2M → 2.6M)** while
   Fontsquirrel fell 33% (450K → 300K). Monotype is consolidating this actively.
3. **Brand moat 144K/mo** (`what the font` 123K + `whatthefont` 21K) — second only to iLovePDF.
4. **Hardest build in the list** — font recognition needs a real ML model.

> **Sharpest disagreement with the ChatGPT research in the whole run.** It called Font
> Identifier "⭐ My #1 opportunity … VALIDATED … Best opportunity in this category."
>
> Actual: 35x larger cluster than redirect checker, **10x lower value per visit**, entrenched
> Monotype property doubling its lead, 144K brand moat, highest technical cost.

## PDF BLOCK

| # | Seed | Incumbent | Organic | Traffic value | $/visit | Tier-1 | Pattern |
|---|---|---|---:|---:|---:|---:|---|
| 19 | extract pages from pdf | smallpdf.com/extract-pdf-pages (#2) | 57.4K | $5K | **$0.087** | **11%** | **SUITE LOCK — Adobe + iLovePDF + Smallpdf** |
| 20 | split pdf | ilovepdf.com/split_pdf | **1.8M** | $186.4K | $0.104 | **4%** | **UMBRELLA — 8.7M brand moat** |

### 20. Split PDF — UMBRELLA (largest moat + worst geo in the dataset)

`ilovepdf.com/split_pdf` is #1 on all five: split pdf 563K · i love pdf **8.7M** ·
ilovepdf 2.8M · pdf split 94K · split pdf online 91K (India volumes).

- **Brand moat: `i love pdf` = 8.7M/mo.** 290x coolors' 30K. Unassailable.
- **Tier-1 geo: 4%** (India 53 · Indonesia 8 · Malaysia 6 · US 4 · Philippines 3). Lowest measured.
- **$0.104/visit** on 1.8M organic.

> Cleanest illustration of volume ≠ value in the whole run: **1.8M visits here is worth less
> than 500K visits on the colour picker.**

### PDF BLOCK VERDICT: both seeds umbrella

Suite-locked by Adobe / iLovePDF / Smallpdf, strongest brand moat measured, worst geo
economics ($0.087 and $0.104/visit at 11% and 4% tier-1). Ship as features if a document
tool ever gets built; do not target as a standalone site.

### 19. Extract pages from PDF — UMBRELLA (suite lock + poor economics)

Smallpdf is **#2 on all five**; Adobe and iLovePDF hold the rest of the top 3.
extract pages from pdf 39K · extract pdf 15K · pdf page extractor 11K · pdf extract 9.4K ·
pdf extractor 6.6K (India volumes).

**India 58% / US 11%, $0.087/visit** — same bracket as gamepad tester.

> **Prediction disconfirmed.** I expected PDF to sit in the high-value B2B bracket with
> colours. It does not. PDF tools are free commodities used largely by students and office
> workers in developing markets; advertisers barely bid.

> ### KEY SYNTHESIS: tier-1 geo share predicts $/visit better than category
>
> | Seed | Tier-1 | $/visit |
> |---|---:|---:|
> | eyedropper (photoaid) | 75% | $0.704 |
> | image color picker | 50% | $0.554 |
> | recolor image (fotor) | 74% | $0.44 |
> | color palette generator | 40% | $0.340 |
> | webcam test | 40% | $0.294 |
> | merge images | 12% | $0.150 |
> | microphone test | 27% | $0.135 |
> | extract pdf | 11% | $0.087 |
> | dead pixel test | 16% | $0.0596 |
>
> **Read the country panel first.** It tells you what the traffic is worth before any other
> analysis. High India/SEA skew = low ad value, regardless of how "professional" the tool
> sounds.

### 18. Merge images — ENTRENCHED, India-heavy

`pinetools.com/merge-images` holds **#1 on all five**: merge images 65K · image merge 27K ·
photo merge 26K · photo merge online 8.6K · merge image 6.9K (India volumes).

204.3K organic but **India 76% / US 10%** — the most extreme geo skew in the dataset.
$0.150/visit. Blended RPM ~$0.6–1.2 → **₹10–21k/mo**, barely clearing the bar on 204K traffic.

> **Two corrections this seed forces:**
> 1. My Bing scrape predicted iLovePDF / Smallpdf / PDF24 / Adobe would hold this SERP.
>    **Wrong** — a small multi-tool site owns all five. Google data ≠ Bing data, again.
> 2. `pinetools.com` is a **multi-tool umbrella site winning outright**. That is a
>    counter-example to the "dedicated beats umbrella" rule from the device block. The rule
>    is a tendency, not a law.

### 16. Hex to RGB — UMBRELLA: Google answers it inline

**Google shows its own Color Picker widget above the fold** for `rgb to hex` — HEX, RGB,
CMYK, HSV, HSL, with a copy button. Zero reason to click a result.

That explains every number: $0.067/visit (device-tier, despite being a "design" query);
w3schools at **#13** for `hex to rgb` 9.9K pulling only 3.3K total; the whole cluster
generating a fraction of what its volume implies.

> ### NEW SIGNAL: Google's own widget = zero-click = volume is a lie
>
> Ahrefs reports search volume, **not clickable volume**. When Google answers inline, a 9.9K
> keyword may send a few hundred clicks to the entire SERP.
>
> **Check every remaining seed for a Google widget / answer box / AI Overview before
> trusting its volume.** Likely candidates in the remaining list: anything Google can compute
> or render itself — conversions, encoders, simple lookups.

### COLOR BLOCK RESOLVES TO ONE WEBSITE (seeds 13–17)

Primary = **image color picker** (best $/visit in the dataset, $0.554, and the only one with
a crack in the incumbent). The rest ship as features on the same site:

| Feature | Seed | Why not standalone |
|---|---|---|
| **Image colour picker** (primary) | 13 | — |
| Palette generator | 14 | coolors #1 on all 5 + Canva/Figma #2–3 + 30K brand moat |
| Palette from image | 15 | coolors takes all 5 |
| HEX/RGB/HSL converter | 16 | Google widget answers inline, zero-click |
| Colour replacer | 17 | cluster only ~4.6K traffic |

All five cost almost nothing to add once the picker exists — same canvas, same audience.
None can carry a domain alone.

### 15. Color palette from image — UMBRELLA

Coolors wins all five synonyms via its `/image-picker` subpage. UK 43% · US 28% = 71% tier-1,
growing. UK panel: colour palette generator 14K #1 · coolors 7.7K #1 · colour palette from
image 400 #1 · colour picker from image 6.3K **#6**.

**Colour block splits cleanly:** picking a colour from an image → `imagecolorpicker.com`;
generating palettes → `coolors.co`; everything above them → Figma, Canva.

> **Gap in `synonym-groups.md`: no British spellings.** `colour` variants are a distinct
> cluster Google treats separately — `colour palette generator` is 14K in the UK alone, and
> coolors is harvesting them quietly. Add `colour` variants for every colour-related seed.

### 14. Color palette generator — UMBRELLA

`coolors.co` holds **#1 on all 5 synonyms**, with **Canva and Figma alternating #2/#3**.
US: color palette generator 81K #1 · color palette 177K #1 · coolors 30K #1 ·
color generator 25K #1 · color 174K #1.

Economics are fine ($0.340/visit, 40% tier-1, ~$4,000–7,800/mo at #1). They are simply not
reachable: every slot above #4 is held by an entrenched specialist or a billion-dollar company.

Contrast seed 13 — also entrenched, but only Figma at #2, and `photoaid.com` had actually
taken a synonym. Cracks existed there. Here there are none.

> **New signal: brand-name search volume = moat.** `coolors` is itself a **30K/mo US keyword**.
> When the incumbent's brand name is a five-figure search term, users navigate to them by name
> rather than searching the generic term. No amount of better UX penetrates that.
> **Check brand-name volume for every entrenched incumbent from here on.**

> ### CATEGORY ECONOMICS: design traffic is 5–10x device traffic
>
> | Seed | Traffic value | $/visit |
> |---|---:|---:|
> | **image color picker** | **$417.6K** | **$0.554** |
> | webcam test (best device) | $150.7K | $0.294 |
> | microphone test | $94.6K | $0.135 |
> | gamepad tester | $39K | $0.088 |
> | dead pixel test | $6K | $0.0596 |
>
> Same build difficulty, an order of magnitude more money. Design/dev tools attract SaaS
> advertisers; gaming-hardware queries attract almost none.
>
> **Est. ad revenue for imagecolorpicker.com: $3,000–6,000/mo (₹2.5–5 lakh)** — 2–3x the
> webcam estimate on comparable traffic.
>
> US head terms: `color picker` **629K** #1 · `hex color picker` 75K #1 ·
> `color picker from image` 41K #1 · `color code finder` 13K #1 · `image color picker` 10K #1.
>
> **But competition is far stronger than the device block:** Figma sits at #2 for
> `image color picker`, and imagecolorpicker.com is entrenched across 4/5 synonyms with
> 753.6K behind it. Opposite of the CodePen-at-#1 situation in seed 11.
>
> **Implication: the 12-seed device block may be the worst category in the list.** Expect
> PDF / URL / SVG / fonts to sit in this higher bracket too — confirm as they come.

### Device block resolves to ~6 websites, not 12

- **webcam test** — standalone (best economics)
- **mouse tester** (+ touchscreen) — standalone, purchase-intent, affiliate path
- **microphone test** — standalone
- **audio test** = speaker + headphone + surround — one site
- **screen test** = monitor + dead pixel + refresh rate — one site
- **keyboard tester** — standalone, but weakest economics of the large clusters
- gamepad tester — standalone, deprioritised (entrenched, low $/visit, EMDs already failed)

| Seed | Organic | $/visit | Tier-1 |
|---|---:|---:|---:|
| webcam test | 511.8K | **$0.294** | **40%** |
| headphone test | 10.5K | $0.219 | 31% |
| speaker test | 88.8K | $0.148 | 48% |
| surround sound | 2.9K | $0.138 | **84%** |
| microphone test | 703.3K | $0.135 | 27% |
| monitor test | 27.2K | $0.118 | 11% |
| gamepad tester | 441.7K | $0.088 | 16% |
| dead pixel test | 100.6K | **$0.0596** | 16% |
| keyboard tester | 574.3K | $0.059 | 20% |
| 1 | gamepad tester | hardwaretester.com/gamepad | 441.7K | $39K | $0.088 | 16% | **ENTRENCHED** |
| 2 | keyboard tester | keyboardtester.com | 574.3K | $33.8K | **US-ENTRENCHED** (only 3 competitors) |

> **Check whether fragmentation is geographic before calling it fragmented.** Seed 2 looked
> fragmented across mixed-geo data. On the US SERP `key-test.ru` does not appear at all — it
> owns SEA, not the US. Same cluster, different verdict. Always confirm on `gl=us`.

> **Research geo must be US.** Google personalises by country. Searching from India surfaces
> India winners — `keyboardchecker.com` ranks #5 for `keyboard test` where `key-test.ru` holds
> #1. Use `&gl=us&hl=en&pws=0`, or read positions off the traffic checker's country panel.
>
> **Traffic ≠ revenue.** `key-test.ru` has 29% more traffic than `keyboardtester.com` and
> likely earns half, because no US in its top-5 countries. A competitor absent from the US is
> a *weak* competitor for an ads business — and an open door.

### 1. Gamepad tester — ENTRENCHED, low priority

`hardwaretester.com/gamepad` holds **position 1 on all 5 synonyms**. Traffic flat Apr–Aug.

| Keyword (US) | Vol | Pos |
|---|---:|---:|
| gamepad tester | 26K | 1 |
| controller tester | 21K | 1 |
| controller test | 5.1K | 1 |
| stick drift test | 3.9K | 1 |
| controller input test | 1.2K | 1 |

Countries: US 16% · Brazil 11% · India 9% · Indonesia 7% · Spain 6%.
Only 16% US → blended RPM ~$1–2 → **~$400–900/mo realistic ad revenue.**

**The finding that matters: exact-match domains are already here and losing.** The Bing SERP
shows `gamepad-tester.net`, `controllertest.io`, `controllertester.co` ranking *below* a
generic-brand site that owns the whole cluster. In this niche the EMD lever has already been
pulled by others and did not work. Displacing this needs a genuine product edge, not a domain.

Verdict: real demand, decent prize, **hardest possible competitive shape.** Not a first build.

### 2. Keyboard tester — FRAGMENTED, best shape so far

No site owns the cluster. Three split it, and each leaves the others' terms on the table.

| Site | Owns | Organic/mo | US share |
|---|---|---:|---:|
| keyboardtester.com | keyboard tester 74K #1 · keyboard test 17K #1 · key tester 5.1K #1 · keyboard checker 6.9K **#2** | 574.3K | 20% |
| en.key-test.ru | keyboard test 144K #1 · test keyboard 56K #1 · keytest 10K #1 (Indonesia) | 741.4K | **not top-5** |
| keyboardchecker.com | keytest 6.2K #1 · keyboard checker 6K #1 — but only **#5** for keyboard test 89K, **#6** for online keyboard test 46K | 117.9K | 12% |
| typequicker.com | n-key rollover 450 #1 · nkro test 70 #1 | 834 | 25% |

**Cluster is huge and nobody has consolidated it.** keyboardtester.com is #2 on
`keyboard checker`; keyboardchecker.com is #5–6 on the `keyboard test` variants. Those gaps
are the opening — one site covering tester + test + checker + key tester properly could take
more than any current incumbent holds.

NKRO is a rounding error (70/mo US) — cheap sub-feature, not a reason to build.

**US SERP re-check (gl=us) — revises the verdict.** Only three results: keyboardtester.com,
keyboardchecker.com, typequicker.com. **`key-test.ru` does not rank in the US at all** — its
741.4K is SEA traffic. The apparent fragmentation was geographic, not competitive.

In the US, keyboardtester.com holds 4 of 5 synonyms (#1/#1/#1/#2). That is near-entrenched.

Two positives survive:

1. **Only 3 competitors in the US** vs 10 for gamepad tester. Matches the "few strong
   competitors" criterion.
2. **The EMD won its own term.** `keyboardchecker.com` is #1 for `keyboard checker` (6.9K)
   while the much larger keyboardtester.com sits at #2 — the opposite of gamepad tester,
   where three EMDs all lost. **Evidence for the domain thesis, and it is mixed across seeds.
   Track this per seed.**

Verdict: better than gamepad on competitor count, worse on consolidation. Hold pending more
seeds — do not build first.

### 3. Webcam test — best economics so far, pattern incomplete

`webcamtests.com` — 511.8K organic, **$150.7K traffic value = $0.294/visit**, 3.3x gamepad
and 5x keyboard. Countries: India 31 · **US 31** · Philippines 8 · **UK 5** · **CA 4** —
40% tier-1, the best in the set.

Top keywords (India panel): webcam test 97K #1 · camera test 29K #1 · online camera test
8.5K #1 · online webcam test 8.1K #1 · webcam test online 6K #1.

Realistic ad revenue ~**$1,300–2,500/mo** — first seed where the economics justify a build.

**Still needed:** #1 result for the other 4 synonyms (`camera test`, `webcam checker`,
`test my camera`, `webcam tester`), and US positions rather than the India panel.

### 4. Microphone test — ENTRENCHED (US-confirmed)

`mictests.com` — 703.3K organic, $94.6K value, **$0.135/visit**. US 27 · India 19 ·
Philippines 13 · Pakistan 5 · Indonesia 5.

US panel, all position 1: mic test 100K · microphone test 37K · test microphone 14K ·
mic tester 11K · test my microphone 5K. Complete cluster ownership.

Traffic peaked ~850K in May, drifting to ~780K. Mild decline.

**Seeds 3 and 4 are separate clusters** — webcam went to `webcamtests.com`, mic to
`mictests.com`. Neither `onlinemictest.com` nor `webcammictest.com` won either. Two
websites, not one.

### 5. Speaker test — FRAGMENTED, small prize, video-dominated SERP

| Site | Organic | $/visit | Tier-1 | Owns |
|---|---:|---:|---:|---|
| onlinemictest.com/sound-test | 88.8K | $0.148 | **48%** (US 40 · CA 4 · AU 4) | sound test 30K #1 · test sound 4.2K #1 · speaker test 5K #1 (US) · audio tester 1.5K #1 · audio test 12K #2 |
| audiocheck.net/audiotests | 46.3K | $0.147 | 30% | speaker test 25K #1 (India) · left right speaker test 1K #1 · speaker test online 2.3K #3 · sound test 9.7K #4 · speaker check 7.1K #8 |

**Prize is ~5x smaller** than mic or webcam — 135K combined vs 703K / 512K.

**Geographic inversion:** onlinemictest holds `speaker test` #1 in the US (5K); audiocheck
holds it #1 in India (25K). India carries 5x the US volume on that term.

> ### New tracked signal: SERP shape
>
> **3 of 5 synonyms open with a YouTube carousel and no tool above the fold**
> (`speaker test`, `stereo test`, `left right speaker test`).
>
> - **Against:** a video block above the first organic result cuts organic CTR ~30–50%.
>   Position 1 here is worth materially less than position 1 on a clean SERP. Discount the
>   revenue model accordingly.
> - **For:** video ranking means Google has no satisfying *tool* answer — the weak-SERP
>   signal from the original brief. A browser tool beats a video for this job (click a
>   channel vs. sit through 1:47).
> - **Caution:** the #1 video is **8 years old** and still holding. That shape looks stable,
>   not transitional.
>
> **Record SERP shape for every remaining seed** — clean / video-topped / forum-topped.
> It changes achievable CTR more than position does.

### 6. Headphone test — UMBRELLA FEATURE, not a website

`webcammictest.com/headphones` owns **all five synonyms at #1** and earns only **10.5K
organic/mo**. Declining: 14K (Apr) → 10.5K (Aug).

Cluster volumes: headphone test 1.3K · headphone test online 1.3K · headset test 800 ·
headset test online 500 · earphone test 250. **~4K total.**

At 31% tier-1 and $0.219/visit: **complete domination pays ~$25–30/mo.** Below the cost of
the domain, never mind a month of build time.

`left right headphone test` is video-topped, then audiocheck.net, then webcammictest.

> **The lesson this seed teaches:** owning 100% of a 4K cluster is worth far less than
> placing 5th in a 500K one. Cluster size gates everything; position is secondary.

### Emerging cluster: seeds 5 + 6 (+ likely 7) = ONE audio-test website

Both `onlinemictest.com/sound-test` and `audiocheck.net` already span speaker, stereo, **and**
headphone terms — audiocheck takes the top organic slot on `left right headphone test` too.
Same tools, same audience, same hardware. Expect surround sound (7) to fold in as well.

> **Lead to chase: `webcamtests.com` + `mictests.com`.** Same naming construction, same
> niche, both single-purpose EMDs owning their entire cluster at #1. Likely one operator
> running a portfolio — i.e. this exact strategy, already working. Check shared footer,
> analytics ID, design system, registrar. If they match, **their full site list is a
> pre-validated build queue.**

### Two traps in these numbers

1. **Country.** Keyword lookups above were `country=us` and banded (`>10,000`). The traffic
   checker is **global**. US `>10,000` vs global 441.7K on one page — the US band hid an
   order of magnitude. Do not compare the two directly.
2. **Traffic value is not ad revenue.** It is what the traffic would cost to *buy* on Google
   Ads. Display ads pay roughly 1–2 orders of magnitude less. Divide, don't celebrate.

`verb` = autocomplete queries containing the seed phrase. It is an **ecosystem-breadth
proxy, not volume.** A tool can have one huge keyword and no variants — thumbnail
downloader looks like exactly that. Only Ahrefs settles it.

**Paste `data/ahrefs-core.txt` (6,013 kw) into Keywords Explorer, export, merge here.**

## The headline finding

**None of the 33 has an open SERP.** Every one is contested by dedicated tools. There is
no "nobody built this" option in this list. So the decision is not *find the empty niche*
— it is *find where volume justifies the fight*, which is the call your Ahrefs data makes,
not this file.

# ★★ SITE PLAN — 34 seeds → 19 websites, 19 months

## Operating thesis (operator, 2026-08-23)

> No seed is excluded. With an EMD, country-specific keywords, and the long-tail the leaders
> ignore, every cluster yields consistent revenue that compounds — **including the dominant
> ones** (coolors, iLovePDF, MyFonts). Build the most-probable-to-succeed first, then work
> down until all seeds are covered. One website per month.

**Scrap maths that justifies this:** `split pdf` is 563K volume. Taking **1%** = 5.6K visits.
`font identifier` is ~350K; 2% = 7K visits. At a ₹10k bar those are marginal alone — but they
are near-zero marginal cost once the site exists, and they compound as authority builds.

## The 19 websites

| Site | Primary (→ domain) | Seeds absorbed | Est. RPM | Leader traffic pool |
|---|---|---|---:|---:|
| **1. Redirect checker** | redirect checker (21) | 22 http status | **$16.62** | 29.8K + 22.2K |
| **2. URL encoder/decoder** | url encoder (23) | — | **$16.43** | 68.5K |
| **3. Website down checker** | website down (34) | — | **$12.30** | 161.3K |
| **4. Website legit checker** | website legit (24) | — | **$15.00** | 81K + 60K |
| **5. Image colour picker** | image color picker (13) | 14 palette gen · 15 palette-from-image · 16 hex/rgb · 17 colour changer | $10.56 | 753.6K + 975.2K |
| **6. Mouse tester** | mouse tester (11) | 12 touchscreen | $9.83 | 76.5K + 49K |
| **7. SVG tools** | svg viewer (26) | 27 optimizer · 28 svg→png | $7.61 | 54.6K + 201.5K |
| **8. Favicon generator** | favicon generator (29) | — | $6.48 | 118.9K + 93K |
| **9. Webcam test** | webcam test (3) | — | $4.41 | 511.8K |
| **10. Refresh rate test** | refresh rate test (10) | — | $3.65 | 117.6K |
| **11. YouTube tools** | youtube transcript (30) | 31 thumbnail dl · 32 thumbnail tester · 33 tag generator | $2.82 | 495.1K |
| **12. Merge images** | merge images (18) | — | $2.25 | 204.3K |
| **13. Audio test** | speaker test (5) | 6 headphone · 7 surround | $2.22 | 88.8K + 46.3K |
| **14. Microphone test** | microphone test (4) | — | $2.02 | 703.3K |
| **15. Font identifier** | font identifier (25) | — | $1.98 | 2.3M |
| **16. Screen test** | dead pixel test (9) | 8 monitor test | $1.77 | 100.6K + 27.2K |
| **17. PDF page tools** | split pdf (20) | 19 extract pages | $1.56 | 1.8M |
| **18. Gamepad tester** | gamepad tester (1) | — | $1.32 | 441.7K |
| **19. Keyboard tester** | keyboard tester (2) | — | $0.88 | 574.3K |

**All 34 seeds accounted for.** 13 standalone, 6 umbrellas absorbing 15 secondary seeds.

## Build order — 19 months

### Phase 1 · Months 1–4 — URL block (highest RPM, softest incumbents)

| Mo | Site | Why first |
|---:|---|---|
| 1 | **Redirect checker** | Highest RPM. **Fragmented** — two small incumbents (22.2K / 29.8K), no giant, no brand moat. |
| 2 | **URL encoder/decoder** | RPM $16.43 and the incumbent is a **2005 personal-blog page**. Google's panel doesn't replace the tool. |
| 3 | **Website down checker** | Incumbent **declining −25% in 5 months**, brand moat only 3.6K, 57% tier-1. Easiest entrenched target. |
| 4 | **Website legit checker** | Biggest URL cluster (~55K) and `scamwise` proved entry **0→60K in 2 months**. Placed 4th not 3rd because of **YMYL risk** + Google Safe Browsing owning the head term. |

### Phase 2 · Months 5–8 — high-RPM tools

| Mo | Site | Why |
|---:|---|---|
| 5 | **Image colour picker** | Absorbs 5 seeds. Largest high-RPM pool in the set (753K + 975K). Figma at #2 is the catch. |
| 6 | **Mouse tester** | **A CodePen pen ranks #1** for `double click test` — weakest competitor found. Purchase-intent traffic + affiliate path. |
| 7 | **SVG tools** | Absorbs 3 seeds. Small incumbent (54.6K), no giant, no moat. |
| 8 | **Favicon generator** | **Fragmented** — best competitive shape in this phase. |

### Phase 3 · Months 9–14 — volume plays

| Mo | Site | Why |
|---:|---|---|
| 9 | **Webcam test** | Best device economics: $0.294, 40% tier-1, 511.8K pool. |
| 10 | **Refresh rate test** | $0.243, 117.6K. testufo is strong but single-site. |
| 11 | **YouTube tools** | Absorbs 4 seeds in one build — best seeds-per-month ratio in the plan. |
| 12 | **Merge images** | 204.3K pool. India-heavy, so revenue is thin per visit. |
| 13 | **Audio test** | Absorbs 3 seeds. Best geo in the research (48–84% tier-1) on a small base. |
| 14 | **Microphone test** | 703.3K pool, entrenched by mictests.com. Volume play. |

### Phase 4 · Months 15–19 — scraps of giant clusters

| Mo | Site | Why last |
|---:|---|---|
| 15 | **Screen test** | Absorbs 2 seeds. $0.0596–0.118 — near-worst economics. |
| 16 | **PDF page tools** | 1.8M pool but suite-locked and 4% tier-1. Pure scrap play: 2% of the cluster ≈ 36K visits. |
| 17 | **Gamepad tester** | 441.7K but $0.088 and 3 EMDs already failed here. |
| 18 | **Keyboard tester** | 574.3K, **worst $/visit in the set** ($0.059). Only 3 US competitors though. |
| 19 | **Font identifier** | 2.3M pool — but **needs an ML model**, the only build in the plan that isn't a canvas/fetch trick. Do it last, with 18 months of practice behind you. |

## Domain notes

Clean EMD `.com` is gone for nearly every primary. Use the **qualified-EMD** pattern that
compilefuture actually used (`realonlineruler.com`, `fontfinderai.com`) — query phrase intact
plus one qualifier.

Confirmed **available** from the earlier RDAP sweep, relevant to this plan:
`httpstatuschecker.com` (site 1) · `urlencoderdecoder.com` (site 2) ·
`screenshotcolorpicker.com` / `imagecolorpicker.io` (site 5) · `viewsvg.com` /
`svginspector.com` (site 7) · `pdfpageextractor.com` (site 17) ·
`fontidentifierfromimage.com` / `fontfinderfromimage.com` (site 15) ·
`transcriptyoutube.com` (site 11).

**Re-check availability before each build** — these were measured 2026-08-22.

# ★ ALL-SEED RANKING TABLES

`Est. RPM = $/visit × 15` — derived heuristic, **not measured**. Calibrated against
wheregoes ($1.108 → ~$15–20 observed range), split pdf ($0.104 → ~$1.6), dead pixel
($0.0596 → ~$0.9).

## TABLE 1 — sorted by TRAFFIC (traffic leader in each cluster)

| # | Seed | Traffic leader | Organic/mo | Traffic value | $/visit | Tier-1 | Est. RPM |
|---:|---|---|---:|---:|---:|---:|---:|
| 25 | font identifier | myfonts.com/whatthefont | **2.3M** | $244.4K | $0.106 | 22% | $1.59 |
| 20 | split pdf | ilovepdf.com/split_pdf | **1.8M** | $186.4K | $0.104 | 4% | $1.56 |
| 14 | color palette generator | coolors.co | 975.2K | $331.3K | $0.340 | 40% | $5.10 |
| 13 | image color picker | imagecolorpicker.com | 753.6K | $417.6K | $0.554 | 50% | $8.31 |
| 2 | keyboard tester | en.key-test.ru | 741.4K | $40.3K | $0.054 | no US | $0.82 |
| 4 | microphone test | mictests.com | 703.3K | $94.6K | $0.135 | 27% | $2.02 |
| 3 | webcam test | webcamtests.com | 511.8K | $150.7K | $0.294 | 40% | $4.41 |
| 30 | youtube transcript | youtubetotranscript.com | 495.1K | $93.3K | $0.188 | 17% | $2.82 |
| 31 | yt thumbnail downloader | youtube-thumbnail-grabber.com | 481.5K | $91.9K | $0.191 | 7% | $2.87 |
| 1 | gamepad tester | hardwaretester.com/gamepad | 441.7K | $39K | $0.088 | 16% | $1.32 |
| 18 | merge images | pinetools.com/merge-images | 204.3K | $30.7K | $0.150 | 12% | $2.25 |
| 28 | svg to png | svgtopng.com | 201.5K | $31.4K | $0.156 | 18% | $2.34 |
| 34 | website down checker | isitdownrightnow.com | 161.3K | $132.2K | **$0.820** | 57% | **$12.30** |
| 29 | favicon generator | favicon.io | 118.9K | $48.5K | $0.408 | 21% | $6.12 |
| 10 | refresh rate test | testufo.com | 117.6K | $28.6K | $0.243 | 24% | $3.65 |
| 9 | dead pixel test | displaytech.org | 100.6K | $6K | $0.0596 | 16% | $0.89 |
| 5 | speaker test | onlinemictest.com/sound-test | 88.8K | $13.1K | $0.148 | 48% | $2.22 |
| 24 | website legit checker | urlvoid.com | 81K | $45.9K | $0.567 | 55% | $8.51 |
| 11 | mouse tester | onlinemictest.com/mouse-test | 76.5K | $11.3K | $0.148 | 10% | $2.22 |
| 23 | url encoder/decoder | meyerweb.com/dencoder | 68.5K | $75K | **$1.095** | 28% | **$16.43** |
| 19 | extract pages from pdf | smallpdf.com/extract-pdf-pages | 57.4K | $5K | $0.087 | 11% | $1.31 |
| 26 | svg viewer | svgviewer.dev | 54.6K | $27.7K | $0.507 | 25% | $7.61 |
| 15 | color palette from image | coolors.co/image-picker | 40.2K | $12.3K | $0.306 | 71% | $4.59 |
| 12 | touchscreen test | onlinemictest.com/touch-screen-test | 30.1K | $4.7K | $0.156 | 15% | $2.34 |
| 21 | redirect checker | redirect-checker.org | 29.8K | $21.5K | $0.721 | 31% | $10.82 |
| 8 | monitor test | eizo.be/monitor-test | 27.2K | $3.2K | $0.118 | 11% | $1.77 |
| 16 | hex to rgb | htmlcolorcodes.com/hex-to-rgb | 22.4K | $1.5K | $0.067 | — | $1.01 |
| 6 | headphone test | webcammictest.com/headphones | 10.5K | $2.3K | $0.219 | 31% | $3.29 |
| 27 | svg optimizer | svgomg.net | 9.7K | $2.4K | $0.247 | 21% | $3.71 |
| 22 | http status checker | httpstatus.io | 9.5K | *hidden* | — | 43% | — |
| 32 | yt thumbnail tester | testmythumbnails.com | 5.4K | $1.7K | $0.315 | 41% | $4.73 |
| 7 | surround sound test | soundtest.io/surround-sound-test | 2.9K | $401 | $0.138 | 84% | $2.07 |
| 17 | image color changer | lunapic.com/replace-color | 2.8K | $995 | $0.355 | 52% | $5.33 |
| 33 | youtube tag generator | *not measured* | — | — | — | — | — |

## TABLE 2 — sorted by RPM / $/visit (best-paying site in each cluster)

| Rank | # | Seed | Best-paying site | $/visit | Est. RPM | Its traffic | Tier-1 |
|---:|---:|---|---|---:|---:|---:|---:|
| 1 | 21 | **redirect checker** | wheregoes.com | **$1.108** | **$16.62** | 22.2K | 61% |
| 2 | 23 | **url encoder/decoder** | meyerweb.com/dencoder | **$1.095** | **$16.43** | 68.5K | 28% |
| 3 | 24 | **website legit checker** | ssltrust.com | **$1.00** | **$15.00** | 8.6K | **100%** |
| 4 | 34 | **website down checker** | isitdownrightnow.com | **$0.820** | **$12.30** | 161.3K | 57% |
| 5 | 13 | image color picker | photoaid.com/eyedropper | $0.704 | $10.56 | 2.7K | 75% |
| 6 | 11 | mouse tester | codepen.io (double click) | $0.655 | $9.83 | 13.9K | 13% |
| 7 | 27 | svg optimizer | svgminify.com ⚠ | $0.528 | $7.92 | **396** | 51% |
| 8 | 26 | svg viewer | svgviewer.dev | $0.507 | $7.61 | 54.6K | 25% |
| 9 | 17 | image color changer | fotor.com/recolor-image | $0.44 | $6.60 | 1.8K | 74% |
| 10 | 29 | favicon generator | realfavicongenerator.net | $0.432 | $6.48 | 93K | 19% |
| 11 | 14 | color palette generator | coolors.co | $0.340 | $5.10 | 975.2K | 40% |
| 12 | 32 | yt thumbnail tester | testmythumbnails.com | $0.315 | $4.73 | 5.4K | 41% |
| 13 | 15 | color palette from image | coolors.co/image-picker | $0.306 | $4.59 | 40.2K | 71% |
| 14 | 31 | yt thumbnail downloader | get-youtube-thumbnail.com ⚠ | $0.299 | $4.49 | 6.7K | 23% |
| 15 | 3 | webcam test | webcamtests.com | $0.294 | $4.41 | 511.8K | 40% |
| 16 | 10 | refresh rate test | testufo.com | $0.243 | $3.65 | 117.6K | 24% |
| 17 | 6 | headphone test | webcammictest.com | $0.219 | $3.29 | 10.5K | 31% |
| 18 | 30 | youtube transcript | youtubetotranscript.com | $0.188 | $2.82 | 495.1K | 17% |
| 19 | 12 | touchscreen test | onlinemictest.com | $0.156 | $2.34 | 30.1K | 15% |
| 20 | 28 | svg to png | svgtopng.com | $0.156 | $2.34 | 201.5K | 18% |
| 21 | 18 | merge images | pinetools.com | $0.150 | $2.25 | 204.3K | 12% |
| 22 | 5 | speaker test | onlinemictest.com/sound-test | $0.148 | $2.22 | 88.8K | 48% |
| 23 | 7 | surround sound test | soundtest.io | $0.138 | $2.07 | 2.9K | **84%** |
| 24 | 4 | microphone test | mictests.com | $0.135 | $2.02 | 703.3K | 27% |
| 25 | 25 | font identifier | fontsquirrel.com/matcherator | $0.132 | $1.98 | 267K | 30% |
| 26 | 8 | monitor test | eizo.be | $0.118 | $1.77 | 27.2K | 11% |
| 27 | 20 | split pdf | ilovepdf.com | $0.104 | $1.56 | 1.8M | 4% |
| 28 | 1 | gamepad tester | hardwaretester.com | $0.088 | $1.32 | 441.7K | 16% |
| 29 | 19 | extract pages from pdf | smallpdf.com | $0.087 | $1.31 | 57.4K | 11% |
| 30 | 16 | hex to rgb | w3schools.com | $0.069 | $1.04 | 3.3K | 46% |
| 31 | 9 | dead pixel test | displaytech.org | $0.0596 | $0.89 | 100.6K | 16% |
| 32 | 2 | keyboard tester | keyboardtester.com | $0.059 | $0.88 | 574.3K | 20% |
| — | 22 | http status checker | httpstatus.io | *hidden* | — | 9.5K | 43% |
| — | 33 | youtube tag generator | *not measured* | — | — | — | — |

⚠ **Small-sample warning.** `svgminify.com` (396 visits) and `get-youtube-thumbnail.com`
(6.7K) post high $/visit on tiny traffic — noisy. Their cluster leaders are far lower:
svg optimizer leader `svgomg.net` = $0.247; yt thumbnail leader = **$0.099–0.191**.

### What the two tables show together

The rankings are **almost inverted**. Top-10 by traffic contains only *one* seed from the
top-10 by RPM (13 image color picker). The four highest-RPM seeds — 21, 23, 24, 34 — rank
**25th, 20th, 18th and 13th** by traffic.

Biggest gaps:

| Seed | Traffic rank | RPM rank | Gap |
|---|---:|---:|---:|
| 21 redirect checker | 25th | **1st** | +24 |
| 23 url encoder | 20th | **2nd** | +18 |
| 25 font identifier | **1st** | 25th | −24 |
| 20 split pdf | **2nd** | 27th | −25 |
| 2 keyboard tester | 5th | 32nd | −27 |

# ★ FINAL RANKED BUILD LIST — all 34 seeds complete

## The operating assumption (set by the operator, 2026-08-23)

> Nothing with high volume, good CPM and low competition exists any more — that combination
> is gone. So competition is not a kill criterion. Any seed whose SERP is not owned by a
> giant can plausibly reach **page 1 and ~10K visits/month inside year 1**, which covers the
> domain and lets authority compound.

**This inverts the ranking logic.** If traffic in year 1 is roughly fixed at a ~10K floor,
then traffic potential stops being the variable and **$/visit becomes the only thing that
decides whether year 1 pays for itself.**

### Revenue heuristic

`display RPM ≈ $/visit × 15` — calibrated against the per-seed estimates in this file
(wheregoes $1.108 → ~$15–20 RPM; dead pixel $0.0596 → ~$0.9; split pdf $0.104 → ~$1.6).
Rough, not measured. Then, at ₹85/$:

**Visits needed to clear ₹10,000/month ≈ 7,867 ÷ $/visit**

| Seed | $/visit | Visits needed for ₹10k/mo | Reachable in yr 1? |
|---|---:|---:|:--:|
| 21 redirect checker | $1.108 | **7.1K** | **yes** |
| 23 url encoder/decoder | $1.095 | **7.2K** | **yes** |
| 34 website down checker | $0.820 | **9.6K** | **yes** |
| 24 website legit (ssltrust tier) | $1.00 | **7.9K** | yes, w/ YMYL risk |
| 11 mouse tester (double-click) | $0.655 | 12K | likely |
| 13 image colour picker | $0.554 | 14.2K | likely |
| 26 svg viewer | $0.507 | 15.5K | likely |
| 29 favicon generator | $0.43 | 18.3K | maybe |
| 32 yt thumbnail tester | $0.315 | 25K | no — cluster only 4.6K |
| 3 webcam test | $0.294 | 26.8K | maybe |
| 30 youtube transcript | $0.188 | 41.8K | no |
| 28 svg to png | $0.156 | 50K | no |
| 4 microphone test | $0.135 | 58K | no |
| 20 split pdf | $0.104 | 75.6K | no |
| 31 yt thumbnail downloader | $0.099 | 79.5K | no |
| 9 dead pixel test | $0.0596 | 132K | no |

**At a 10K floor, only the URL block pays for itself in year 1.** Everything else needs
2x–13x the floor before it clears ₹10k.

---

## TIER 1 — BUILD THESE (URL / SEO block)

All four: no giant in the SERP, no meaningful brand moat, small incumbents, highest $/visit
measured, and 43–61% tier-1 geo.

| # | Site | Primary keyword | $/visit | Incumbent | Why now |
|---:|---|---|---:|---|---|
| 1 | **Redirect checker** | redirect checker 2.3K | **$1.108** | wheregoes 22.2K · redirect-checker.org 29.8K | **Fragmented**, both incumbents small, no moat. Absorbs seed 22 (http status) as a feature. |
| 2 | **URL encoder/decoder** | url decoder 6.8K | **$1.095** | meyerweb.com — a 2005 blog page | Incumbent is a relic on a personal site. Google's percent-encoding panel does **not** replace the tool. |
| 3 | **Website down checker** | is it down right now 9.4K | **$0.820** | isitdownrightnow 161.3K | Entrenched but **declining −25% in 5 months**, 3.6K brand moat only, 57% tier-1. |
| 4 | **Website legit checker** | website legit checker 6.9K | $0.56–**1.00** | urlvoid 81K · scamwise 60K | **Largest URL cluster (~55K)** + `scamwise` proved entry **0→60K in 2 months**. Risk: YMYL, Google Safe Browsing owns the head term. |

## TIER 2 — BUILD AFTER (need 12–18K visits to clear the bar)

| # | Site | $/visit | Note |
|---:|---|---:|---|
| 5 | **Mouse tester** (+ touchscreen) | $0.655 | **A CodePen pen ranks #1** for `double click test` — weakest competitor found anywhere. Purchase-intent traffic; Redragon monetises it via affiliate. Low tier-1 (10–19%). |
| 6 | **Image colour picker** (+ palette gen, palette-from-image, hex/rgb, colour changer) | $0.554 | Absorbs seeds 14–17. Huge pool (753K) and 50% tier-1, but Figma at #2 and imagecolorpicker.com entrenched. |
| 7 | **SVG viewer** (+ optimizer, svg→png) | $0.507 | Absorbs 27–28. Small incumbent (54.6K), no giant, no moat. |
| 8 | **Favicon generator** | $0.43 | **Fragmented** — best competitive shape in tier 2. realfavicongenerator growing 67%. Only 19–21% tier-1. |

## TIER 3 — DEVICE BLOCK (winnable, poor economics)

Resolves to ~5 sites: webcam · microphone · audio (speaker+headphone+surround) ·
screen (monitor+dead pixel+refresh rate) · keyboard. Best is webcam at $0.294 / 40% tier-1;
the rest sit at $0.06–0.15. All need 27K–132K visits to clear ₹10k.

## TIER 4 — DO NOT BUILD

| Seeds | Reason |
|---|---|
| 19, 20 PDF | Suite-locked (Adobe/iLovePDF/Smallpdf) · **8.7M brand moat** · 4–11% tier-1 |
| 25 fonts | 144K brand moat · MyFonts +117% · $0.106 · needs an ML model |
| 30, 31, 33 YouTube | 7–17% tier-1 · $0.099–0.191 · large *growing* incumbents |
| 14, 15 colour palette | coolors #1 on all 5 + Canva/Figma #2–3 + 30K brand moat |
| 16 hex to rgb | **Google widget answers inline** — zero-click |
| 18 merge images | India 76%, 12% tier-1 |
| 1 gamepad, 2 keyboard | $0.088 / $0.059 — lowest value at scale |

## Five live entries caught during this research

`soundtest.io` (0→2.9K, took #1 from xbitlabs in ~1 month) · `displaytech.org` (30K→100.6K) ·
`redragonshop.com` (0→45K in 2 months) · `scamwise.com` (0→60K in 2 months) ·
`realfavicongenerator.net` (+67%).

**All five moved inside 2–5 months.** That supports the operator's year-1 thesis — entry is
demonstrably fast in these niches — and suggests a 3–4 month checkpoint is more informative
than waiting the full 12.

---

## Phase B — competitor depth (survivors only, after all 33 pass Phase A)

Take the top 5 results per seed, traffic-check each, and plot the decay.

**The decay curve decides it, not the leader's traffic.** Both of these have a 500K leader
and mean opposite things:

| Deep market | | Winner-take-all | |
|---|---:|---|---:|
| #1 | 500K | #1 | 500K |
| #2 | 400K | #2 | 25K |
| #3 | 310K | #3 | 8K |
| #4 | 220K | #4 | 3K |
| #5 | 150K | #5 | 1K |

Left: position 4 pays rent — profitable without beating anyone. Right: below #1 earns nothing.

Given the model is one site/month held 12 months, taking #1 inside a year is unlikely. So the
question is **not** "can we beat the leader" but **"what does a realistic #3–#5 finish pay?"**
A shallow decay beats a big leader.

Per seed record: top-5 URLs, organic/mo each, $/visit each, and whether any is an EMD.

## Table

`ded` = dedicated competitors in top-10. `EMD?` = is the exact-match domain lever already
taken by a ranking competitor.

| Tool | Cat | verb | ded | EMD? | Competition read |
|---|---|---:|---:|:--:|---|
| split pdf | pdf | 461 | 0 | no | **Locked by suites** — iLovePDF, Smallpdf, PDF24, Adobe |
| youtube transcript | yt | 446 | 10 | yes | youtubetotranscript, notegpt, videotranscriber + 7 |
| color palette generator | color | 400 | 1 | no | **Locked** — Coolors, colorhunt, htmlcolorcodes, colorhexa |
| svg to png | svg | 359 | 4 | yes | freeconvert, svgtopng.com, cloudconvert, w3schools |
| speaker test | device | 346 | 8 | no | devicechecker.org, onlinemictest, soundtest.io |
| gamepad tester | device | 330 | 10 | yes | hardwaretester, gamepad-tester.net, controllertest.io |
| keyboard tester | device | 314 | 3 | yes | key-test.ru, keyboard-tester.com, keyboard-test.space |
| merge images | image | 284 | 2 | no | **Locked by suites** — iLovePDF, Smallpdf, PDF24, Adobe |
| webcam test | device | 251 | 9 | yes | webcamtests.com, webcam.org, webcammictest, onlinemictest |
| microphone test | device | 234 | 9 | yes | mictests.com, microphone-test.com, webcammictest |
| svg viewer | svg | 220 | 5 | yes | svgrepo, w3schools, svgviewer.dev |
| extract pages from pdf | pdf | 217 | 0 | no | **Locked** — Adobe, iLovePDF, pdf.net, Canva |
| surround sound test | device | 211 | 7 | no | xbitlabs, soundtest.io, fixmyspeakers, onlinesoundtest |
| font identifier | font | 206 | 8 | no | myfonts, fontsquirrel, fontspring, whatfontis |
| dead pixel test | device | 198 | 10 | yes | deadpixeltest.org, screentest.run, deadpixel.tools |
| monitor test | device | 196 | 10 | yes | eizo, screentester.io, display-test.app |
| hex to rgb | color | 180 | 6 | yes | rgbcolorcode, rapidtables, htmlcolorcodes, omnicalculator |
| favicon generator | svg | 170 | 9 | yes | favicon.io, favicongenerator.io, realfavicongenerator |
| mouse tester | device | 126 | 10 | yes | mousetester.net, testmouse.com, onlinemictest |
| refresh rate test | device | 116 | 9 | yes | 9 dedicated EMDs — screenhz, whatismyrefreshrate, fpstest |
| headphone test | device | 115 | 7 | no | webcammictest, soundtest.io, mictest.co, audiocheck |
| image color picker | color | 105 | 8 | yes | imagecolorpicker.com, redketchup, imgcolorpicker |
| youtube tag generator | yt | 93 | 10 | no | **vidIQ, keywordtool.io, rapidtags** + 7 more |
| redirect checker | url | 89 | 10 | yes | redirectchecker.io, redirect-checker.org, wheregoes |
| color palette from image | color | 89 | 9 | no | mdigi, icolorpalette, swatchery + Coolors/image-picker |
| url encoder | url | 53 | 7 | yes | urlencoder.org, urldecoder.org, urlencoder.io |
| touchscreen test | device | 47 | 7 | yes | touchscreentest.org/.com, touchscreen-test.com |
| image color changer | image | 43 | 9 | yes | convertico, imagecolorchanger.com, nanoimage |
| is this website legit | url | 40 | 7 | yes | **ScamAdviser, URLVoid** + 5. Also trust/E-E-A-T risk |
| svg optimizer | svg | 35 | 5 | no | svgrepo, w3schools, svgviewer.dev (SVGOMG not in top-10) |
| youtube thumbnail tester | yt | 15 | 7 | yes | TubeBuddy + testmythumbnails, thumbnailtester.app + 4 |
| youtube thumbnail downloader | yt | 14 | 6 | yes | youtube-thumbnail-grabber, youtubethumbnaildownloader + 4 |
| http status checker | url | 10 | 6 | no | ipvoid, chemicloud, pemavor, devtoollab (mostly suites) |

## Category findings

### Device diagnostics is the most farmed category, not the least

This reverses the earlier read. Six established operators already run **multi-test umbrella
sites** — the exact model planned here:

`onlinemictest.com` (webcam, mic, mouse, touchscreen) · `xbitlabs.com` (refresh rate,
surround) · `soundtest.io` (speaker, headphone, surround) · `devicetests.com` ·
`checkadevice.com` · `hardwaretester.com` · `devicechecker.org` · `screentester.io`

`refresh rate test` alone has **nine** dedicated EMD micro-tools, several clearly recent.
Combined with the domain check — every device EMD `.com` already registered — this niche
is being actively carpet-bombed right now.

### The suite-locked ones are not winnable on intent

`split pdf`, `extract pages from pdf`, `merge images` return `ded=0` — but that is not an
open SERP, it is the opposite: iLovePDF / Smallpdf / PDF24 / Adobe hold every slot. A new
domain does not displace those.

### Thin-cluster group needs volume before any verdict

`http status checker` (10), `youtube thumbnail downloader` (14), `youtube thumbnail tester`
(15), `svg optimizer` (35), `is this website legit` (40). ChatGPT's research rated the
thumbnail downloader 9.0/10 and http status checker VALIDATED. Autocomplete says neither
phrase branches. **Flagged, not rejected** — one big keyword is a legitimate shape.

## Where the ChatGPT shortlist and this data disagree

| Idea | ChatGPT verdict | This data |
|---|---|---|
| youtube thumbnail downloader | 9.0/10 | cluster of 14; 6 dedicated EMD tools |
| http status checker | VALIDATED | cluster of 10 |
| color palette from image | promising sleeper | cluster of 89; Coolors already ships `/image-picker` |
| svg optimizer | strong opportunity | cluster of 35 |
| font identifier | #1, 9.x/10 | myfonts/fontspring/whatfontis hold it; Medium–Hard build |
| device diagnostics | (not in the 7 categories) | most contested category of all |

## Next step

1. Ahrefs bulk import `data/ahrefs-core.txt` → export volume + KD.
2. Merge. Standalone = real volume + KD you can beat + a qualified-EMD domain still free.
3. Everything else becomes a sub-feature of whichever survivor shares its audience.

## Reproduce

```
python cluster.py tools-seeds.txt data/tool-kw.jsonl   # clusters
python harvest.py serp data/tool-serp-q.txt data/tool-serp.jsonl
python score_tools.py                                   # table
python score_tools.py csv                               # Ahrefs cuts
```

Known limit: Bing collapses any query containing "youtube" into a canned branded SERP, and
broad-matches multi-word technical phrases into dictionaries/Amazon. Ten queries failed
that way; they were resolved via WebSearch instead. `cov < 0.5` flags most but not all —
it measures topical match, not tool-ness.
