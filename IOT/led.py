import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

try:
    while True:
        print("LED ON")
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.1)
        print("LED OFF")
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.1)
except:
    GPIO.cleanup()