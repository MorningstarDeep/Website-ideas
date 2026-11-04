"""Open a seed's 5 synonym SERPs in one incognito window.

  python serp.py 3           # webcam test -> 5 incognito tabs
  python serp.py 3 --edge    # same, in Edge
  python serp.py             # list all seeds with their numbers

ponytail: reuses GROUPS from gen_links so synonyms live in exactly one place.
"""
import sys, subprocess, urllib.parse
from gen_links import GROUPS, SERP


def flat():
    """[(n, seed, [synonyms])] with the same numbering as synonym-groups.md"""
    out, n = [], 0
    for _, seeds in GROUPS:
        for seed, syns in seeds:
            n += 1
            out.append((n, seed, syns))
    return out


def urls(syns):
    return [SERP.format(urllib.parse.quote_plus(s)) for s in syns]


def open_tabs(us, browser):
    """`start <browser>` resolves via the Windows App Paths registry, so this works
    without hardcoding an install path. Multiple URLs land as tabs in one window."""
    try:
        subprocess.run(["cmd", "/c", "start", "", browser, "--incognito", *us],
                       check=True)
        return True
    except Exception as e:
        print(f"couldn't launch {browser}: {e}\n")
        for u in us:
            print(u)
        return False


def main():
    rows = flat()
    if len(sys.argv) < 2:
        for n, seed, syns in rows:
            print(f"{n:>3}. {seed:<32}{syns[0]}")
        return
    n = int(sys.argv[1])
    browser = "msedge" if "--edge" in sys.argv else "chrome"
    match = [r for r in rows if r[0] == n]
    if not match:
        print(f"no seed {n} (1-{len(rows)})")
        return
    _, seed, syns = match[0]
    print(f"{seed}: {len(syns)} tabs")
    for s in syns:
        print(f"  - {s}")
    open_tabs(urls(syns), browser)


def demo():
    rows = flat()
    assert len(rows) == 39, len(rows)
    assert rows[0][1] == "Gamepad Tester" and rows[33][1] == "Website Down Checker"
    assert all(len(r[2]) == 5 for r in rows)
    u = urls(["5.1 surround sound test"])[0]
    assert "q=5.1+surround+sound+test" in u and "gl=us" in u
    print("ok")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        main()
