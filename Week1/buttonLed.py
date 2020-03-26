import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if (GPIO.input(12)==0):
        GPIO.output(11,GPIO.HIGH)
    else:
        GPIO.output(11,GPIO.LOW)
