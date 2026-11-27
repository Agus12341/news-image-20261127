[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Agus12341/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Agus12341/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

# The World Today - Friday 27 November 2026

One image that sums up the world news of Friday 27 November 2026, drawn as a newspaper front page for the make.fun bounty [news-image-20261127](https://make.fun/bounty/news-image-20261127).

The front page leads with the coastal storm that postponed the 100th Macy's Thanksgiving Day Parade in New York and left half a million US homes without power. Below it: the drone strike in Kuwait that killed two Italian workers, the diesel tanker that capsized off Ibiza with one dead, and the marathon draw in Game 3 of the World Chess Championship between Gukesh and Sindarov. The ticker adds two more of the day's stories: Israeli strikes killing 10 in Gaza, and UK net migration falling to its lowest level since 1997.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` checks that `entry.png` is a whole PNG inside the competition limits (at most 1 MiB, at most 1024 by 1024 pixels) and copies it to the output directory as `entry.png`. With no `MAKEFUN_OUTPUT_DIR` set it writes to `/output`, as in the grader.
