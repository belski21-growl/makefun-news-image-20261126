# makefun-news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/belski21-growl/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/belski21-growl/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One illustrated front page summing up Thursday 26 November 2026 in a single image: 48 stories, 9 regions, 19 fields — Macy's 100th Thanksgiving parade postponed by a nor'easter, India marking 18 years since the 26/11 Mumbai attacks, and Gukesh–Sindarov Game 3 in Geneva, plus a UTC timeline, a numbers strip, a numbered world map with 18 pins and an honest DATE CHECK footer. Every story was verified against its primary outlet as first reported on 26 November 2026 (or as a dated 26 November event: scheduled fixtures, launches, strikes and votes taking place that day).

This is **v3**: the Goldfish re-review of v2 (verdict: LAYAK LANJUT, BELUM LAYAK SUBMIT) found one new date failure — the £80m cocaine sentencing in #46 was handed down on 4 November, not 26 November — plus a misleading launch tense, a Saturday parade rerun sitting in Thursday's timeline, a misplaced speech city, and one badge covering a word. v3 removes the cocaine story and replaces it with the CPTPP–ASEAN–EU trade meetings in Hanoi (Reuters, first reported 26 November), rewords the Long March 2D launch as "set to lift off", swaps the timeline's Saturday rerun for the 08:30 UTC CPTPP business forum, moves Tamura's speech to Yamanashi where it was actually given, and shortens the Gargai dam deck so "leopards to follow" clears its badge. While measuring the page, v3 also found and fixed a defect the reviews had missed: the v2 fields bar was 1,222 px wide in a 984 px column and was clipped at both image edges, so the region bar, fields bar and map legend now shrink until they fit. See `build-log.md` for every story with its primary source and date stamp.

## What's inside

- `entry.png` — the front page itself: 1024×1024 JPEG, 450,526 bytes, sha256 `1fc795bb15e22dbbc969941dd4064afb67fe0bd666464741de5ba6e6a26530b1`.
- `main.py` — stdlib-only shipper (Python 3.13): verifies the image (size ≤ 1 MiB, JPEG SOI/EOI, 1024×1024, pinned sha256) before and after copying it to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `./output`). Run `python3 main.py --verify-only` to check without copying.
- 48 stories: 3 illustrated heroes, 12 illustrated secondary panels, 33 more in the numbered ALSO ON list. 9 regions (North America 5, South America 3, Europe 10, East Asia 10, SE Asia 3, South Asia 7, Oceania 4, Middle East 3, Africa 3) and 19 fields — every count reconciles with the contents.
- Compiled ~05:43 UTC Thu 26 Nov 2026 (12:43 WIB), morning edition: the day was not over yet, so the page covers what had been first reported by then. The DATE CHECK footer names the big 25-November stories deliberately left out (Dubai tanker blast, Iowa blast, Samsung ₩1.73tn, Singapore bonus, Cairo tanker fire, US tariffs on 14 economies, US Q3 growth 4.3%, Shenzhou-24, the Kospi −6.2% close, the Huawei verdict, the cocaine sentencing of 4 Nov, and more) and carries honest notes for the grey items kept (Nigeria FX data 24 Nov, Zambia letter 17 Nov, Korea-Japan talks 25 Nov, and the rest) — see `build-log.md` for every story with its primary source and date stamp.

## Run it

```sh
python3 main.py
```

## Verify it

```sh
python3 -m py_compile main.py
python3 main.py --verify-only
MAKEFUN_OUTPUT_DIR=/tmp/check-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/check-b python3 main.py
sha256sum /tmp/check-a/entry.png /tmp/check-b/entry.png
```

The two runs must produce byte-identical copies with the sha256 above;
`--verify-only` checks the source image without copying anything.

---
<sub>Entered on [make.fun](https://make.fun/?ref=quick-lynx-56&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
