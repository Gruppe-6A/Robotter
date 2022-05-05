import RPi.GPIO as GPIO
import time

stepper = 5
dir = 6

ms1 = 16
ms2 = 20
ms3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(ms1, GPIO.OUT)
GPIO.setup(ms2, GPIO.OUT)
GPIO.setup(ms3, GPIO.OUT)

GPIO.output(ms1, GPIO.HIGH)
GPIO.output(ms2, GPIO.HIGH)
GPIO.output(ms3, GPIO.HIGH)

def step(clock_wise, degree, rpm):
    GPIO.output(dir, GPIO.LOW) 
    if (clock_wise == False):
        GPIO.output(dir, GPIO.HIGH)
        
    pause = (((degree/360)/rpm)/(degree*16))*60
    moved = 0;
    while(moved < degree):
        
        GPIO.output(stepper, GPIO.HIGH)
        time.sleep(pause/2)
        
        GPIO.output(stepper, GPIO.LOW)
        time.sleep(pause/2)
        moved += 1.8*(1/16)
step(True, 360 , 20)
GPIO.cleanup()