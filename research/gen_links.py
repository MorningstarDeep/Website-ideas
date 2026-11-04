"""Generate synonym-groups.md with pre-built US-geo Google search links.

  python gen_links.py

ponytail: groups live here as data so the .md is disposable/regenerable. Edit the dict,
re-run, done. Hand-writing 165 URLs invites typos that silently return the wrong SERP.
"""
import urllib.parse

# category -> [(seed, [synonyms...])]
GROUPS = [
    ("Device Diagnostics", [
        ("Gamepad Tester", ["gamepad tester", "controller tester", "joystick test",
                            "stick drift test", "controller test"]),
        ("Keyboard Tester", ["keyboard tester", "keyboard test", "key tester",
                             "keyboard checker", "nkro test"]),
        ("Webcam Test", ["webcam test", "camera test", "webcam checker",
                         "test my camera", "webcam tester"]),
        ("Microphone Test", ["microphone test", "mic test", "mic check",
                             "test my microphone", "microphone tester"]),
        ("Speaker Test", ["speaker test", "audio test", "sound test", "stereo test",
                          "left right speaker test"]),
        ("Headphone Test", ["headphone test", "earphone test", "headset test",
                            "headphone check", "left right headphone test"]),
        ("Surround Sound Test", ["surround sound test", "5.1 surround sound test",
                                 "7.1 speaker test", "surround speaker test",
                                 "channel test"]),
        ("Monitor Test", ["monitor test", "screen test", "display test", "lcd test",
                          "monitor checker"]),
        ("Dead Pixel Test", ["dead pixel test", "stuck pixel test", "pixel checker",
                             "screen pixel test", "dead pixel checker"]),
        ("Refresh Rate Test", ["refresh rate test", "hz test", "monitor hz checker",
                               "144hz test", "screen refresh rate test"]),
        ("Mouse Tester", ["mouse tester", "mouse test", "double click test",
                          "mouse click test", "polling rate test"]),
        ("Touchscreen Test", ["touchscreen test", "touch test", "multi touch test",
                              "ghost touch test", "touchscreen checker"]),
    ]),
    ("Colors", [
        ("Image Color Picker", ["image color picker", "color picker from image",
                                "pick color from image", "eyedropper online",
                                "color picker from screenshot"]),
        ("Color Palette Generator", ["color palette generator", "color scheme generator",
                                     "color combination generator", "palette maker",
                                     "color palette"]),
        ("Color Palette From Image", ["color palette from image",
                                      "extract colors from image",
                                      "image color extractor", "palette from photo",
                                      "image to color palette"]),
        ("Hex to RGB Converter", ["hex to rgb", "rgb to hex", "color converter",
                                  "hex color converter", "color code converter"]),
    ]),
    ("Image Utilities", [
        ("Image Color Changer", ["image color changer", "change color of image",
                                 "replace color in image", "recolor image",
                                 "image color replacer"]),
        ("Merge Images", ["merge images", "combine images", "image merger",
                          "put two images side by side", "join images"]),
    ]),
    ("PDF", [
        ("Extract Pages From PDF", ["extract pages from pdf", "pdf page extractor",
                                    "save pages from pdf", "get pages from pdf",
                                    "copy pages from pdf"]),
        ("Split PDF", ["split pdf", "pdf splitter", "divide pdf",
                       "separate pdf pages", "split pdf into pages"]),
    ]),
    ("Website / URL", [
        ("Redirect Checker", ["redirect checker", "redirect chain checker",
                              "url redirect checker", "301 redirect checker",
                              "check redirects"]),
        ("HTTP Status Checker", ["http status checker", "url status checker",
                                 "status code checker", "website status checker",
                                 "http response checker"]),
        ("URL Encoder / Decoder", ["url encoder", "url decoder", "urlencode",
                                   "percent encoding", "url encode decode"]),
        ("Website Legitimacy Checker", ["is this website legit", "website checker",
                                        "site checker", "scam website checker",
                                        "website safety checker"]),
    ]),
    ("Fonts", [
        ("Font Identifier", ["font identifier", "what font is this", "font finder",
                             "identify font from image", "font recognition"]),
    ]),
    ("SVG & Icons", [
        ("SVG Viewer", ["svg viewer", "view svg online", "svg file viewer",
                        "open svg online", "svg code viewer"]),
        ("SVG Optimizer", ["svg optimizer", "compress svg", "minify svg",
                           "reduce svg size", "svg compressor"]),
        ("SVG to PNG", ["svg to png", "convert svg to png", "svg png converter",
                        "svg to png online", "export svg as png"]),
        ("Favicon Generator", ["favicon generator", "favicon maker", "create favicon",
                               "favicon checker", "png to favicon"]),
    ]),
    ("YouTube", [
        ("YouTube Transcript", ["youtube transcript", "youtube transcript generator",
                                "youtube video to text", "transcript youtube",
                                "youtube transcript downloader"]),
        ("YouTube Thumbnail Downloader", ["youtube thumbnail downloader",
                                          "youtube thumbnail grabber",
                                          "download youtube thumbnail",
                                          "get youtube thumbnail",
                                          "youtube thumbnail extractor"]),
        ("YouTube Thumbnail Tester", ["youtube thumbnail tester",
                                      "youtube thumbnail preview", "thumbnail checker",
                                      "youtube thumbnail simulator",
                                      "thumbnail preview tool"]),
        ("YouTube Tag Generator", ["youtube tag generator", "youtube tags",
                                   "video tag generator", "youtube keyword tool",
                                   "youtube hashtag generator"]),
    ]),
    # Appended, NOT inserted into Website/URL — inserting mid-list would renumber seeds
    # 25-33 and break every reference in 04-TOOL-VALIDATION.md.
    ("Website / URL (added)", [
        # Surfaced during seed 22: isitdownrightnow.com, $0.820/visit, 57% tier-1,
        # incumbent declining 220K -> 165K. Belongs with seeds 21-24 by topic.
        ("Website Down Checker", ["is this website down", "website down checker",
                                  "is it down right now", "site down checker",
                                  "check if website is down"]),
    ]),
    # Seed 35-37. Appended last to keep seeds 1-34 numbered as they were.
    ("Timers", [
        ("Pomodoro Timer", ["pomodoro timer", "focus timer", "study timer",
                            "tomato timer", "pomodoro technique timer"]),
        ("Aesthetic Timer", ["aesthetic pomodoro timer", "study timer aesthetic",
                             "aesthetic timer", "cute timer", "study with me timer"]),
        ("Stage Timer", ["stage timer", "presentation timer", "speaker timer",
                         "conference timer", "event countdown timer"]),
        ("Visual Timer", ["visual timer", "sand timer", "hourglass timer",
                          "timer for kids", "adhd timer"]),
        ("Duration Timer", ["30 minute timer", "25 minute timer", "1 hour timer",
                            "2 hour timer", "online timer"]),
    ]),
]

# pws=0 disables personalisation, gl=us forces the US SERP — the market we sell ads into
SERP = "https://www.google.com/search?q={}&gl=us&hl=en&pws=0"

HEADER = """# Phase A — synonym groups (US-geo search links)

39 seeds x 5 synonyms. Distinct **phrasings**, not modifier variants.

**Per keyword:** click the link (US SERP, personalisation off) -> copy the #1 result URL ->
paste into the traffic checker -> record organic/mo, traffic value, top countries,
top keywords + positions.

Traffic checker URL — swap in the result URL:
`https://ahrefs.com/traffic-checker/?input=PASTE_URL_HERE&mode=exact`

**The verdict per group is the pattern, not the traffic:**

- Same site #1 on every synonym -> **ENTRENCHED**, cluster already consolidated
- Different site wins each synonym -> **FRAGMENTED**, nobody owns it — best case
- A synonym with no dedicated tool -> **GAP**, enter there

Flag any competitor with **no US in its top-5 countries** — big traffic, but not defending
the market you monetise.

---
"""

FOOTER = """
---

## Capture template

```
## <N>. <Seed>

| Synonym | #1 result | Organic/mo | Traffic value | US share |
|---|---|---:|---:|---:|
|  |  |  |  |  |

Top keywords (US):
Pattern: ENTRENCHED / FRAGMENTED / GAP
```
"""


def main():
    out = [HEADER]
    n = 0
    for cat, seeds in GROUPS:
        out.append(f"\n## {cat}\n")
        for seed, syns in seeds:
            n += 1
            out.append(f"\n### {n}. {seed}\n")
            for s in syns:
                out.append(f"- [{s}]({SERP.format(urllib.parse.quote_plus(s))})")
            out.append("")
    out.append(FOOTER)
    p = "synonym-groups.md"
    open(p, "w", encoding="utf-8").write("\n".join(out))
    total = sum(len(s) for _, seeds in GROUPS for _, s in seeds)
    print(f"{n} seeds, {total} links -> {p}")


def demo():
    assert n_seeds() == 39, n_seeds()
    u = SERP.format(urllib.parse.quote_plus("5.1 surround sound test"))
    assert "q=5.1+surround+sound+test" in u and "gl=us" in u and "pws=0" in u, u
    # every seed must carry exactly 5 synonyms, else a group was mis-edited
    for _, seeds in GROUPS:
        for seed, syns in seeds:
            assert len(syns) == 5, f"{seed} has {len(syns)}"
            assert len(set(syns)) == 5, f"{seed} has duplicates"
    print("ok")


def n_seeds():
    return sum(len(seeds) for _, seeds in GROUPS)


if __name__ == "__main__":
    import sys
    (demo if len(sys.argv) > 1 and sys.argv[1] == "demo" else main)()
