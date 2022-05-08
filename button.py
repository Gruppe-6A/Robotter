import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Power
GPIO.setup(27, GPIO.IN) # Input button 1
GPIO.setup(27, GPIO.IN) # Input button 2
GPIO.output(17, GPIO.HIGH) # Turn ON power


def button_1():
    if GPIO.input(27) == 0:
        return True
    else:
        return False

def button_2():
    if GPIO.input(27) == 0:
        return True
    else:
        return False

#GPIO.cleanup()