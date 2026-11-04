# Cross-linking the portfolio — decision

**Question:** should the 19 sites link to each other to pass SEO value?

**Answer: No, not as a link network. A narrow traffic-network version is allowed, under the
rules below.**

Researched 2026-08-24.

---

## Why the blanket version is a bad idea

Google's enforcement definition of a private blog network is:

> clusters of sites built **mainly to link to each other**, with shared ownership, thin
> content, and near-identical hosting footprints

That describes this portfolio's proposed cross-link scheme exactly. SpamBrain is specifically
tuned to find the interconnections, and detection keys on same IP ranges, same hosting, same
outbound link patterns, and repeated anchor text. The December 2024, August 2025 and October
2025 spam updates each expanded enforcement here.

**The killer:** *once one site in a network is flagged, the whole network usually follows.*
19 sites, 19 months of work, one correlated failure mode.

### This portfolio's footprint — updated 2026-08-25

Each site is built as a **separate standalone project**: its own design language, layout, page
structure and freshly written copy. Only the *method* is shared. That materially reduces the
network signature.

| Signal | Status |
|---|---|
| Design + layout + copy | ✅ **Different per site** — the strongest signal, and it is absent |
| Page structure | ✅ Different per site |
| Hosting | ⚠ All Cloudflare Pages, same IP ranges |
| Framework | ⚠ Astro + Tailwind throughout (a common stack; weak signal on its own) |
| Ownership | ⚠ **Same AdSense publisher ID** and same GSC account |
| Launch pattern | ⚠ Sequential, one per month |

**Common ownership is not a violation.** Shared AdSense and GSC accounts are not links and
are not link spam — plenty of legitimate operators run multiple sites.

What converts "same owner" (fine) into "link scheme" (not fine) is **the link pattern**. With
the design/content footprint gone, a uniform cross-link mesh becomes the *only* thing that
would make this look like a network. That is precisely why the policy below is zero-by-default.

### The reward is near zero anyway

Links from 18 brand-new, zero-authority domains pass almost nothing. You would be accepting
network-wide penalty risk in exchange for negligible PageRank. The risk/reward is bad even
before considering policy.

---

## The distinction that actually matters

**Google does not penalise you for owning 19 sites.** Common ownership is not a violation —
the AdSense ID and shared GSC account are not links and are not link spam.

**Google penalises the link pattern built to manipulate rank.**

So the question for any cross-link is never "is this allowed?" but:

> **Would a real visitor click this, and be glad they did?**

If yes, it is an editorial link that happens to be internal to the portfolio.
If no, it is a link scheme.

---

## ⚠ OPERATOR POLICY — the binding rules

Set by the operator 2026-08-24. **These override anything softer written below.**

| Rule | Detail |
|---|---|
| **Default** | **No cross-links at all.** Zero is the normal state of this portfolio |
| **Trigger** | Only when a site genuinely needs an SEO boost. Never routine, never on launch |
| **Who decides** | **The operator, explicitly.** Never added on an agent's initiative |
| **Earliest** | **4–5 months after the receiving site launched.** Never at launch, never in month 1–3 |
| **Cadence** | **One link. Then wait ~3 months. Then consider one more.** Never a batch |
| **Relevance** | Same audience cluster only (see clusters below). No exceptions |
| **Volume** | Minimise. Fewer is always safer. Aim to need none |

### Why the delay is the right instinct

A brand-new domain acquiring links the moment it launches is an unnatural pattern —
real sites earn their first links slowly, after they have something worth linking to. Waiting
4–5 months means the link arrives when the site plausibly deserves one.

It also costs nothing to wait: a link from a 3-month-old zero-authority site passes
approximately nothing anyway. **Both sites should have real age and traffic before a link
between them means anything at all.**

### Link ledger — record every one

Cross-links are rare enough to track individually. Log each here when added:

| Date | From site | To site | Placement | Anchor | Reason |
|---|---|---|---|---|---|
| — | — | — | — | — | *(none yet — this is the correct state)* |

---

## What IS allowed, when the policy above permits it

Build it for **referral traffic**, not for PageRank. A visitor moving from the colour picker
to the SVG viewer is a real, monetised session — that value is immediate and does not depend
on Google passing any link equity at all.

### Rules

1. **Only link between sites with genuine audience overlap.** Legitimate clusters:

   | Cluster | Sites |
   |---|---|
   | Designers | image colour picker · SVG tools · favicon generator · merge images · font identifier |
   | Developers / SEO | redirect checker · URL encoder · website down checker · website legit checker |
   | Device diagnostics | mouse · keyboard · webcam · microphone · audio · screen · refresh rate · gamepad |

   **Never** link across clusters. `gamepad tester -> PDF splitter` has no user overlap and
   reads as manipulation to a human reviewer, never mind an algorithm.

2. **Never link every site to every site.** That uniform mesh *is* the detectable pattern.
   Link 2–4 genuinely related tools, contextually.

3. **Contextual placement, not a global footer.** A small "related tools" block on relevant
   pages, or an in-content mention where it actually helps. **Not** a 19-link footer on every
   page of every site.

4. **Vary anchor text naturally.** Exact-match anchors repeated across a network is the
   classic signature.

5. **Add links when there is a reason**, not on launch day as a batch. A network that appears
   fully interlinked the moment each site goes live is a pattern; organic growth is not.

6. **Expect zero SEO value and be right about it.** If the links stop being useful to
   visitors, remove them. If you find yourself justifying a link by its SEO benefit, that is
   the signal it should not exist.

7. **`rel="nofollow"` is not required** for genuinely editorial links — and using it
   everywhere would concede these are not editorial. Just keep them few, relevant and useful.

---

## What to do instead for authority

The portfolio's stated constraint is already **no backlink building, no directory
submissions.** That leaves:

- **The tool being genuinely better** — the only durable link magnet. `wheregoes.com` and
  `testufo.com` earn links because people reference them, not because they built a network.
- **AEO** (`SEO-BRIEF` §16) — being recommended by ChatGPT/Claude/Gemini/Perplexity is the
  modern equivalent of a link, and it is earned by clarity, not by linking.
- **Genuine presence where people ask** — an honest Reddit/Stack Exchange answer where your
  tool is the real solution, with disclosure. One of those beats the entire cross-link scheme.
- **Brand search** — the moat coolors (30K/mo) and iLovePDF (8.7M/mo) actually have. Track it
  with GSC's branded-query filter.

---

## Decision

- ❌ **Do not** build a cross-link network for SEO value.
- ✅ **Do** add a small number of contextual, genuinely useful cross-links within an audience
  cluster, valued only for the referral traffic they produce.
- ✅ Revisit only if a site earns real independent authority — at which point a link from it
  means something and the calculus changes.
