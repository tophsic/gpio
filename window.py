#!/usr/bin/python

import curses
import signal
import sys
from lib.gpio import Monitoring
from lib.counter import Counter


def main(stdscr):
    global screen, counter
    screen = stdscr

    maxyx = screen.getmaxyx()

    subscreen = stdscr.subwin(maxyx[0], maxyx[1], 0, 0)
    subscreen.box()
    subscreen.refresh()

    gpioMonitoring = Monitoring(screen)
    counter = Counter(subscreen)
    counter.start()

    def sigint_handler(signum, frame):
        counter.stop()
        exit(0)
            
    signal.signal(signal.SIGINT, sigint_handler)


    while True:
        c = subscreen.getch()
        if c != -1:
            # print numeric value
            subscreen.addstr(2, 1, str(c))

        subscreen.refresh()
        pass


if __name__ == '__main__':
    curses.wrapper(main)

