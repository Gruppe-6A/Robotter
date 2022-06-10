import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) # Power to transistor
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


def c_out():
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)

def c_in():
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    
def off():
    GPIO.output(26, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)

def p_card():
    c_out()
    time.sleep(1)
    c_in()
    time.sleep(1)
    off()

def d_card():
    c_out()
    time.sleep(1)
    c_in()
    time.sleep(1)
    off()
