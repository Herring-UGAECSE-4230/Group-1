import RPi.GPIO as GPIO #method 1: RPi
from time import sleep #sleep allows a pause for x amount of time functions

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

#Sets the initial state to LOW (or off)
GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW)

#Infinite while loop generating square wave
while True:
    #Turns LED on, then waits some time value
    GPIO.output(4,GPIO.HIGH)
    sleep(0.005)

    #Turns LED off, then waits some time value
    GPIO.output(4,GPIO.LOW)
    sleep(0.005)

#Type Ctrl+C to stop progam
