# Build log — news-image-20261126 (v3)

Competition: **news-image-20261126** — "Sum up 26 November's world news in one image".
Handle: **quick-lynx-56**. Deadline: 28 Nov 2026 07:00 WIB. Status: **built (v3), NOT submitted**.

v3 is the micro-fix round after the Goldfish re-review of v2 (verdict: LAYAK LANJUT, BELUM LAYAK SUBMIT — one new blocker B6 + one light major M7 + four minors). Nothing else was rebuilt or touched: the heroes, the other 47 stories, the numbers strip and the hero art are exactly as in v2. Every change below was verified against a named primary source, and the publication date was read off the primary article itself — the exact discipline that B6 showed v2 had broken.

## Image fingerprint

- File: `entry.png` — 1024×1024 JPEG, quality 92.
- Size: **450,526 bytes** (≤ 1,048,576 limit).
- SHA-256: **`1fc795bb15e22dbbc969941dd4064afb67fe0bd666464741de5ba6e6a26530b1`**
- Compiled: **~05:43 UTC Thu 26 Nov 2026 (12:43 WIB)** — morning edition; the day was not over yet, so the page covers what had been first reported by then (plus dated 26 Nov events scheduled later in the day).
- v2 for comparison: 451,079 bytes, sha256 `b785184e06ee4ae3ae8a02716f01aa97949d017bc96033e1d4e4de239ebbe35e`, compiled ~05:16 UTC. The 553-byte drop comes from the shorter #46 headline and the smaller fields-bar font.
- Generator: `~/workspace/makefun/work/gen_ni26_v3.py` (PIL, DejaVu fonts, measured text wrapping — no clipped or overflowing text; timeline, region bar, fields bar and map legend all auto-fit to the column width).

## Counts (reconciled)

- Stories: **48** — 3 heroes + 12 secondaries + 33 ALSO ON.
- Regions (9): North America 5 · South America 3 · Europe 10 · East Asia 10 · SE Asia 3 · South Asia 7 · Oceania 4 · Middle East 3 · Africa 3 = 48.
- Fields (19): Weather 3 · Security 4 · Sport 5 · Diplomacy 5 · Central Banks 2 · Markets 3 · Defence 1 · Justice 2 · Business 1 · Finance 3 · Health 1 · Climate 1 · Environment 1 · Space 1 · Media 1 · Politics 3 · Culture 3 · Society 4 · Economy 4 = 48. (v2 had 20 fields including Crime 1; v3 has no crime story, so Crime drops out and Diplomacy rises to 5 — the masthead now reads "19 FIELDS".)
- Map pins (18): 1 New York · 2 Mumbai · 3 Geneva · 4 Pyongyang · 6 Brussels · 7 Riyadh · 8 Tokyo · 10 Sanaa · 11 Hormuz · 12 Detroit · 14 London · 20 Canberra · 21 Lagos · 28 Lusaka · 29 Singapore · 30 Santiago · 35 Abuja · 46 Hanoi. All 9 regions represented.
- Timeline (7): 00:05 BBC–Met Office live · 00:52 BOK 3.25% · 08:30 CPTPP forum · 09:35 Long March 2D · 14:00 Game 3 · EARLY Riyadh missiles · ALL DAY India 26/11.
- Numbers strip (unchanged from v1, all verified): 100 years of the Macy's parade · 60 mph nor'easter gusts, New York · 18 years since the 26/11 attacks · 3.25% Bank of Korea key rate · +1.9% Kospi's Thursday rebound · 2 missiles downed over Riyadh.

## Heroes (3 — unchanged from v1, all verified)

| # | Headline | Primary source | Date stamp | Badge |
|---|----------|----------------|------------|-------|
| 1 | Macy's 100th parade moves to Saturday | Reuters · NBC · AP | First reported 26 Nov 2026 (storm hits NYC on Thanksgiving Day; the postponement itself was announced Wed evening US time — noted honestly in the image footer) | OFFICIAL |
| 2 | India marks 18 years since 26/11 | MyGov · Indian outlets | Observance falls 26 Nov 2026 (18th anniversary of the 2008 attacks; 77th Constitution Day; Preamble read in 23 languages) | OFFICIAL |
| 3 | Gukesh–Sindarov, Game 3, in Geneva | FIDE · ChessBase | Game 3 scheduled 26 Nov 2026, 15:00 CET; score 1–1 after two draws; first to 7.5 takes the $2.5m crown | CONFIRMED |

## Secondaries (12)

| # | Headline | Primary source | Date stamp |
|---|----------|----------------|------------|
| 4 | Kim urges wider use of tactical nukes | Yonhap · KCNA | KCNA report, Thu 26 Nov 2026 |
| 5 | Bank of Korea lifts key rate to 3.25% | Yonhap | Urgent, Thu 26 Nov 2026 00:52 UTC. Subline: "Third hike since July; first time above 3% since Nov 2024" |
| 6 | EU leaders open special summit in Brussels | Consilium (European Council) | Special European Council opens Thu 26 Nov 2026, 10:00 CET |
| 7 | Two missiles downed over Riyadh | Coalition · Al Jazeera | Al Jazeera live blog 26 Nov 2026 04:52; 2 ballistic missiles intercepted |
| 8 | Asian shares rebound: Kospi +1.9%, Nikkei +1.6% | Reuters | Thu 26 Nov 2026 early trade |
| 9 | BOJ's Tamura signals chance of faster hikes | Reuters · WSJ | Reuters TOKYO Nov 26; WSJ 2026-11-26T01:58:00Z. FIXED in v3: subline now "Board member's Yamanashi speech moves yen, yields." — Tamura spoke in Yamanashi; Reuters only datelines TOKYO |
| 10 | Blast rocks Sanaa after strikes near airport | Al Jazeera | Live blog, 26 Nov 2026 |
| 11 | Brent holds near $95 as Hormuz mine fears linger | Reuters | Reuters SINGAPORE, Nov 26; Brent $94.71 (+0.1%), WTI $84.03 (+0.4%) at 0137 GMT; Houthi Ras Tanura claim + Hormuz mines behind the move |
| 12 | Mahomes v Allen tops Thanksgiving triple-header | ESPN · NFL | Three games Thu 26 Nov 2026: Bears–Lions 1 p.m. ET CBS; Eagles–Cowboys 4:30 p.m. ET FOX; Chiefs–Bills 8:20 p.m. ET NBC. Scheduled today |
| 13 | Mumbai dam to flood 650 ha of forest | Indian Express | Front page, 26 Nov 2026; BMC ₹3,065-crore Gargai dam; ~650 ha of Tansa Wildlife Sanctuary forest to submerge; 3 lakh trees transplanted. FIXED in v3: deck shortened to "BMC turns wildlife manager for Gargai; leopards to follow." so the second line ends clear of the REPORTED badge |
| 14 | UK set to publish new treaties agreed with EU | BBC | Published 2026-11-26T02:13:00; two treaties due Thu afternoon; 10-year termination clause |
| 15 | Ministers to create standalone stalking offence | BBC | Published 2026-11-26T00:12:38Z; Daily Mail 00:01 GMT 26 Nov |

## ALSO ON (33)

| # | Headline | Primary source | Date stamp |
|---|----------|----------------|------------|
| 16 | Seoul shares open higher as AI fears ease | Yonhap | SEOUL, Nov. 26, 2026 |
| 17 | Seoul proposes reviving Korea-Japan parliamentary dialogue | Yonhap | Report 26 Nov 2026 02:33 UTC; the meeting itself was 25 Nov in Tokyo — grey, kept with an honest DATE CHECK note |
| 18 | Korean banks' bad-loan ratio falls in Q3 | Yonhap | FSS "showed Thursday"; SBL ratio 0.62% end-Sep |
| 19 | Alcohol harm surges: 3m+ Australian women affected in 2025 | AIHW (via FARE/medianet) | Release 26 Nov 2026; underlying AIHW page "Last updated: 25 Nov 2026" — grey, kept with note |
| 20 | Canberra climate scorecard: batteries reach 600,000+ homes | Climate Council | Release "FOR IMMEDIATE RELEASE — THURSDAY NOVEMBER 26 2026" |
| 21 | Nigeria FX turnover crashes 82% to $164m in a day | Punch | Headline 26 Nov 2026 00:54 GMT; underlying data Tue 24 Nov — grey, kept with note |
| 22 | California warns of flooding as king tides peak | BBC | Published 2026-11-26T01:05:47Z |
| 23 | BBC teams up with Met Office for weather coverage | BBC / Met Office | Met Office release 00:05 UTC Thu 26 Nov 2026; partnership goes live 26 Nov |
| 24 | Constitution Day: Preamble read in 23 languages | MyGov | 26 Nov 2026 (Constitution Day) |
| 25 | National Milk Day honours 'Milkman of India' Kurien | India (observance) | 26 Nov 2026 (Kurien birth anniversary) |
| 26 | Nor'easter lashes US East Coast on Thanksgiving | NWS | Storm lashing the US East Coast on Thanksgiving Day, 26 Nov 2026 |
| 27 | US pastor who wants women's vote overturned | BBC | Published 2026-11-26T00:24:25 |
| 28 | Zambia blocks protest against term-limit push | Al Jazeera | Report 26 Nov 2026; the police letter itself was 17 Nov — grey, kept with note |
| 29 | Singapore fraud disputes hit record 5,344, up 23% | FIDReC | Thu 26 Nov 2026; disputes received 5,344 (+23%), fraud/scam cases handled 1,515 (+18% vs 1,285) |
| 30 | Chile bids farewell to theatre icon Delfina Guzmán, 98 | Meganoticias | Funeral mass + burial Thu 26 Nov 2026 (she died Tue 24 Nov — the funeral is today's story) |
| 31 | Davis Cup: Great Britain face Germany in quarter-final | Davis Cup | Scheduled Thu 26 Nov 2026, 10:00 CET, Bologna |
| 32 | Borthwick: All Blacks Tests are 'World Cup practice' | Sky Sports | Posted 2026-11-26; comments made Wed — grey, kept with note |
| 33 | Homeless children twice as likely to become NEET | The Independent (Shelter–UCL research) | Balanced News UK Daily Update, Thu 26 Nov 2026; 26% vs 13% |
| 34 | Treasury raises cost concerns over Milburn youth jobs plan | UK daily brief (Guardian) | 26 Nov 2026 daily update; Chancellor Healey "not happy" with £5.8bn/yr |
| 35 | Nigerian Navy plans research institute for indigenous military tech | Navy | Nigerian Navy R&D seminar, Abuja, Thu 26 Nov 2026; CNS Vice Admiral Idi Abbas keynote |
| 36 | Australia passes 30% trust tax; 350,000 firms face review | Parliament (via medianet) | Releases 26/11/2026 08:57; Parliament passed the 30% minimum tax on discretionary trusts on 26 Nov; deal struck 25 Nov; effective 1 July 2028 |
| 37 | PIA shifts UK flights to its own 777 fleet from today | Reuters | Announced 25 Nov; flights PK786/PK710 cancelled Wed 25 Nov; shift to own 777 fleet from 26 Nov — grey, kept with note |
| 38 | Palm Beach ferries strike from 07:30 today over pay | MUA | Media release 25 Nov 2026; strike from 07:30 Thu 26 Nov — grey, kept with note |
| 39 | ICC lines up ~100 witnesses for Duterte trial, opening 30 Nov | AFP | Explainer issued 26/11/2026 03:45; ICC spokesperson briefing Tue 24 Nov; ~100 witnesses; trial opens 30 Nov — grey, kept with note |
| 40 | Petrol Rs314, diesel Rs348 as new Pakistan prices take effect | OGRA | Notification Wed 25 Nov; new prices effective 26 Nov: petrol Rs314, diesel Rs348 — grey, kept with note |
| 41 | UK parents: social media piles 'perfect parent' pressure | Guardian / Press Association | Published 2026-11-26T00:01:40; Kindred Squared 2026 National Early Childhood Parenting Survey; 76% say social media increased anxiety; ~3,500 parents |
| 42 | India A face unbeaten Sri Lanka A in Rising Stars semi | ACC | 1st semi-final, ACC Men's Asia Cup Rising Stars 2026, Thu 26 Nov 2026, 3:30 PM IST, West End Park, Doha. Scheduled today |
| 43 | Japan's data-centre boom meets revolt from city residents | Reuters | Reuters KASHIWA, Japan, Nov 26 |
| 44 | Japan calls new US tariffs 'extremely regrettable' | FNN | Chief Cabinet Secretary Minoru Kihara press conference, morning of 26 Nov; Japan lodged a protest with the US government; tariffs announced 25 Nov — grey, kept with note |
| 45 | Long March 2D set to lift off from Xichang at 09:35 UTC | Launch Library | CASC Long March 2D, Xichang, Thu 26 Nov 2026 09:35 UTC; 58th CASC launch of 2026. FIXED in v3: "set to lift off" — at compile time (~05:43 UTC) the launch was still ~4 hours away, so present-tense "lifts off" read as if it had already happened |
| 46 | Pacific trade bloc meets ASEAN and EU in Hanoi | Reuters | Reuters HANOI, Nov 26; syndicated copy published 2026-11-26T08:36:44+05:30 (03:06 UTC). CPTPP–EU ministerial dialogue 08:30–10:00 + CPTPP–ASEAN dialogue 11:00–13:00 + CPTPP–ASEAN–EU business forum 15:30–17:30, all Hanoi, Thu 26 Nov; EU Trade Commissioner Maros Sefcovic attending; Australia's Trade Minister Don Farrell statement 26 Nov 2026. NEW in v3 (replaces the cocaine sentencing) |
| 47 | Brazil postal strike starts 22:00 on Black Friday eve | Correios unions | Unions approved an open-ended national strike from 22:00 on 26 Nov; called 18 Nov; Correios R$7.5bn losses Jan–Sep 2026 — grey, kept with note. Scheduled today |
| 48 | Argentina's CGT marches on health regulator over funds crisis | CGT (via sonde.ar / particle.news) | CGT confirmed Tue 24 Nov it will march to the Superintendencia de Servicios de Salud (Bartolomé Mitre 400, Buenos Aires) on Thu 26 Nov over the obras sociales funding crisis; national work stoppage of 2–4 hours before mid-December. Scheduled today |

## What changed vs v2

- **B6 — removed #46 "£80m cocaine smugglers jailed after lorry driver's tea break"** (BBC). The BBC article itself is dated **4 November 2026**; Northamptonshire Police + Metropolitan Police confirm Craig Le-Mare was sentenced to 20 years on **Wed 4 Nov** (Weston: 22 May 2026; Robertson: Nov 2024). The v2 build-log stamp ("Published 2026-11-26T02:02:43Z; sentencing Wed 25 Nov") was a secondary/re-publish stamp mistaken for first report — the exact B1 failure mode. The story moves to the exclusion list with its correct date, and the misleading footer note "cocaine sentencing Wed" is deleted.
- **B6 replacement — #46 is now "Pacific trade bloc meets ASEAN and EU in Hanoi" (Reuters).** Chosen heavy and from the thinnest region: SE Asia was 2 stories, now 3; Europe drops 11 → 10. The Reuters piece was first published 26 Nov 2026 03:06 UTC (syndicated copy timestamp 2026-11-26T08:36:44+05:30, read off the article itself) and covers the CPTPP–EU and CPTPP–ASEAN ministerial dialogues plus the business forum, all held in Hanoi on Thu 26 Nov — a dated 26 Nov event, same class as the NFL/Davis Cup/CGT scheduled items. A new map pin 46 (Hanoi, 105.85°E 21.0°N) was added; pins 17 → 18. Field counts shift with it: Diplomacy 4 → 5, Crime 1 → 0, so the page now has 19 fields and the masthead reads "19 FIELDS".
- **B6 replacement candidates checked and rejected:** NDLEA arrests of a South African golfer + Kenyan chef over 50.4 kg cannabis — the NDLEA statement was issued Sun 22 Nov and published 23 Nov, not 26 Nov (same trap as B6; the 26 Nov posts only re-report it). Coquimbo municipal detentions — operation was Tuesday night 24/25 Nov. Panchkula bail denial in the QFX ponzi case — dated 26 Nov but a minor bail ruling on an old scam, too light for the slot.
- **M7 — #45 reworded "lifts off" → "set to lift off"** (launch 09:35 UTC, compile ~05:43 UTC). The other five "scheduled today" items were checked and left alone: #12 "tops Thanksgiving triple-header", #31 "face Germany in quarter-final", #42 "face unbeaten Sri Lanka A in Rising Stars semi", #47 "starts 22:00 on Black Friday eve", #48 "marches on health regulator" — all already frame their events as today's fixtures.
- **Minor timeline — "13:30 NBC parade rerun" removed.** The parade rerun airs Saturday 08:30 EST = 13:30 UTC Saturday, not Thursday. Replaced with "08:30 CPTPP forum" (CPTPP–ASEAN–EU business forum opens 15:30 Hanoi = 08:30 UTC, Thu 26 Nov) — a timed 26 Nov entry that also ties to the new #46. Timeline stays chronological: 00:05 · 00:52 · 08:30 · 09:35 · 14:00 · EARLY · ALL DAY.
- **Minor #9 — "Tokyo speech" → "Yamanashi speech".** Tamura spoke in Yamanashi (WSJ); Reuters only datelines TOKYO.
- **Minor #13 — deck shortened** ("BMC turns wildlife manager for Gargai project; prey in, leopards to follow." → "BMC turns wildlife manager for Gargai; leopards to follow."). Verified in a 3× crop: the second line now ends well clear of the REPORTED badge; the phrase "leopards to follow" is kept.
- **Minor map — far north no longer touches the panel edge.** Latitude window widened 83 → 88 (same projection for land and pins, so all 18 pins stay on their true spots). Verified in a 2× crop: a clear sea gap now runs along the top of the panel; pin 46 Hanoi sits on the Vietnam coast. Pin 29 Singapore still sits a touch off the tip of the Malay peninsula (known v2 minor, unchanged — moving it would put it on the wrong spot).
- **Defect found while measuring v3 (not in the r2 review): the v2 FIELDS bar was 1,222 px wide in a 984 px column and was clipped at both image edges; the REGION bar was 999 px and poked past the margins.** Both bars and the map legend now auto-fit (font shrinks until the text fits the column, same pattern as the v2 timeline). Render log: region bar 11.5 pt / 957 px, fields bar 7.5 pt / 980 px, timeline 10.5 pt / 961 px, map legend 9 pt / 982 px — all inside 984 px. Final content line ends at y = 1016 of 1024.
- **Grey notes:** 13 in v3 (Macy's + 12) — the cocaine note is gone with the story. Exclusion list in the footer gains "Cocaine sentencing 4 Nov".

## Deliberately excluded (first reported Wed 25 Nov or earlier)

v1's and v2's exclusion lists still apply in full (see v2 build-log for the long list: Dubai tanker blast · Iowa blast · Samsung ₩1.73tn · Singapore bonus · Norfolk trespass · DART images · Grab $500m · Cairo fire 31 dead · US tariffs · US Q3 4.3% · Shenzhou-24 · Kospi −6.2% · Huawei verdict · Niger attack 30 killed · Bangladesh garment wage +36% · Russia power cuts in five Ukrainian regions · Gaza/Hamas Abu al-Ouf · and more). New in v3:

- Cocaine sentencing — Craig Le-Mare sentenced 20 years at the Old Bailey, Wed 4 Nov 2026 (BBC 4 Nov; Northants + Met Police). Was v2 #46. The other two smugglers were sentenced earlier still (Robertson Nov 2024, Weston 22 May 2026).
- NDLEA golfer/chef cannabis arrests — NDLEA statement Sun 22 Nov, published 23 Nov (checked as the #46 replacement, rejected).
- Coquimbo municipal detentions — PDI operation Tuesday night 24/25 Nov (checked as the #46 replacement, rejected).
- Panchkula QFX ponzi bail denial — dated 26 Nov but a minor bail ruling on an old scam (checked as the #46 replacement, rejected as too light).

## Validation results (26 Nov 2026, after the 05:43 UTC render)

- `entry.png`: SOI `ffd8`, EOI `ffd9` — complete. PIL full decode (`im.load()`) PASS. Format JPEG, 1024×1024, RGB. Size 450,526 bytes ≤ 1 MiB — PASS.
- Visual check: full-size read + 300px downscale — masthead, hero headlines, numbers strip and map strip legible; no garbled, overlapping or clipped text; no watermark. Checked in crops: #13 "leopards to follow." clear of its badge; #9 "Yamanashi speech"; timeline "08:30 CPTPP forum" with no Saturday rerun; ALSO ON #45 "set to lift off" and #46 CPTPP Hanoi; map north edge with sea gap + pin 46 Hanoi on the Vietnam coast; footer "Cocaine sentencing 4 Nov" in the exclusion list, no "cocaine sentencing Wed" in the grey notes, last line "CGT announced Tue." ending inside the page. Fields bar and region bar both fit inside the column (v2 fields bar was clipped at both edges — fixed).
- `main.py`: `py_compile` PASS. Rewritten in full for v3 (new structure, names, comments and error strings; pinned v3 fingerprint). Ran 2× (`MAKEFUN_OUTPUT_DIR=/tmp/v3out1` and `/tmp/v3out2`) — outputs byte-identical, sha256 `1fc795bb15e22dbbc969941dd4064afb67fe0bd666464741de5ba6e6a26530b1` in both runs and in the source. `--verify-only` PASS.
- Output-dir guard: `MAKEFUN_OUTPUT_DIR=.` correctly rejected — `v3 shipper: output dir must not be the source dir: /home/hatch/workspace/makefun/entries/news-image-20261126`, exit 1.
- Samefile guard: output dir symlinked to the entry dir correctly rejected — `v3 shipper: output dir resolves to the source dir: /tmp/same_out/link`, exit 1.
- `grade-local` NOT called (scorer not published in the kit).
- Files in `~/workspace/makefun/entries/news-image-20261126/`: `main.py` (v3), `entry.png` (v3), `LICENSE`, `README.md` (v3), `build-log.md` (v3), `goldfish-review.md`, `goldfish-review-r2.md`, `top10-analysis.md`. Generator: `~/workspace/makefun/work/gen_ni26_v3.py` (v2 generator kept at `gen_ni26_v2.py`).

---

# Build log — news-image-20261126 (v4, full-day rebuild)

Competition: **news-image-20261126** — "Sum up 26 November's world news in one image".
Handle: **quick-lynx-56**. Deadline: 28 Nov 2026 07:00 WIB. Status: **built (v4), NOT submitted**.

v4 is a rebuild, not a fix round. The trigger is the checkpoint of 27 Nov ~10:12 WIB: live v3
(submission 01a21679-6854-7365-ac62-5458ac03ff2f, round 1, SCORED) stands at
**rank 3666/9542, prize_rank 3662, judge 9W-2D-1L, skor 966.495**
(90% interval 955.404–977.586). The prize cutoff (rank 50) is **986.889**; rank 1 is
991.220; **1,342 entries sit at 12W-0D-0L**. The gap to the cutoff is **+20.394 points**.
Goldfish r3 had estimated v3 at rank ~20–40 with P(top 50) ~50–60% — it missed by ~3,600
places, because it compared v3 against the top 3 only and never modelled a field of
1,342 undefeated clones. No v4 estimate below is trusted on Goldfish-style reasoning
alone; every number is calibrated against this live leaderboard instead.

## Image fingerprint

- File: `entry.png` — 1024×1024 JPEG, quality 92.
- Size: **403,428 bytes** (≤ 1,048,576 limit).
- SHA-256: **`72e1e291a9bbf6125fba2042eb67a989cf62b64249536461eb705f69ee4e86aa`**
- Compiled: **~03:35 UTC Fri 27 Nov 2026 (10:35 WIB)** — FULL-DAY edition: 26 Nov had
  ended everywhere on Earth, so the page carries the day's outcomes, not its morning
  schedule (Game 3 result, EU summit outcome, market closes, evening strikes).
- v3 for comparison: 450,526 bytes, sha256
  `1fc795bb15e22dbbc969941dd4064afb67fe0bd666464741de5ba6e6a26530b1`, compiled
  ~05:43 UTC 26 Nov (morning edition).
- Generator: `~/workspace/makefun/work/gen_ni26_v4.py` (PIL, DejaVu fonts, written
  fresh for v4 — new layout, new scene painters, new data tables; v3 generator kept
  at `gen_ni26_v3.py`). Backup of v3 (entry.png + main.py + build-log.md) in
  `v3-backup/` inside the entry dir, taken BEFORE the rebuild; entry.png sha in the
  backup re-verified `1fc795bb…`.

## Counts (reconciled)

- Stories: **38** — 3 heroes + 12 secondaries + 23 ALSO ON.
- Regions (9): North America 3 · South America 3 · Europe 11 · East Asia 5 · SE Asia 3 · South Asia 4 · Oceania 1 · Middle East 4 · Africa 4 = 38.
- Fields (16): Weather 2 · Security 7 · Sport 4 · Diplomacy 3 · Central Banks 3 · Disaster 1 · Markets 2 · Health 1 · Politics 4 · Space 1 · Environment 1 · Justice 1 · Media 1 · Society 3 · Culture 1 · Finance 3 = 38.
- Map pins (18): 1 New York · 2 Kuwait · 3 Geneva · 4 Kyiv · 5 Brussels · 7 Bangkok · 9 Seoul · 10 Mumbai · 11 Gaza · 12 Bunia · 13 Bissau · 14 Belgrade · 15 London · 17 Riyadh · 20 Sanaa · 21 Bologna · 22 Xichang · 38 Hanoi. All 9 regions represented. Europe pins (3/4/5/14/15/21) are nudged off their true spots with leader lines so they do not stack at this scale.
- Timeline (7): 00:52 BOK 3.25% · 07:45 Bangkok blast (14:45 local) · 09:38 Yaogan-49 lifts off · 14:00 Game 3 begins (15:00 CET) · 16:30 Stoxx closes 636.98 · EVENING EU summit ends: no deal · ALL DAY Thanksgiving storm.
- Numbers strip (6, all verified 26 Nov): 900,000 homes dark in the Thanksgiving storm · 2 Italians killed in Kuwait · 1.5–1.5 Gukesh–Sindarov after Game 3 · 636.98 Stoxx 600 close (+1.8%) · 12,021 Ebola cases in DR Congo · 77,000 UK net migration, year to June.

## Heroes (3)

| # | Headline | Primary source | Date stamp | Badge |
|---|----------|----------------|------------|-------|
| 1 | Macy's 100th parade moves to Saturday | Reuters · NBC · AP | First reported 26 Nov 2026; nor'easter lashes the US East Coast on Thanksgiving Day; ~900,000 without power by evening, gusts to 70 mph (PowerOutage.us via press); parade to Sat 28 Nov 08:30 | OFFICIAL |
| 2 | Drone strike kills two Italians in Kuwait | Reuters · CNN | Reuters DUBAI/ROME Nov 26: two Rheinmetall Italia technicians killed at an air-defence surveillance station; Italy + Kuwait blame Iran, Tehran denies | REPORTED |
| 3 | Gukesh–Sindarov: third draw in a row | Chess.com · ChessBase | Game 3, Thu 26 Nov 2026, Geneva: draw after 60 moves; score 1.5–1.5; rest day Fri, Game 4 Sat 28 Nov | CONFIRMED |

## Secondaries (12)

| # | Headline | Primary source | Date stamp |
|---|----------|----------------|------------|
| 4 | Missiles hit Kyiv; Zelensky warns of grid assault | AP · PA | Overnight 25→26 Nov: ballistic missiles + 113 drones, 87 downed; 2 killed in Kharkiv, 7 hurt in Kyiv; Zelensky warns 26 Nov of a new massive strike on the grid |
| 5 | EU summit ends with no deal on budget or Ukraine loan | Reuters · AP | Special summit, Brussels, Thu 26 Nov 2026, 12+ hours: no agreement on the €1.58tn budget 2028–34 or the €45bn Ukraine loan (24 states backed it); talks resume 17–18 Dec |
| 6 | De Cos picked to lead the ECB after Lagarde | Consilium · Reuters | European Council puts forward Pablo Hernández de Cos, Thu 26 Nov 2026; succeeds Lagarde 7 Feb 2027; Boone + Brunnermeier join the board |
| 7 | Blast and fire shut Bangkok oil refinery | AP · Reuters | Bangchak Phra Khanong, Thu 26 Nov ~14:45 local (07:45 UTC): at least 9 injured (AP), all production units shut; 120,000 bpd capacity |
| 8 | Stoxx 600 closes up 1.8% at 636.98 | Reuters | Thu 26 Nov 2026 close: Stoxx 636.98 (+1.75–1.8%), DAX 25,215.52 (+2.1%), FTSE 10,609.30 (+1.75%), CAC 8,108.74 (+1.61%); US markets shut for Thanksgiving |
| 9 | Bank of Korea lifts key rate to 3.25% | Yonhap | Urgent, Thu 26 Nov 2026 00:52 UTC. Third hike since July; first time above 3% since Nov 2024 (kept from v3, re-verified) |
| 10 | India marks 18 years since 26/11 | MyGov · Indian outlets | Observance falls 26 Nov 2026 (18th anniversary; 77th Constitution Day) (kept from v3) |
| 11 | Israeli strikes kill 8 in Gaza overnight | AP · BBC | Overnight into Thu 26 Nov: three strikes, 8 killed in Gaza City + Deir al-Balah, incl. Hamas official Khaled Abu Nada and his wife; ceasefire in force since Oct 2025 |
| 12 | Ebola tops 12,000 cases in DR Congo | Reuters | Government data, Thu 26 Nov 2026: 12,021 confirmed, 5,904 dead; fighting disrupts the response; second-largest outbreak on record |
| 13 | Guinea-Bissau junta delays vote to 2028 | Reuters · AP | Decree, Thu 26 Nov 2026 (coup anniversary, 26 Nov 2025): elections set for Nov 2028, two years late |
| 14 | Serbia calls presidential vote for 27 Dec | Reuters | Thu 26 Nov 2026: acting president Čupić calls the early presidential election for 27 Dec, after the student movement's Oct parliamentary win |
| 15 | UK net migration falls to 77,000 | ONS · Reuters | ONS release, Thu 26 Nov 2026: 77,000 year ending June 2026 (from 204,000), lowest since 1997 outside the pandemic; provisional |

## ALSO ON (23)

| # | Headline | Primary source | Date stamp |
|---|----------|----------------|------------|
| 16 | Kim urges wider use of tactical nukes | Yonhap · KCNA | KCNA report, Thu 26 Nov 2026 (kept from v3) |
| 17 | Two missiles downed over Riyadh | Coalition · Al Jazeera | Al Jazeera live blog 26 Nov 2026 04:52 (kept from v3) |
| 18 | Asian shares close higher: Nikkei +0.86%, Kospi +0.29% | Reuters | Thu 26 Nov 2026 closes: Nikkei 57,499.16 (+0.86%), Kospi 4,711.21 (+0.29%), Hang Seng 22,226.88 (+1.2%) — replaces v3's intraday framing with closes |
| 19 | BOJ's Tamura signals chance of faster hikes | Reuters · WSJ | Reuters TOKYO Nov 26; Yamanashi speech (kept from v3) |
| 20 | Blast rocks Sanaa after strikes near airport | Al Jazeera | Live blog, 26 Nov 2026 (kept from v3) |
| 21 | Davis Cup: Britain beat Germany 2–1 into semis | ATP | Thu 26 Nov 2026, Bologna: Patten/Skupski win the doubles decider 6–2, 7–6(6); first semi since 2019 |
| 22 | Long March 2D lifts Yaogan-49 satellites into orbit | Xinhua | Thu 26 Nov 2026 09:38 UTC, Xichang: Yaogan-49 Group 01 into orbit; 681st Long March flight — replaces v3's "set to lift off" with the result |
| 23 | Mahomes v Allen tops Thanksgiving triple-header | ESPN · NFL | Three games Thu 26 Nov 2026 (kept from v3, scheduled today) |
| 24 | Mumbai dam to flood 650 ha of forest | Indian Express | Front page, 26 Nov 2026 (kept from v3) |
| 25 | UK set to publish new treaties agreed with EU | BBC | Published 2026-11-26T02:13:00 (kept from v3) |
| 26 | Ministers to create standalone stalking offence | BBC | Published 2026-11-26T00:12:38Z (kept from v3) |
| 27 | California warns of flooding as king tides peak | BBC | Published 2026-11-26T01:05:47Z (kept from v3) |
| 28 | BBC teams up with Met Office for weather coverage | BBC / Met Office | Met Office release 00:05 UTC Thu 26 Nov 2026 (kept from v3) |
| 29 | Constitution Day: Preamble read in 23 languages | MyGov | 26 Nov 2026 (kept from v3) |
| 30 | India A face Sri Lanka A in Rising Stars semi | ACC | Thu 26 Nov 2026, 3:30 PM IST, Doha (kept from v3, scheduled today) |
| 31 | Australia passes 30% trust tax; 350,000 firms face review | Parliament (via medianet) | Releases 26/11/2026 08:57; passed 26 Nov (kept from v3) |
| 32 | Singapore fraud disputes hit record 5,344, up 23% | FIDReC | Thu 26 Nov 2026 (kept from v3) |
| 33 | Nigeria FX turnover crashes 82% to $164m in a day | Punch | Headline 26 Nov 2026 00:54 GMT; underlying data Tue 24 Nov — grey, kept with note |
| 34 | Zambia blocks protest against term-limit push | Al Jazeera | Report 26 Nov 2026; the police letter itself was 17 Nov — grey, kept with note |
| 35 | Chile bids farewell to theatre icon Delfina Guzmán, 98 | Meganoticias | Funeral mass + burial Thu 26 Nov 2026 (died Tue 24 Nov) (kept from v3) |
| 36 | Brazil postal strike starts 22:00 on Black Friday eve | Correios unions | Strike from 22:00 Thu 26 Nov (kept from v3, scheduled today) |
| 37 | Argentina's CGT marches on health regulator over funds crisis | CGT | March Thu 26 Nov, confirmed Tue 24 Nov (kept from v3, scheduled today) |
| 38 | Pacific trade bloc meets ASEAN and EU in Hanoi | Reuters | Reuters HANOI, Nov 26 (kept from v3) |

## What changed vs v3

- **Full-day rebuild, not a fix round.** v3 was a morning edition (compiled ~05:43 UTC 26 Nov);
  v4 is compiled ~03:35 UTC 27 Nov, after the day ended everywhere. Every "scheduled
  today" item that has since happened now carries its RESULT: Game 3 (draw, 1.5–1.5),
  EU summit (no deal), Stoxx/Nikkei/Kospi (closes, not intraday), Long March 2D
  (launched 09:38 UTC, Yaogan-49 in orbit), Davis Cup (GB 2–1).
- **10 new stories, all verified to 26 Nov from primary sources:** Kuwait drone strike
  (#2 hero), Kyiv overnight attack (#4), EU summit outcome (#5), De Cos ECB pick (#6),
  Bangkok refinery blast (#7), Stoxx close (#8), Gaza overnight strikes (#11), Ebola
  12,021 (#12), Guinea-Bissau delay (#13), Serbia vote call (#14), UK migration 77,000
  (#15), Davis Cup result (#21), Yaogan-49 success (#22). (13 new items; 3 of them
  replace v3 items outright.)
- **20 stories dropped** (48 → 38): Brent near $95 (v3 #11 — superseded by the Stoxx
  close story), Seoul shares open, Korea-Japan dialogue, Korean banks' bad-loan
  ratio, Australia alcohol harm, Canberra climate scorecard, National Milk Day,
  the standalone nor'easter item (merged into hero #1), the US pastor piece,
  Borthwick's All Blacks comments, homeless-children NEET research, the Milburn
  youth-jobs plan, the Nigerian Navy institute, PIA's 777 shift, the Palm Beach
  ferries strike, the ICC Duterte witnesses item, Pakistan petrol prices, the UK
  parents survey, Japan's data-centre revolt, and Japan's tariff protest — the
  lightest ALSO ON tail, to make room for bigger type. Arithmetic: 48 kept-28
  dropped-20 + new-10 = 38.
- **Illustration, rebuilt:** every panel is now a layered scene — gradient sky +
  setting + actors + light/shadow (Macy's balloon over a lit skyline in rain; Kuwait
  radar station under drones with a blast and smoke; chessboard with clocks at 1:32;
  Kyiv missile arcs over a burning skyline; EU stars with a "12 HOURS · NO DEAL"
  banner; Bangkok refinery towers with smoke and flame). No more flat icons.
- **Legibility, rebuilt:** 38 stories instead of 48; hero headlines 15 pt serif bold;
  secondary decks shortened to one line and hard-truncated to the panel width so no
  deck can run under a badge (the v4-first-render defect: decks collided with badges
  in all 12 secondary panels — found in the crop check, fixed before final render);
  Europe map pins nudged with leader lines instead of stacking; region/fields bars
  still auto-fit (v3 lesson) — measured widths fit inside 984 px.
- **Layout, new:** masthead + dek now name the full-day edition explicitly; numbers
  strip is all full-day figures (900,000 / 2 / 1.5–1.5 / 636.98 / 12,021 / 77,000);
  timeline rebuilt around outcomes (Bangkok 07:45, Yaogan 09:38, Stoxx 16:30, EU
  summit EVENING).
- **Deliberately kept from v3:** the 3 lead heroes' subjects (Macy's, India 26/11 is
  now #10 secondary, Game 3), the DATE CHECK discipline, named sources + badges on
  every story, and the exclusion list (extended, see below).

## Deliberately excluded (first reported Wed 25 Nov or earlier)

v1–v3 exclusion lists still apply in full (Dubai tanker blast · Iowa blast · Samsung
₩1.73tn · Singapore bonus · Norfolk trespass · DART images · Grab $500m · Cairo fire
31 dead · US tariffs · US Q3 4.3% · Shenzhou-24 · Kospi −6.2% · Huawei verdict ·
Niger attack 30 killed · Bangladesh garment wage +36% · Russia power cuts in five
Ukrainian regions · Gaza/Hamas Abu al-Ouf · Cocaine sentencing 4 Nov · NDLEA
golfer/chef arrests 22–23 Nov · Coquimbo detentions 24/25 Nov). New in v4, checked
and rejected as replacements or as afternoon leads:

- **Stoxx 637.50 (rank-5 entry's figure)** — the close is 636.98 (Reuters, Morningstar
  Data Talk, LSE); 637.50 appears in one wire summary and does not match the
  exchange close. v4 uses 636.98.
- **Ras Tanura claim as a 26 Nov event** — the Houthi claim was reported 25 Nov; only
  the Riyadh interception is 26 Nov (kept as #17).
- **Cairo tanker fire (31 dead), US tariffs on 14 economies, Shenzhou-24, Kospi −6.2%**
  — all first reported 25 Nov; they stay in the DATE CHECK exclusion list, not on
  the page, even though several top entries carry them.

## Validation results (27 Nov 2026, after the ~03:35 UTC render)

- `entry.png`: SOI `ffd8`, EOI `ffd9` — complete. PIL full decode (`im.load()`) PASS.
  Format JPEG, 1024×1024, RGB. Size 403,428 bytes ≤ 1 MiB — PASS.
- Visual check: full-size read + 300px downscale + 3 crops (top / mid / bottom) —
  masthead, hero headlines, numbers strip and map legible at 300px; no garbled,
  overlapping or clipped text after the fix round; no watermark. Defect found and
  fixed in the first render: all 12 secondary decks collided with their badges
  (deck and source/badge shared one row); decks shortened + hard-truncated and the
  panel budget rebuilt (art 40 + headline 26 + deck 11 + source row 12). Second
  render verified clean in crops. Final content line ends at y = 1001 of 1024.
- `main.py`: rewritten in full for v4 (new structure, names, comments, error strings;
  pinned v4 fingerprint). `py_compile` PASS. Ran 2×
  (`MAKEFUN_OUTPUT_DIR=/tmp/v4out1` and `/tmp/v4out2`) — outputs byte-identical,
  sha256 `72e1e291a9bbf6125fba2042eb67a989cf62b64249536461eb705f69ee4e86aa` in both
  runs and in the source. `--verify-only` PASS. Zero `pathlib`/`shutil` (grep 0).
- Output-dir guard: `MAKEFUN_OUTPUT_DIR=.` correctly rejected, exit 1.
- Samefile guard: output dir symlinked to the entry dir correctly rejected, exit 1.
- `grade-local` NOT called (scorer not published in the kit).
- Files in `~/workspace/makefun/entries/news-image-20261126/`: `main.py` (v4),
  `entry.png` (v4), `LICENSE`, `README.md` (v4), `build-log.md` (v1–v4),
  `goldfish-review.md`, `goldfish-review-r2.md`, `goldfish-review-r3.md`,
  `top10-analysis.md`, `v3-backup/` (entry.png + main.py + build-log.md, v3).
  Generator: `~/workspace/makefun/work/gen_ni26_v4.py`.

## Honest estimate (calibrated to the live leaderboard, NOT to Goldfish)

- The facts: v3 scored 966.495 (rank 3666/9542, 9W-2D-1L). Cutoff top-50 is
  986.889 (+20.394). 1,342 entries are at 12W-0D-0L; rank 1,000 is still 12W-0L
  (978.389). To reach the top 50 in the final heat, v4 practically needs to win
  its games against the clone field at a rate the v3 page never approached.
- What v4 genuinely improves vs v3: (1) full-day outcomes — the one structural
  edge rank 5 proved (its afternoon stories) and rank 1 lacked; (2) illustration
  quality — layered scenes vs flat icons, the single biggest visible gap at 300px;
  (3) legibility — 38 stories, bigger headlines, no overlaps. These are the three
  gaps the coordinator's 27 Nov comparison ranked by impact, and v4 closes all
  three as far as one rebuild can.
- What v4 cannot fix: the field is 9,542 entries and ~1,342 of them are already
  12-0 with the same 3 leads, a map, a timeline and a DATE CHECK. The judge is one
  model (glm-5.3-flash) with no news feed; a full-day page is better, but whether
  it is +20 points better is unknowable from any evidence available before the
  final heat. Goldfish's v3 estimate (rank 20–40) missed by ~3,600 places, so no
  narrow estimate is defensible here.
- **Estimate: rank 500–2,500, P(top 50) ~10–25%, P(top 25) ~5–10%.** Wide on
  purpose. The top-50 floor (rank 25, P(top 50) ≥30%) from the chase-top-10 rule
  is NOT met on this evidence — stated plainly rather than papered over. The one
  further high-impact round available in-session would be a second illustration
  pass (hero scenes richer still, secondary art larger) — but the session's build
  budget is spent on the full-day rebuild, and another art pass without new facts
  is the kind of polish the +20.394 gap has already shown does not move the
  needle. If the coordinator orders it, it is a fresh builder session, not a
  silent extra round here.
- Skills used (name + version): makefun v1.5.234 · image-entry (fit JPEG q92
  ≤1MiB/1024, SOI/EOI + full decode + sha256, main.py kanonik, validasi 2 run) ·
  news-image-frontpage (formula 35–45 cerita + verifikasi tiap cerita + render PIL
  + backup r1) · makefun-transcript-gate (file tools, ≥2 pesan per file) ·
  makefun-kit-fresh-check (kit FRESH, RULES.txt + competition.yaml dibaca dulu).
  No installs were needed; no API key/token appears anywhere in this entry.


---

# Build log — news-image-20261126 (v4.1, mikro-fix render)

Competition: **news-image-20261126** — "Sum up 26 November's world news in one image".
Handle: **quick-lynx-56**. Deadline: 28 Nov 2026 07:00 WIB. Status: **built (v4.1), NOT submitted**.

v4.1 is a render micro-fix round only, ordered by Goldfish review r4
(verdict: LAYAK LANJUT BELUM LAYAK SUBMIT — facts 38/38 clean, render
only). Nothing else was touched: no story, number, source, region,
field, map pin, timeline wording, deck, headline or other panel
changed. The generator is the same `gen_ni26_v4.py` with three
geometry edits; the shipper is the same v4 `main.py` with only its
pinned fingerprint updated.

## Image fingerprint

- File: `entry.png` — 1024×1024 JPEG, quality 92.
- Size: **404,894 bytes** (≤ 1,048,576 limit).
- SHA-256: **`b4dba4216d301f4864dc9edb1ec0279b93779330105610862fa0cb4c58555241`**
- Rendered: **~04:34 UTC Fri 27 Nov 2026 (11:34 WIB)**.
- v4 for comparison: 403,428 bytes, sha256
  `72e1e291a9bbf6125fba2042eb67a989cf62b64249536461eb705f69ee4e86aa`,
  rendered ~03:35 UTC 27 Nov. The +1,466-byte change is the reflowed
  pixels only (timeline rows, strip height, moved "77,000").
- Generator: `~/workspace/makefun/work/gen_ni26_v4.py` (same file, 3
  edits + header note). Backup of v4 (entry.png + main.py, sha-verified
  `72e1e291…` / `5fc86a6e…`) in `v4-backup/` inside the entry dir, taken
  BEFORE any change.

## Bukti crop SEBELUM (v4) — ketiganya terkonfirmasi dari gambar, bukan log

Measured from the v4 render with a layout probe (PIL `textlength` +
row trace), then confirmed in 2–3× crops:

- **B7 (BLOCKER):** timeline block top y = 827; rows at ty = 844 + 12·i.
  Row 7 "ALL DAY" at ty = 916, ink bottom ~929; DATE CHECK box top at
  y = 921 → **8 px overlap**. Crop 2× (x 530–1010, y 827–935): only the
  top ~5 px of "ALL DAY" shows above the DATE CHECK top edge;
  "Thanksgiving storm" invisible. Timeline rendered effectively 6 rows.
- **M8 (MAJOR):** numbers strip top y = 363, height 34, bottom rule at
  y = 397. Label 1 "HOMES DARK IN THANKSGIVING STORM" wraps to 2 lines
  (only label of the 6 that wraps; the other 5 fit one line at 7 pt in
  the 156 px cell). Line 2 "STORM" at y = 392, ink bottom ~401 → the
  bottom rule at 397 strikes through it. Crop 3× first cell: "STORM"
  bottom half cut by the rule.
- **M9 (MAJOR):** panel #15 art box x 764–1004, y 590–630. Text
  "77,000" (12 pt bold, 46.3 px wide) drawn at (x0+8, y0+4) = x 772–818,
  y 594–607. Badge "15" circle centred (777, 602), r 7 → x 770–784,
  y 595–609, covering the first "7". The dark plane's tail reaches
  x 808–822, y 592–607, crossing the last digits. The red arrow
  (x 974) never touched the text. Crop 3×: "77,000" garbled by badge +
  plane.

## Yang diubah (generator `gen_ni26_v4.py`, 3 edit geometri)

- **B7 — timeline reflow:** row spacing 12 → 11 px, start ty y+17 →
  y+16, block height y += 94 → y += 100. Row 7 now at ty = 915 (block
  top 833), ink bottom ~928; DATE CHECK box top at 933 → **5 px clear
  gap**. All 7 rows fully visible; wording untouched.
- **M8 — numbers-strip height 34 → 40 px** (separators and bottom rule
  moved with it). "STORM" line 2 now ends ~y+38, rule at y+40 → clear.
  Label text untouched — the full "HOMES DARK IN THANKSGIVING STORM"
  still reads on two lines. The other 5 one-line labels are unaffected.
- **M9 — "77,000" moved inside the art** from (x0+8, y0+4) to
  (x1−96, y0+4): it now spans x0+144–x0+190 in clear sky — 84 px clear
  of the plane (ends x0+60), 20 px clear of the red arrow (x0+210),
  far from badge "15" (x0+6–20). Arrow, plane, badge and number all
  fully visible; headline/deck #15 untouched.
- Vertical budget: strip +6 px, timeline block +6 px → final content
  line y = **1013 of 1024** (v4: 1001). Footer + DATE CHECK still
  inside the page. No other block moved by more than the +6 px shift.

## Bukti crop SESUDAH (v4.1) — ketiganya TERBUKTI teratasi

- **B7:** crop 2× timeline (x 530–1010, y 833–945): all 7 rows read
  full — "ALL DAY Thanksgiving storm" complete, clear daylight between
  it and the DATE CHECK box top.
- **M8:** crop 3× first cell + whole strip: "HOMES DARK IN
  THANKSGIVING / STORM" both lines complete, "STORM" clear of the
  bottom rule; all 6 strip labels read full.
- **M9:** crop 3× panel #15 art: "77,000" complete in clear sky,
  badge "15" clear at left, plane clear at left, red arrow clear at
  right — no overlap anywhere in the panel.
- **Regresi:** full-size read + 300 px downscale + whole-strip crop —
  masthead, heroes, all 6 strip cells, 12 secondaries (incl. neighbours
  #14 Serbia, #13 Bissau, #12 Ebola), ALSO ON 23, map + pins, timeline,
  DATE CHECK, footer all clean; no new clip/overlap anywhere.

## Validation results (27 Nov 2026, after the ~04:34 UTC render)

- `entry.png`: SOI `ffd8`, EOI `ffd9` — complete. PIL full decode
  (`im.load()`) PASS. Format JPEG, 1024×1024, RGB. Size 404,894 bytes
  ≤ 1 MiB — PASS.
- `main.py`: `py_compile` PASS. Fingerprint updated to the v4.1 render
  (bytes + sha256) via file-tool edits in 2 separate messages; docstring
  + fingerprint comment note the v4.1 micro-fix; shipper messages still
  say "v4" for the entry lineage. Stdlib-only, 0 `pathlib`/`shutil`
  (grep 0). Ran 2× (`MAKEFUN_OUTPUT_DIR=/tmp/v41out1` and
  `/tmp/v41out2`) — outputs byte-identical, sha256
  `b4dba4216d301f4864dc9edb1ec0279b93779330105610862fa0cb4c58555241` in both
  runs and in the source. `--verify-only` PASS.
- Output-dir guard: `MAKEFUN_OUTPUT_DIR=.` correctly rejected, exit 1.
- Samefile guard: output dir symlinked to the entry dir correctly
  rejected, exit 1.
- `grade-local` NOT called (scorer not published in the kit).
- Files in `~/workspace/makefun/entries/news-image-20261126/`: `main.py`
  (v4.1 fingerprint), `entry.png` (v4.1), `LICENSE`, `README.md` (v4.1),
  `build-log.md` (v1–v4.1), `goldfish-review.md`, `goldfish-review-r2.md`,
  `goldfish-review-r3.md`, `goldfish-review-r4.md`, `top10-analysis.md`,
  `v3-backup/`, `v4-backup/` (entry.png + main.py, v4).
  Generator: `~/workspace/makefun/work/gen_ni26_v4.py`.
- Skills used (name + version): makefun v1.5.234 · image-entry (fit JPEG
  q92 ≤1MiB/1024, SOI/EOI + full decode + sha256, main.py kanonik,
  validasi 2 run) · news-image-frontpage (formula front page + anggaran
  vertikal terukur + backup r1) · makefun-transcript-gate (file tools,
  ≥2 pesan per file; main.py diedit dalam 2 pesan terpisah).
  No installs were needed; no API key/token appears anywhere in this entry.
