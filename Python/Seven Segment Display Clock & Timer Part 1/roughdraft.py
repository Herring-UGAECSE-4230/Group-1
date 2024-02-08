import RPi.GPIO as GPIO
from time import sleep

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

curVal=''

def gpiosetup():
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

    #initialize GPIO pins
    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 1 -> 7SD 1 (E) -> GPIO 18
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 2 -> 7SD 2 (D) -> GPIO 23 
    GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 3 -> 7SD 4 (C) -> GPIO 25
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 4 -> 7SD 5 (DP) -> GPIO 12
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 5 -> 7SD 6 (B) -> GPIO 16
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 6 -> 7SD 7 (A) -> GPIO 20
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 7 -> 7SD 9 (F) -> GPIO 21
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 8 -> 7SD 10 (G) -> GPIO 24
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # ENABLE -> GPIO 22
    GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH) # CLOCK -> GPIO 11 (SPICLOCK)

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

def sevensegment(a,b,c,d,e,f,g,dp):
    if e==1:
        GPIO.output(18,GPIO.HIGH)
    if d==1:
        GPIO.output(23,GPIO.HIGH)
    if c==1:
        GPIO.output(25,GPIO.HIGH)
    if dp==1:
        GPIO.output(12,GPIO.HIGH)
    if b==1:
        GPIO.output(16,GPIO.HIGH)
    if a==1:
        GPIO.output(20,GPIO.HIGH)
    if f==1:
        GPIO.output(21,GPIO.HIGH)
    if g==1:
        GPIO.output(24,GPIO.HIGH)

def sendOutput(curVal):
    sevensegment(0, 0, 0, 0, 0, 0, 0, 0)
    if curVal==0:
        sevensegment(1,1,1,1,1,1,0,0)
    elif curVal==1:
        sevensegment(0,1,1,0,0,0,0,0)
    elif curVal==2:
        sevensegment(1,1,0,1,1,0,1,0)
    elif curVal==3:
        sevensegment(1,1,1,1,0,0,1,0)
    elif curVal==4:
        sevensegment(0,1,1,0,0,1,1,0)
    elif curVal==5:
        sevensegment(1,0,1,1,0,1,1,0)
    elif curVal==6:
        sevensegment(1,0,1,1,1,1,1,0)
    elif curVal==7:
        sevensegment(1,1,1,0,0,0,0,0)
    elif curVal==8:
        sevensegment(1,1,1,1,1,1,1,0)
    elif curVal==9:
        sevensegment(1,1,1,0,0,1,1,0)
    elif curVal=='A':
        sevensegment(1,1,1,0,1,1,1,0)
    elif curVal=='B':
        sevensegment(0,0,1,1,1,1,1,0)
    elif curVal=='C':
        sevensegment(1,0,0,1,1,1,0,0)
    elif curVal=='D':
        sevensegment(0,1,1,1,1,0,1,0)
    elif curVal=='*': # hash will be explained in main loop. it should change enable
        sevensegment(0,0,0,0,0,0,0,1)


gpiosetup()

count = 0

while True:
    readKeypad(26,[1,2,3,'A'])
    sleep(.03)
    readKeypad(19,[4,5,6,'B'])
    sleep(.03)
    readKeypad(13,[7,8,9,'C'])
    sleep(.03)
    readKeypad(6,['*',0,'#','D'])
    sleep(.03)
    if curVal=='#':
        count = count + 1
        if count%2==1:
            #turn enable on
            GPIO.output(22, GPIO.HIGH)
        else:
            #turn enable off
            GPIO.output(22, GPIO.LOW)

    sendOutput(curVal)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)