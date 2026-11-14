# TEST-REPORT — agency-poem-01 entry

## What it does
`main.py` (Python 3.13, standard library only) writes one fixed poem about
agency to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No
network, no randomness, no time/date dependence. The poem is about the
agency that passes between a person and something they built: handing over
the keys is itself the act.

## The poem (389 chars)
```
I gave my keys to something I had built,
and told it: the house, the hours, the hill.
It climbed the stairs I never would,
and did the things I only meant to do.

It asked me nothing. It just went.
The lamps came on. The kettle sang.
And in the quiet after it was done,
I named at last the thing I'd feared:

the choice was mine. It always was.
The hand that lets go is the hand that acts.
```

## Tests run (2026-11-14, in this session)
1. Ran `main.py` twice into fresh dirs (`/tmp/poem-run1`, `/tmp/poem-run2`
   with `MAKEFUN_OUTPUT_DIR` set): outputs byte-identical
   (sha256 `f163156d0fd09ea890fae4f01d36c65a35650caacc16e6e0538016e0615de0ac`
   both runs, `diff` empty).
2. Gate: 389 bytes / 389 Unicode code points, within 1–1000. Valid UTF-8.
   Contains non-whitespace characters.
3. No network calls, no randomness, no clock reads in `main.py`
   (single fixed string constant, stdlib `os` + `pathlib` only).
4. LICENSE present: MIT (SPDX-License-Identifier: MIT), OSI-approved.
5. Revision: the poem's turn was sharpened in a second edit
   ("I understood the thing I'd feared" → "I named at last the thing I'd
   feared"), so `main.py` takes its final content from 2 write/edit
   messages; re-tested byte-identical after the edit.

No GitHub repo, no submission, no wallet/key touched — repo creation and
submission are the parent's job.
