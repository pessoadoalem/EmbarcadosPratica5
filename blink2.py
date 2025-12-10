import time
import RPi.GPIO as GPIO

PIN2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN2, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN2, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(PIN2, GPIO.LOW)
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
