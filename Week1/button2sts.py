import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
xx = 0
while True:
    if (GPIO.input(12)==0 and xx == 0):
        time.sleep(0.2)
        xx = 1
    elif (GPIO.input(12)==0 and xx == 1):
        time.sleep(0.2)
        xx = 0
    if (xx==1):
        GPIO.output(11,GPIO.HIGH)
    elif (xx == 0):
        GPIO.output(11,GPIO.LOW)
