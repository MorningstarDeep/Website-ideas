"""Pull REAL Google autocomplete for each shortlist idea.

Presence in autocomplete is Google's own demand-floor signal; breadth across an
a-z sweep is the cluster-size signal. Slow and serial on purpose — Google throttles.

  python keywords.py shortlist-seeds.txt data/kw.jsonl
"""
import sys, json, time, random, os, urllib.parse
from harvest import get

def google(q):
    raw = get("https://www.google.com/complete/search?client=chrome&hl=en&gl=us&q="
              + urllib.parse.quote(q), tries=1)
    try:
        d = json.loads(raw)
        rel = d[4].get("google:suggestrelevance") if len(d) > 4 else None
        return list(zip(d[1], rel)) if rel else [(s, 0) for s in d[1]]
    except Exception:
        return []

def bing(q):
    raw = get("https://api.bing.com/osjson.aspx?query=" + urllib.parse.quote(q))
    try:
        return [(s, 0) for s in json.loads(raw)[1]]
    except Exception:
        return []

# Google autocomplete blocks this IP after bulk use; Bing's osjson endpoint does not.
# Bing suggestions are a different corpus but still real query language, so the source
# is recorded per row rather than silently mixed.
ENGINE = os.environ.get("KW_ENGINE", "bing")

def suggest(q):
    if ENGINE == "google":
        r = google(q)
        if r:
            return r, "google"
        return bing(q), "bing"
    return bing(q), "bing"

def main():
    seeds = [l.strip() for l in open(sys.argv[1], encoding="utf-8")
             if l.strip() and not l.startswith("#")]
    dst = sys.argv[2]
    done = set()
    if os.path.exists(dst):
        for l in open(dst, encoding="utf-8"):
            try:
                done.add(json.loads(l)["seed"])
            except Exception:
                pass
    seeds = [s for s in seeds if s not in done]
    print(f"{len(seeds)} seeds", flush=True)
    with open(dst, "a", encoding="utf-8") as f:
        for i, seed in enumerate(seeds, 1):
            out, eng = {}, "bing"
            stems = [seed] + [seed + " " + c for c in "abcdefghijklmnopqrstuvwxyz"]
            for st in stems:
                res, eng = suggest(st)
                for s, rel in res:
                    if s.lower() not in out or rel > out[s.lower()]:
                        out[s.lower()] = rel
                time.sleep(0.25 + random.random() * 0.25)
            f.write(json.dumps({"seed": seed, "eng": eng, "q": out}) + "\n")
            f.flush()
            print(f"  [{i}/{len(seeds)}] {seed}: {len(out)}", flush=True)
            time.sleep(1.0)

if __name__ == "__main__":
    main()
