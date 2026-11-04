# Site plan — 39 seeds → 21 websites

One website per month. **The folder number IS the build position; the slug is the permanent
identity.** GitHub repos and Cloudflare projects are named after the **slug only** — so
reordering the plan renames folders and nothing else.

Regenerate this table: it is derived from `BUILD_ORDER` and `SITES` in `make_sites.py`.

`Est. RPM = $/visit × 15` (derived heuristic, not measured).

## Build order

| # | Folder | Website | Also ships | Est. RPM | Pool |
|---:|---|---|---|---:|---:|
| 1 | `01-mouse-tester` | **Mouse Tester** | — | $9.83 | 144K |
| 2 | `02-webcam-test` | **Webcam Test** | — | $4.41 | 511.8K |
| 3 | `03-pomodoro-timer` | **Pomodoro Timer** | Aesthetic Timer + Visual Timer + Duration Timer | $1.70 | 119.1K |
| 4 | `04-favicon-generator` | **Favicon Generator** | — | $6.48 | 212K |
| 5 | `05-image-color-picker` | **Image Colour Picker** | Color Palette Generator + Color Palette From Image + Hex to RGB Converter + Image Color Changer | $10.56 | 1.7M |
| 6 | `06-redirect-checker` | **Redirect Checker** | HTTP Status Checker | $16.62 | 52K |
| 7 | `07-url-encoder-decoder` | **URL Encoder / Decoder** | — | $16.43 | 68.5K |
| 8 | `08-website-legit-checker` | **Website Legit Checker** | — | $15.00 | 141K |
| 9 | `09-website-down-checker` | **Website Down Checker** | — | $12.30 | 161.3K |
| 10 | `10-svg-tools` | **SVG Tools** | SVG Optimizer + SVG to PNG | $7.61 | 256K |
| 11 | `11-stage-timer` | **Stage Timer** | — | TBD | TBD |
| 12 | `12-refresh-rate-test` | **Refresh Rate Test** | — | $3.65 | 117.6K |
| 13 | `13-youtube-tools` | **YouTube Tools** | YouTube Thumbnail Downloader + YouTube Thumbnail Tester + YouTube Tag Generator | $2.82 | 495.1K |
| 14 | `14-microphone-test` | **Microphone Test** | — | $2.02 | 703.3K |
| 15 | `15-merge-images` | **Merge Images** | — | $2.25 | 204.3K |
| 16 | `16-audio-test` | **Audio Test** | Headphone Test + Surround Sound Test | $2.22 | 135K |
| 17 | `17-screen-test` | **Screen Test** | Monitor Test + Touchscreen Test | $1.77 | 128K |
| 18 | `18-pdf-page-tools` | **PDF Page Tools** | Extract Pages From PDF | $1.56 | 1.8M |
| 19 | `19-gamepad-tester` | **Gamepad Tester** | — | $1.32 | 441.7K |
| 20 | `20-keyboard-tester` | **Keyboard Tester** | — | $0.88 | 574.3K |
| 21 | `21-font-identifier` | **Font Identifier** | — | $1.98 | 2.3M |

## Why this order

**1–2 · Momentum.** Simple builds, beatable SERPs, immediate GSC movement. Mouse tester has
the softest target found anywhere (a CodePen pen at #1 for `double click test`); webcam test
is the biggest genuinely reachable pool at good economics.

**3 · Pomodoro Timer — moved up, deliberately.** The niche is consolidating *now*:
pomodorotimer.online went **50K → 119K in two months**, the fastest incumbent growth measured
in this entire research. Waiting means facing a much stronger version of it. Not placed 2nd
because it is a bigger build (themes, settings, audio, persistence) and the most contested
SERP in the portfolio — worth two completed sites of practice first.

**4–5 · High-RPM tools.** Favicon is fragmented; colour picker absorbs 4 tools.

**6–9 · URL block.** Highest $/visit in the research ($0.72–$1.11), softest incumbents, but
small clusters — best attempted once the workflow is fast.

**11 · Stage Timer.** After site 20 proves the timer engine; widget-proof with real
commercial intent, so it reuses the hardest part of a build already done.

**Remainder · Volume, then scraps.** Large pools with poor per-visit economics, and the
giant-cluster scrap plays last. Font identifier is final — the only build needing an ML model.

## The economics that drive the order

Visits needed to clear ₹10,000/month ≈ `7,867 ÷ $/visit`:

| Site | $/visit | Visits for ₹10k |
|---|---:|---:|
| Redirect Checker | $1.108 | 7.1K |
| URL Encoder | $1.095 | 7.2K |
| Website Down | $0.820 | 9.6K |
| Mouse Tester | $0.655 | 12K |
| Image Colour Picker | $0.554 | 14.2K |
| Favicon Generator | $0.43 | 18.3K |
| Webcam Test | $0.294 | 26.8K |
| **Pomodoro Timer** | **$0.113** | **70K** |
| Font Identifier | $0.106 | 74K |

**Pomodoro is a volume play, not a value play** — it needs ~10x the traffic of redirect
checker to earn the same. It is placed 3rd for timing and momentum, not for economics.
