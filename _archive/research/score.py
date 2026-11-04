"""Score captured SERPs for micro-tool opportunity.

  python score.py data/calib-serp.jsonl

The core signal is FARM DENSITY, and it is INVERSE. Empirically (2026-08 scan):
formula-shaped queries return 5-7 AI-generated calculator farms; dataset-shaped
queries return zero. High farm density means the task reduces to a formula, which
means it is infinitely cloneable and already cloned. Low farm density + PDFs +
forums + vendor pages means nobody could auto-generate it => real moat.
"""
import sys, json, re
from harvest import classify

GAPPY = ("pdf", "forum", "social/video", "shop", "wiki", "edu/gov")

def dedicated(res, q):
    """Does this result look like a tool built FOR this query (not a blog about it)?"""
    words = [w for w in re.findall(r"[a-z]+", q.lower())
             if w not in ("calculator", "tool", "online", "free", "chart", "the", "a",
                          "for", "to", "of", "and")]
    hits = 0
    for x in res[:10]:
        t = (x["t"] + " " + x["u"]).lower()
        if sum(1 for w in words if w in t) >= max(2, len(words) - 1):
            hits += 1
    return hits

def score(r):
    res, q = r["res"], r["q"]
    top = res[:10]
    if not top:
        return None
    kinds = [x["k"] for x in top]
    farm = kinds.count("calc-farm")
    gap = sum(1 for k in kinds if k in GAPPY)
    site = kinds.count("site")
    ded = dedicated(top, q)
    # farm density is inverse; gappy results are positive
    opp = (gap * 10) + max(0, 40 - farm * 10) + max(0, 30 - ded * 5)
    return {"q": q, "farm": farm, "gap": gap, "site": site, "ded": ded,
            "opp": opp,
            "shape": "FORMULA (cloned)" if farm >= 3 else
                     "dataset/gap" if farm == 0 and gap >= 2 else
                     "contested" if ded >= 4 else "mixed"}

def main():
    rows = []
    for l in open(sys.argv[1], encoding="utf-8"):
        r = json.loads(l)
        # reclassify with current rules (FARM list evolves as new farms appear)
        for x in r["res"]:
            x["k"] = classify(x["d"], x["u"])
        s = score(r)
        if s:
            rows.append(s)
    rows.sort(key=lambda x: -x["opp"])
    print(f"{'opp':>4} {'farm':>4} {'gap':>3} {'ded':>3}  {'shape':<18} query")
    for s in rows:
        print(f"{s['opp']:>4} {s['farm']:>4} {s['gap']:>3} {s['ded']:>3}  "
              f"{s['shape']:<18} {s['q']}")

if __name__ == "__main__":
    main()
