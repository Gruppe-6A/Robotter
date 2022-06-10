import RPi.GPIO as GPIO
import time

current_degree = 0
stepper = 5
dir = 6

ms1 = 16
ms2 = 20
ms3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(stepper, GPIO.OUT) #Stepper pin
GPIO.setup(dir, GPIO.OUT) #Direction pin
GPIO.setup(ms1, GPIO.OUT) #Micro step 1
GPIO.setup(ms2, GPIO.OUT) #Micro step 2
GPIO.setup(ms3, GPIO.OUT) #Micro step 3

#Set stepsize to 1/16 (0,1125 degrees)
GPIO.output(ms1, GPIO.HIGH)
GPIO.output(ms2, GPIO.HIGH)
GPIO.output(ms3, GPIO.HIGH)

def step(clock_wise, degree, rpm):
    global current_degree
    GPIO.output(dir, GPIO.LOW) 
    if (clock_wise == False):
        GPIO.output(dir, GPIO.HIGH)
        current_degree -= degree
    else:
        current_degree += degree
    if degree != 0:
        pause = (((degree/360)/rpm)/(degree*16))*60
    else:
        pause = 0
    moved = 0;
    while(moved < degree):
        
        GPIO.output(stepper, GPIO.HIGH)
        time.sleep(pause/2)
        
        GPIO.output(stepper, GPIO.LOW)
        time.sleep(pause/2)
        moved += 1.8*(1/16)

def go_to_pos(degree, rpm):
    global current_degree
    diff = current_degree - degree
    if diff < 0:
        step(True, abs(diff), rpm)
    else:
        step(False, abs(diff), rpm)
#go_to_pos(-30, 4)
#print(current_degree)
#time.sleep(1)
#go_to_pos(-90, 5)
#print(current_degree)
#GPIO.cleanup()