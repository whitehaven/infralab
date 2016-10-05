import curses

from cryOSHardware import cryOSHardwareSet

offset_down = 1
offset_right = 3

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

test_hardware = cryOSHardwareSet()

test_hardware.add_temp_sensor('hot side', diagram_location=5)
test_hardware.add_temp_sensor('cold side', diagram_location=4)

choice = None
while choice != 'q':
    for line_number, line_contents in enumerate(test_hardware.diagram):
        stdscr.addstr(line_number + offset_down, offset_right, line_contents)

    for sensor in test_hardware.temp_sensors:
        stdscr.addstr(sensor.diagram_location + offset_down, offset_right + len(test_hardware.diagram[0]),
                      str(sensor.description) + ": " + str(float(sensor.temp)))

    choice = stdscr.getkey()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
