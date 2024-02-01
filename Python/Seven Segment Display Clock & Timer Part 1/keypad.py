import RPi.GPIO as GPIO
from time import sleep

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT) #X1
GPIO.setup(19, GPIO.OUT) #X2
GPIO.setup(13, GPIO.OUT) #X3
GPIO.setup(6, GPIO.OUT) #X4

GPIO.setup(5, GPIO.IN) #Y1
GPIO.setup(27, GPIO.IN) #Y2
GPIO.setup(17, GPIO.IN) #Y3
GPIO.setup(4, GPIO.IN) #Y4

def readKeypad(rowNum,char):
    curVal = 0
    GPIO.output(rowNum,GPIO.HIGH)
    if GPIO.input(5)==1: #check Y1
        curVal=char[0]
        print(curVal)
    if GPIO.input(27)==1: #check Y2
        curVal=char[1]
        print(curVal)
    if GPIO.input(17)==1: #check Y3
        curVal=char[2]
        print(curVal)
    if GPIO.input(4)==1: #check Y4
        curVal=char[3]
        print(curVal)
    GPIO.output(rowNum,GPIO.LOW)
    return curVal

while True:
    readKeypad(26,[1,2,3,'A'])
    sleep(.03)
    readKeypad(19,[4,5,6,'B'])
    sleep(.03)
    readKeypad(13,[7,8,9,'C'])
    sleep(.03)
    readKeypad(6,['*',0,'#','D'])
    sleep(.03)