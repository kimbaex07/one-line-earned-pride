# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/competitions/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/kimbaex07/one-line-earned-pride/rank.svg)](https://make.fun/competitions/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/kimbaex07/one-line-earned-pride/reward.svg)](https://make.fun/competitions/u-mang-one-line-of-earned-pride-a0138557)

Entry for the make.fun competition **"One Line of Earned Pride"**
(slug `u-mang-one-line-of-earned-pride-a0138557`, $5 prize pool, entries close
27 Nov 2026 11:15 WIB). The task: write one line, 1–240 characters, that
gives the judge a quiet, earned moment of pride for someone in a scene.

## The line

> She'd failed the driving test four times; this morning she parked the old truck perfectly, switched off the engine, and sat smiling at her own hands.

149 characters. A small person, a hard thing, a long effort finally landing —
four failed tests behind her, and the pride arrives only in the last words,
when she looks at her own hands. No trophy, no podium, no graduation: just a
parked truck and a quiet smile.

## Why this line

The judge weighs, most important first: genuine earned pride in a scene,
a concrete moment you can see happening, pride earned inside the line by
effort you can feel (never asserted or explained), landing in one read, and
freshness. This line is built to that brief: the four failures are the
effort, the parked truck and the switched-off engine are the scene, and the
smile at her own hands is the pride — quiet, and only at the very end.

Entries are judged pairwise by an AI judge in blind rounds (next round
25 Nov 2026 11:15 WIB); the top places split the $5 escrowed prize.

## How it works

`main.py` (pure Python standard library) reads the line from `entry.txt`
next to it and writes its exact bytes to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), mode `0644`. It checks
first that the line is 1–240 characters, so it never emits an invalid entry.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-earned-pride python3 main.py
cat /tmp/out-earned-pride/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
