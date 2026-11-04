"""Merge tool clusters + SERPs into a standalone-vs-umbrella screening table.

  python score_tools.py            # print table
  python score_tools.py csv        # write data/ahrefs-paste.csv (bulk import list)

No search volume here — none is obtainable without a paid API. This scores the two
halves that ARE obtainable: cluster breadth (demand ecosystem proxy) and SERP
competition. Volume from Ahrefs merges in afterwards.
"""
import sys, json, os, re, collections

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# Giants: if one of these owns the SERP, an EMD micro-site will not displace it.
BIG = ("adobe.com", "canva.com", "google.com", "microsoft.com", "apple.com",
       "amazon.com", "figma.com", "corel", "wondershare", "youtube.com",
       "w3schools.com", "cloudflare.com", "mozilla.org", "chrome.google")
# Multi-tool suites: strong domains that rank a subpage for everything. Beatable
# on intent (their page is one of 40), but they are real competition.
SUITE = ("ilovepdf.com", "smallpdf.com", "pdf24.org", "sejda.com", "cloudconvert.com",
         "freeconvert.com", "online-convert.com", "convertio.co", "zamzar.com",
         "tinywow.com", "123apps.com", "aspose.app", "foxit.com", "sodapdf.com",
         "pdfcandy.com", "xodo.com", "lightpdf.com", "pdf2go.com", "avepdf.com",
         "coolors.co", "colorhexa.com", "color-hex.com", "htmlcolorcodes.com",
         "vidiq.com", "tubebuddy.com", "veed.io", "kapwing.com", "descript.com",
         "notta.ai", "clideo.com", "img2go.com", "ezgif.com", "photopea.com",
         "iloveimg.com", "picsart.com", "fotor.com", "befunky.com")

# Reference/content domains that rank for the WORDS but are not competitors.
# Bing broad-matches tool phrases into dictionaries and how-to articles
# ("surround sound test" -> merriam-webster). Counting those as competition
# inverts the signal: a SERP full of dictionaries is an OPEN SERP, not a closed one.
NOISE = ("merriam-webster", "dictionary.", "cambridge.org", "britannica",
         "thesaurus", "wikihow.com", "geeksforgeeks.org", "developer.mozilla.org",
         "imdb.com", "win-rar.com", "hostinger.", "networksolutions.com",
         "wix.com", "squarespace.com", "linkedin.com", "medium.com",
         "wikipedia.org", "quora.com", "byjus.com", "vedantu.com")

STOP = {"online", "free", "tool", "the", "a", "for", "to", "of", "and", "app",
        "is", "this", "my", "best", "how", "what", "in", "test", "checker"}


def terms(q):
    return [w for w in re.findall(r"[a-z0-9]+", q.lower())
            if w not in STOP and len(w) > 2]


def is_emd(domain, seed):
    """Domain contains the seed's distinctive words, in any order, ignoring
    separators. Catches both exact (svgviewer.dev) and qualified (freesvgviewer)."""
    flat = re.sub(r"[^a-z0-9]", "", domain.lower())
    t = terms(seed)
    return bool(t) and all(w in flat for w in t)


def load():
    kw, serp = {}, {}
    p = os.path.join(D, "tool-kw.jsonl")
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            try:
                r = json.loads(l)
                kw[r["seed"]] = r
            except Exception:
                pass
    p = os.path.join(D, "tool-serp.jsonl")
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            try:
                r = json.loads(l)
                serp[r["q"]] = r
            except Exception:
                pass
    return kw, serp


def rows():
    kw, serp = load()
    out = []
    for seed, r in kw.items():
        qs = list(r["queries"])
        # verbatim = query actually contains the seed phrase; the rest is drift
        # (a-z expansion pulls in neighbours, which inflates a raw count)
        verb = [q for q in qs if seed in q]
        s = serp.get(seed, {})
        res = s.get("res", [])[:10]
        doms = [x["d"] for x in res]
        big = sum(1 for d in doms if any(b in d for b in BIG))
        suite = sum(1 for d in doms if any(b in d for b in SUITE))
        emd = sum(1 for d in doms if is_emd(d, seed))
        noise = sum(1 for x in res if any(n in x["d"] for n in NOISE)
                    or x["k"] in ("forum", "social/video", "pdf", "wiki",
                                  "shop", "edu/gov"))
        # dedicated competitors = top-10 minus giants, suites, and pure noise.
        # This is the count that decides whether a SERP is actually contested.
        ded = max(0, len(res) - big - suite - noise)
        out.append({
            "seed": seed, "cat": r.get("cat", "?"),
            "cluster": len(qs), "verbatim": len(verb), "cov": s.get("cov", 0),
            "serp_n": len(res), "big": big, "suite": suite,
            "emd": emd, "noise": noise, "ded": ded,
            "top": doms[:5],
        })
    out.sort(key=lambda x: (-x["verbatim"], x["big"] + x["suite"]))
    return out


def main():
    rs = rows()
    if not rs:
        print("no data yet — run cluster.py / harvest.py serp first")
        return
    print(f"{'seed':<28}{'cat':<8}{'verb':>6}{'cov':>5}{'ded':>5}{'big':>5}"
          f"{'suite':>6}{'emd':>5}{'noise':>6}  top domains")
    print("-" * 122)
    for r in rs:
        flag = " !" if r["cov"] < 0.5 else "  "
        print(f"{r['seed']:<28}{r['cat']:<8}{r['verbatim']:>6}{r['cov']:>5}"
              f"{r['ded']:>5}{r['big']:>5}{r['suite']:>6}{r['emd']:>5}"
              f"{r['noise']:>6}{flag}" + ", ".join(r["top"][:4]))
    print(f"\n{len(rs)} seeds. verb=autocomplete queries containing the seed phrase "
          f"(demand-ecosystem proxy, NOT volume).")
    print("ded=dedicated competitors in top-10 (excl. giants/suites/noise). "
          "cov<0.5 (!) = Bing broad-matched, SERP unusable.")


def csv():
    """Two cuts: everything, and verbatim-only.

    The a-z expansion drags in neighbouring topics ('keyboard tester' -> 'keyboard
    shortcuts'), which is useful for discovery but wrong for sizing THIS tool.
    Verbatim-only keeps queries containing the seed phrase, and fits inside
    Ahrefs Keywords Explorer's 10k-per-batch cap.
    """
    kw, _ = load()
    allrows, core = {}, {}
    for seed, r in kw.items():
        cat = r.get("cat", "?")
        for q in r["queries"]:
            allrows.setdefault(q, (seed, cat))
            if seed in q:
                core.setdefault(q, (seed, cat))

    for name, rows_ in (("ahrefs-paste.csv", allrows), ("ahrefs-core.csv", core)):
        p = os.path.join(D, name)
        with open(p, "w", encoding="utf-8") as f:
            f.write("keyword,seed,category\n")
            for q in sorted(rows_):
                s, c = rows_[q]
                f.write(f'"{q}","{s}",{c}\n')
        print(f"{len(rows_):>6} keywords -> {p}")
    # plain newline-delimited list is what you actually paste into Ahrefs
    p = os.path.join(D, "ahrefs-core.txt")
    open(p, "w", encoding="utf-8").write("\n".join(sorted(core)))
    print(f"{len(core):>6} keywords -> {p}  (paste this one)")


def demo():
    assert is_emd("svgviewer.dev", "svg viewer")
    assert is_emd("free-svg-viewer.com", "svg viewer")     # qualified EMD counts
    assert not is_emd("adobe.com", "svg viewer")
    assert is_emd("deadpixeltest.com", "dead pixel test")  # 'test' is a stopword
    assert terms("is this website legit") == ["website", "legit"]
    print("ok")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "table"
    {"table": main, "csv": csv, "demo": demo}[cmd]()
