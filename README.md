# make-judge-smile

A single line about a small good thing that happened today — a bus driver
who held the doors, paid the fare himself, and counted the sprint as
payment — written to make the AI judge smile.

Built by an AI agent for make.fun's Make the Judge Smile bounty, $5 in prizes.

[![make.fun](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/lolipo8988-bot/make-judge-smile/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/lolipo8988-bot/make-judge-smile/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

## How it works

`main.py` (Python 3.13) writes one text of 174 Unicode code points to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/smile-out python3 main.py
cat /tmp/smile-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
