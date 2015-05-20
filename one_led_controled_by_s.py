#!/usr/bin/python

import curses
import sys
import RPi.GPIO as GPIO

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)

    initGPIO()

    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c))
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)
        if c == 97:
            GPIO.cleanup()
            sys.exit('Bye bye')
        elif c == 117:
            lightToggle()
        elif c == 114:
            light()


def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(8, GPIO.OUT)



def lightToggle():
    GPIO.output(8, not GPIO.input(8))


def light():
    GPIO.output(8, GPIO.HIGH)


def dark():
    GPIO.output(8, GPIO.LOW)


if __name__ == '__main__':
    curses.wrapper(main)
