"""Flatten harvested autocomplete into tool-intent candidates.

  python analyze.py data/suggest.jsonl [--all|--seed X|--min N]
"""
import sys, json, re
from collections import defaultdict

TOOL = re.compile(r"\b(calculator|calculater|calc|tool|converter|convertor|conversion|"
                  r"generator|estimator|checker|chart|template|formula|online|app|"
                  r"finder|planner|simulator|visualizer|maker|table|worksheet|"
                  r"spreadsheet|excel|pdf|guide|cheat sheet)\b", re.I)
# queries that describe a task without naming a tool
TASK = re.compile(r"^(how (to|do|many|much|long|big)|what (size|is|are)|can i|"
                  r"is there|convert|calculate|work out|figure out|estimate)\b", re.I)

def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    return rows

def main():
    path = sys.argv[1]
    rows = load(path)
    seen = set()
    by_seed = defaultdict(list)
    total = 0
    for r in rows:
        for q in r["queries"]:
            total += 1
            if q in seen:
                continue
            seen.add(q)
            if TOOL.search(q) or TASK.match(q):
                by_seed[r["seed"]].append(q)
    print(f"# {len(rows)} seeds, {total} raw, {len(seen)} unique, "
          f"{sum(len(v) for v in by_seed.values())} tool/task-intent\n")
    for seed in sorted(by_seed, key=lambda s: -len(by_seed[s])):
        qs = by_seed[seed]
        print(f"\n## {seed}  ({len(qs)})")
        for q in sorted(qs):
            print("   ", q)

if __name__ == "__main__":
    main()
