#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.HIGH)

time.sleep(2)

GPIO.cleanup()
