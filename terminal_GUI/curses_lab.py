import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

diagram = ('  ||     ||  ',
           '  ||     ||  ',
           '  ||     ||  ',
           '  =========  ',
           ' +---------+ ',
           ' +---------+ ',
           '  | | | | |  ',
           '    | | |    ',
           '    | | |    ',
           '      |      ',
           '      |      '
           )

# TODO:  add temperature sensors that have random positions

for line_number, line_contents in enumerate(diagram):
    stdscr.addstr(line_number, 2, line_contents)

stdscr.getkey()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
