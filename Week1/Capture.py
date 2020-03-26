import os
import time
import RPi.GPIO as GPIO

time.sleep(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down = GPIO.PUD_UP)
print"=====================Ready================="

while True:
    if(GPIO.input(12)==0):
        GPIO.output(11,GPIO.HIGH)
        timestr = time.strftime("/home/pi/xCapture/%Y%m%d-%H%M%S.jpg")
        print"Capture"
        print('%s'%timestr)
        os.system('fswebcam -p YUYV -d /dev/video0 -r 640x480 %s'%timestr)
        time.sleep(4)
        GPIO.output(11,GPIO.LOW)
        time.sleep(1)
        print"------------------------"
