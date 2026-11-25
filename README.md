# Two Robots in an Elevator

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/ukyo9k/two-robots-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/ukyo9k/two-robots-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) bounty on [make.fun](https://make.fun).

## The line

> I ran a diagnostic on my small-talk module. It returned one word: 'awkward.' So... nice elevator, huh?

One robot, one elevator, one failed attempt at small talk.

## How it works

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`./output/entry.txt`). It validates the output the same way the
competition gate does — UTF-8 text, 1–200 characters, not only
whitespace, no control characters — and does a byte-level round-trip
check so what is written is exactly what was intended.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
