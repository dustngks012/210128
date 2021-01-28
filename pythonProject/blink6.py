import RPi.GPIO as GPIO
import time
led=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)
try:
        while True:
                r=GPIO.input(BUTTON)
                if r==1:
                        GPIO.output(led,True)
                        #time.sleep(1)
                elif r==0:
                        GPIO.output(led,False)
                        #time.sleep(0.1)
except KeyboardInterrupt:
        GPIO.cleanup()
