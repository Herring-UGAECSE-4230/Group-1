import RPi.GPIO as GPIO
import time
on = 1

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

freq = input("Define a starting frequency: ")
dc = input("Define a starting Duty Cycle: ")
stat = input("Do you want to change Duty Cycle in loop? 1 or 0: ")

pwm = GPIO.PWM(18,int(freq))
pwm.start(int(dc))



while int(on) :

    on = input("Keep Going? 1 or 0:  ")
    if int(on) != True:
        pwm.stop()  
        break
    freq = input("Define a Frequency: ")
    if (int(stat)):
        dc = input("Define a Duty Cycle: ")
        pwm.ChangeDutyCycle(int(dc))
    
    pwm.ChangeFrequency(int(freq))

pwm.stop()
    
  
