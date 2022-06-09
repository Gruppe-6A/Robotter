import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # Power to transistor

def p_card():
    print("player_card")
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.3) #Motor ON duration
    GPIO.output(22, GPIO.LOW)

def d_card():
    print("dealer_card")
    GPIO.output(22, GPIO.HIGH)
    time.sleep(1) #Motor ON duration, move card forward
    GPIO.output(22, GPIO.LOW)
    time.sleep(1) #Motor OFF duration, slow down
    GPIO.output(22, GPIO.HIGH)
    time.sleep(1) #Motor ON duration, eject card at lower speed
    GPIO.output(22, GPIO.LOW)
    
p_card()

#GPIO.cleanup()
