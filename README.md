# news-image-20261118-entry

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)

**The World Today — Wednesday, 18 November 2026.** One front page summing up the
day's world news in six stories: Iran's drone strikes on US bases in Kuwait and
Bahrain after the American strike on Qeshm Island; Mary Peltola's Alaska win
handing Democrats a projected 56–44 Senate majority; the Ebola outbreak in DR
Congo more than doubling to 11,000+ cases; a Russian military plane crash in
Siberia killing 19; 146,000 marching across France over living costs; and
Category 5 Cyclone Xavier hitting the Northern Cook Islands.

## Run it

```sh
python3 draw_frontpage.py   # re-render entry.png (needs Pillow + DejaVu fonts)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the shipped `entry.png`
to `/output/entry.png`, so both grader runs write identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=47zzszhb&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
