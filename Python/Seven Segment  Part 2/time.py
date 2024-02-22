import RPi.GPIO as GPIO
from datetime import datetime
import time

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

#sets variable now to datetime data 
now = datetime.now()

PM = False

#takes current hour and removes military time, stores it in variable hour_not_military
hour_not_military = now.hour
if now.hour > 12:
    hour_not_military -= 12
    PM = True

#stores minute into variable at an integer
minute_int = now.minute

#takes hour and minute integer and converts to 2 digit string
hour='{0:02d}'.format(hour_not_military)
minute='{0:02d}'.format(minute_int)

LL = int(hour[0])
LR = int(hour[1])
RL = int(minute[0])
RR = int(minute[1])

if PM==True:
    dot = "*"
else:
    dot = " "

print(LL, LR, dot, ":", RL, RR)