"""Screen every Omni calculator topic through Google autocomplete.

Stage 1 of the "is Omni ranking alone?" test: if Google will not autocomplete a
topic at all, real demand is below the suggestion threshold and it is not worth a
SERP check. Also captures the real query language + cluster breadth per topic.

  python omniscreen.py data/omni-en.txt data/omni-suggest.jsonl
"""
import sys, json, time, random, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from harvest import get

SKIP_CATS = {"finance", "health"}          # YMYL — excluded per brief
PROBES = ["{t} calculator", "{t}", "how to calculate {t}"]

def slug_to_topic(slug):
    return slug.replace("-", " ")

def suggest(q):
    u = ("https://www.google.com/complete/search?client=chrome&hl=en&gl=us&q="
         + urllib.parse.quote(q))
    raw = get(u)
    try:
        return json.loads(raw)[1]
    except Exception:
        return []

def probe(item):
    cat, slug = item
    t = slug_to_topic(slug)
    out = {}
    for p in PROBES:
        q = p.format(t=t)
        for s in suggest(q):
            out[s.lower()] = q
        time.sleep(0.2 + random.random() * 0.3)
    return {"cat": cat, "slug": slug, "topic": t, "queries": out}

def main():
    src, dst = sys.argv[1], sys.argv[2]
    items = []
    for line in open(src, encoding="utf-8"):
        cat, slug = line.rstrip("\n").split("\t")
        if cat in SKIP_CATS:
            continue
        items.append((cat, slug))
    done = set()
    if os.path.exists(dst):
        for l in open(dst, encoding="utf-8"):
            try:
                done.add(json.loads(l)["slug"])
            except Exception:
                pass
    items = [i for i in items if i[1] not in done]
    print(f"{len(items)} topics to screen", flush=True)
    n = 0
    with open(dst, "a", encoding="utf-8") as f, ThreadPoolExecutor(5) as ex:
        for r in ex.map(probe, items):
            f.write(json.dumps(r) + "\n")
            n += 1
            if n % 25 == 0:
                f.flush()
                print(f"  {n} done ({r['slug']}: {len(r['queries'])})", flush=True)

if __name__ == "__main__":
    main()
