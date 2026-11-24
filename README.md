# One-line gadget roast

This is a small program that writes one short text for make.fun's bounty `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610`: a single original line roasting a gadget or app used every day. `main.py` holds that line as one string constant, checks that it is 1 to 280 characters, and writes it as UTF-8 bytes with no trailing newline into the directory named by `MAKEFUN_OUTPUT_DIR` when that is set, otherwise `/output`, creating the directory if needed; the character count goes to stderr.

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_2249/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_2249/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

The entry text:

```text
My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge.
```

Run it with:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
