import RPi.GPIO as GPIO
from datetime import datetime
import time
from Auto import runAuto

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)


#initialize pins to variables
DP = 12
A = 20
B = 16
C = 25
D = 23
E = 18
F = 21
G = 24
Clk1 = 11
Clk2 = 9
Clk3 = 10
Clk4 = 8

def init_pins():
    #iniialize GPIOs
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) #DP
    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #E
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) #D
    GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) #C
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #B
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) #A
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) #F
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) #G
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # CLOCK 1 (H1)
    GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW) # Clock 2 (H2)
    GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) #Clock 3 (M1)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #Clock 4 (M2)

    GPIO.setup(26, GPIO.OUT) #X1
    GPIO.setup(19, GPIO.OUT) #X2
    GPIO.setup(13, GPIO.OUT) #X3
    GPIO.setup(6, GPIO.OUT) #X4

    GPIO.setup(5, GPIO.IN) #Y1
    GPIO.setup(27, GPIO.IN) #Y2
    GPIO.setup(17, GPIO.IN) #Y3
    GPIO.setup(4, GPIO.IN) #Y4

    #Cycle clocks to start
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(11, GPIO.LOW)

    GPIO.output(9, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(9, GPIO.LOW)

    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(10, GPIO.LOW)

    GPIO.output(8, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(8, GPIO.LOW)

def readKeypad(rowNum,char):
        curVal = 100 #initial value for keypad output, cant be a number that is on the display
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

def disp_0():
    GPIO.output(G, GPIO.LOW)
    GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
    GPIO.output([Clk1,Clk2,Clk3,Clk4],GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output([Clk1,Clk2,Clk3,Clk4], GPIO.LOW)

init_pins()
while True:
    disp_0()

    if readKeypad(26,[1,2,3,'A'])=='A':
        runAuto(0)

    if readKeypad(19,[4,5,6,'B'])=='B':
        #runManual()
        print()