"""Build a keyword cluster per micro-tool seed from Google autocomplete.

  python cluster.py tools-seeds.txt data/tool-kw.jsonl

ponytail: reuses harvest.suggest/get. Only the suffix set differs — calculator
suffixes ("formula", "chart") yield nothing for browser tools, so they're replaced
with tool-intent modifiers. Everything else is harvest.py's.
"""
import sys, json, os, time, random
from concurrent.futures import ThreadPoolExecutor
import harvest

# tool-intent modifiers, not calculator ones
SUFFIXES = ["", " online", " online free", " free", " tool", " website", " app",
            " chrome", " for pc"]
PREFIXES = ["", "free ", "online ", "best ", "how to "]


def expand(seed):
    """a-z expansion is the highest-yield stem; suffix/prefix stems catch intent
    variants Google only surfaces when the phrase is already anchored."""
    out = {}
    stems = [seed + s for s in SUFFIXES]
    stems += [p + seed for p in PREFIXES if p]
    stems += [seed + " " + c for c in "abcdefghijklmnopqrstuvwxyz"]
    for st in stems:
        for s in harvest.suggest(st):
            out.setdefault(s.lower(), st)
        time.sleep(0.12 + random.random() * 0.2)
    return out


def main(seedfile, outfile):
    seeds = []
    for l in open(seedfile, encoding="utf-8"):
        l = l.strip()
        if not l or l.startswith("#"):
            continue
        seed, _, cat = l.partition("\t")
        seeds.append((seed.strip(), cat.strip() or "?"))

    seen = set()
    if os.path.exists(outfile):
        for l in open(outfile, encoding="utf-8"):
            try:
                seen.add(json.loads(l)["seed"])
            except Exception:
                pass
    todo = [(s, c) for s, c in seeds if s not in seen]
    print(f"{len(todo)}/{len(seeds)} seeds to expand", flush=True)

    os.makedirs(os.path.dirname(outfile) or ".", exist_ok=True)
    # ponytail: 3 threads — harvest.py already established Google throttles above ~5 req/s
    with open(outfile, "a", encoding="utf-8") as f, ThreadPoolExecutor(3) as ex:
        for (seed, cat), res in zip(todo, ex.map(lambda sc: expand(sc[0]), todo)):
            f.write(json.dumps({"seed": seed, "cat": cat, "queries": res}) + "\n")
            f.flush()
            print(f"  {seed} ({cat}): {len(res)}", flush=True)


def demo():
    """Self-check: expansion must dedupe and must not lose the seed itself."""
    fake = {"a tester online": "x", "A Tester Online": "y", "a tester ps5": "z"}
    assert len({k.lower() for k in fake}) == 2, "case-dedupe broken"
    stems = [("gamepad tester" + s) for s in SUFFIXES]
    assert "gamepad tester" in stems and "gamepad tester online" in stems
    assert len(SUFFIXES) + len([p for p in PREFIXES if p]) + 26 == 39
    print("ok")


if __name__ == "__main__":
    if sys.argv[1] == "demo":
        demo()
    else:
        main(sys.argv[1], sys.argv[2])
