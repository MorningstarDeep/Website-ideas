"""Micro-tool opportunity harvester. stdlib only.

  python harvest.py suggest seeds.txt out.jsonl      # google autocomplete expansion
  python harvest.py serp queries.txt out.jsonl       # duckduckgo SERP capture

ponytail: no deps, no db, JSONL append-only so a crashed run resumes by dedupe.
"""
import sys, json, time, random, re, os, html, base64, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def get(url, tries=5, timeout=20):
    """Fetch with backoff. Google serves a 200 'Sorry...' page when throttled —
    treat that as a hard block and sleep long, otherwise the whole run silently
    fills with empty results (happened once; cost an hour of harvest)."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "ignore")
            if "<title>Sorry..." in body or "unusual traffic" in body:
                time.sleep(30 * (i + 1) + random.random() * 10)
                continue
            return body
        except Exception:
            if i == tries - 1:
                return ""
            time.sleep(2.0 * (i + 1) + random.random())
    return ""

# ---------- autocomplete ----------

TOOL_WORDS = ("calculator", "calculater", "tool", "converter", "convertor", "generator",
              "estimator", "checker", "chart", "template", "formula", "app", "online",
              "free", "finder", "planner", "simulator", "visualizer", "maker", "table")

SUFFIXES = ["", " calculator", " tool", " chart", " converter", " generator",
            " estimator", " checker", " online", " template", " formula"]

def suggest(q, ds=""):
    u = ("https://www.google.com/complete/search?client=chrome&hl=en&gl=us"
         f"&q={urllib.parse.quote(q)}" + (f"&ds={ds}" if ds else ""))
    raw = get(u)
    if not raw:
        return []
    try:
        d = json.loads(raw)
        return d[1] if len(d) > 1 else []
    except Exception:
        return []

def expand_seed(seed):
    out = {}
    stems = [seed + s for s in SUFFIXES]
    stems += [seed + " " + c for c in "abcdefghijklmnopqrstuvwxyz"]
    stems += ["how to " + seed, "how many " + seed, "how much " + seed,
              "what size " + seed, "best " + seed]
    for st in stems:
        for s in suggest(st):
            out[s.lower()] = st
        time.sleep(0.12 + random.random() * 0.2)
    return out

def cmd_suggest(seedfile, outfile):
    seeds = [l.strip() for l in open(seedfile, encoding="utf-8") if l.strip()
             and not l.startswith("#")]
    seen = set()
    if os.path.exists(outfile):
        for l in open(outfile, encoding="utf-8"):
            try:
                seen.add(json.loads(l)["seed"])
            except Exception:
                pass
    seeds = [s for s in seeds if s not in seen]
    print(f"{len(seeds)} seeds to expand", flush=True)
    # ponytail: 3 threads, not 6 — Google throttles autocomplete above ~5 req/s
    with open(outfile, "a", encoding="utf-8") as f, ThreadPoolExecutor(3) as ex:
        for seed, res in zip(seeds, ex.map(expand_seed, seeds)):
            f.write(json.dumps({"seed": seed, "queries": res}) + "\n")
            f.flush()
            print(f"  {seed}: {len(res)}", flush=True)

# ---------- SERP ----------

FORUM = ("reddit.com", "quora.com", "stackexchange.com", "stackoverflow.com",
         "forum", "board", "community", "facebook.com", "answers")
SOCIAL = ("pinterest.", "youtube.com", "youtu.be", "tiktok.com", "instagram.com",
          "twitter.com", "x.com")
SHOP = ("etsy.com", "amazon.", "ebay.", "aliexpress", "walmart.com", "alibaba")
FARM = ("omnicalculator.com", "calculator.net", "inchcalculator.com", "calculatorsoup",
        "gigacalculator", "calcimator", "easycalculation", "calculator.academy",
        "calculatored", "allmath", "vcalc", "calkoo", "captaincalculator",
        "calctool.org", "blocklayer.com", "miniwebtool.com")
# The 2026 AI-generated calculator farms carpet-bomb every formula-shaped keyword.
# They are near-universally named <something>calc/tool<something>, so detect by shape
# rather than maintaining a list that goes stale weekly. Farm density on a SERP is an
# INVERSE opportunity signal: high density means the task reduces to a formula, which
# means it is infinitely cloneable and not worth building.
FARMISH = re.compile(r"(calc|tool)", re.I)
# real brands that would false-positive on FARMISH
NOT_FARM = ("tools.google", "toolsqa", "photopea", "canva", "adobe", "figma",
            "autodesk", "solidworks", "toolstation", "protoolreviews", "toolguyd")

DOCHOST = ("scribd.com", "slideshare.net", "docplayer", "studylib", "yumpu",
           "issuu.com", "academia.edu", "dokumen.pub", "vdocuments")

def classify(domain, url):
    d = domain.lower()
    u = url.lower()
    # a PDF is a PDF wherever it sits in the path, and a doc-locker is the same
    # signal wearing a different hat (user wanted a tool, got a scanned handout)
    if ".pdf" in u or any(x in d for x in DOCHOST):
        return "pdf"
    if any(x in d for x in SOCIAL):
        return "social/video"
    if any(x in d for x in FORUM):
        return "forum"
    if any(x in d for x in SHOP):
        return "shop"
    if any(x in d for x in FARM):
        return "calc-farm"
    if d.endswith(".edu") or d.endswith(".gov"):
        return "edu/gov"
    if "wikipedia" in d:
        return "wiki"
    if FARMISH.search(d.split(".")[0]) and not any(x in d for x in NOT_FARM):
        return "calc-farm"
    return "site"

def ddg(q):
    raw = get("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q))
    res = []
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href, title = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        mm = re.search(r"uddg=([^&]+)", href)
        url = urllib.parse.unquote(mm.group(1)) if mm else href
        if not url.startswith("http"):
            continue
        dom = url.split("/")[2].replace("www.", "")
        res.append({"d": dom, "u": url, "t": html.unescape(title.strip()),
                    "k": classify(dom, url)})
    return res

def bing(q):
    raw = get("https://www.bing.com/search?count=20&setmkt=en-US&q="
              + urllib.parse.quote(q))
    res = []
    for blk in re.findall(r'<li class="b_algo".*?</li>', raw, re.S):
        m = re.search(r'<h2[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
        if not m:
            continue
        href = m.group(1)
        b64 = re.search(r"u=a1([A-Za-z0-9_-]+)", href)
        if b64:
            s = b64.group(1) + "=" * (-len(b64.group(1)) % 4)
            try:
                href = base64.urlsafe_b64decode(s).decode("utf-8", "ignore")
            except Exception:
                pass
        if not href.startswith("http"):
            continue
        dom = href.split("/")[2].replace("www.", "")
        res.append({"d": dom, "u": href,
                    "t": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)).strip()),
                    "k": classify(dom, href)})
    return res

STOP = {"calculator", "tool", "online", "free", "chart", "the", "a", "for", "to",
        "of", "and", "app", "generator", "converter", "template", "size", "how",
        "what", "is", "in", "my", "best"}

def coverage(q, res):
    """Fraction of top-10 results that actually contain the distinctive query terms.

    Bing broad-matches when it has no exact corpus for a phrase (searching
    'wing cube loading calculator' returned Wingstop). Rather than fight that,
    measure it: low coverage == Bing found nothing really about this query, which
    is exactly the 'no dedicated result exists' signal this research is hunting.
    """
    terms = [w for w in re.findall(r"[a-z0-9]+", q.lower())
             if w not in STOP and len(w) > 2]
    if not terms or not res:
        return 0.0
    need = max(1, len(terms) // 2)
    hit = 0
    for x in res[:10]:
        blob = (x["t"] + " " + x["u"]).lower()
        if sum(1 for t in terms if t in blob) >= need:
            hit += 1
    return round(hit / min(10, len(res)), 2)

def serp(q):
    """Bing primary — as of 2026-08 it is the only free engine not captcha-walled
    (DDG html/lite and Mojeek all challenge). DDG kept as an occasional cross-check."""
    r = bing(q)
    if r:
        return r, "bing"
    time.sleep(3)
    return ddg(q), "ddg"

def cmd_serp(qfile, outfile):
    qs = [l.strip() for l in open(qfile, encoding="utf-8") if l.strip()
          and not l.startswith("#")]
    seen = set()
    if os.path.exists(outfile):
        for l in open(outfile, encoding="utf-8"):
            try:
                seen.add(json.loads(l)["q"])
            except Exception:
                pass
    qs = [q for q in qs if q not in seen]
    print(f"{len(qs)} queries", flush=True)
    # ponytail: serial with a 5s gap. DDG hard-blocks above ~1 req/2s and then
    # silently returns 0 results, which reads as "weak SERP" — the worst possible
    # failure mode for this research. Slow and correct beats fast and wrong.
    miss = 0
    with open(outfile, "a", encoding="utf-8") as f:
        for i, q in enumerate(qs, 1):
            r, eng = serp(q)
            if not r:
                miss += 1
                if miss >= 3:
                    print("  !! 3 empty in a row — backing off 120s", flush=True)
                    time.sleep(120)
                    miss = 0
            else:
                miss = 0
            kinds = {}
            for x in r[:10]:
                kinds[x["k"]] = kinds.get(x["k"], 0) + 1
            cov = coverage(q, r)
            f.write(json.dumps({"q": q, "n": len(r), "eng": eng, "cov": cov,
                                "kinds": kinds, "res": r[:12]}) + "\n")
            f.flush()
            print(f"  [{i}/{len(qs)}] cov={cov} {q}: {len(r)} ({eng}) {kinds}",
                  flush=True)
            time.sleep(5.0 + random.random() * 3)

if __name__ == "__main__":
    {"suggest": cmd_suggest, "serp": cmd_serp}[sys.argv[1]](sys.argv[2], sys.argv[3])
