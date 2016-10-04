# infralab
Python experiment and profiling lab repository
## Ongoing Projects
#### Terminal GUI construction
The goals is to make a Terminal-only GUI for a drink cooling system. (see my repository `cryphor-cryOS`.) I'm having a hard time finding a package that isn't engineered for another purpose, like form entry. The right package must:
* Have
#### Candidates so far:
candidate | pros | cons
--- | --- | --- |
`curses` | makes sense | color doesn't work well, 
`urwid` | automatic structuring & resize | seems esoteric
`blessings` | automatic structuring & resize | seems esoteric and focused on input
##### See `./terminal_GUI/` files