import time
import RPi.GPIO as GPIO
import signal
import sys

PIN1 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)

running = True

def stop(signum, frame):
    global running
    running = False

signal.signal(signal.SIGTERM, stop)

while running:
    GPIO.output(PIN1, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(PIN1, GPIO.LOW)
    time.sleep(0.3)

GPIO.cleanup()
