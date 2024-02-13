import RPi.GPIO as GPIO
import time

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

#set DP to off
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # CLOCK -> GPIO 11 (SPICLOCK)
Clk = 11

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 1 -> 7SD 1 (E) -> GPIO 18
E = 18

GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 2 -> 7SD 2 (D) -> GPIO 23 
D = 23

GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 3 -> 7SD 4 (C) -> GPIO 25
C = 25

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 5 -> 7SD 6 (B) -> GPIO 16
B = 16

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 6 -> 7SD 7 (A) -> GPIO 20
A = 20

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 7 -> 7SD 9 (F) -> GPIO 21
F = 21

GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 8 -> 7SD 10 (G) -> GPIO 24
G = 24

#GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # ENABLE -> GPIO 22

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
    if readKeypad(26,[1,2,3,'A'])==1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
        GPIO.output([B, C], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(26,[1,2,3,'A'])==2:
        GPIO.output([C, F], GPIO.LOW)
        GPIO.output([A, B, G, E, D], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(26,[1,2,3,'A'])==3:
        GPIO.output([E, F], GPIO.LOW)
        GPIO.output([A, B, G, C, D], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(26,[1,2,3,'A'])=='A':
        GPIO.output([D], GPIO.LOW)
        GPIO.output([A, B, F, G, E, C], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(19,[4,5,6,'B'])==4:
        GPIO.output([A, D, E], GPIO.LOW)
        GPIO.output([F, G, B, C], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(19,[4,5,6,'B'])==5:
        GPIO.output([B, E], GPIO.LOW)
        GPIO.output([A, F, G, C, D], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(19,[4,5,6,'B'])==6:
        GPIO.output(B, GPIO.LOW)
        GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(19,[4,5,6,'B'])=='B':
        GPIO.output([A, B], GPIO.LOW)
        GPIO.output([F, G, C, D, E], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(13,[7,8,9,'C'])==7:
        GPIO.output([D, E, F, G], GPIO.LOW)
        GPIO.output([A, B, C], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(13,[7,8,9,'C'])==8:
        GPIO.output([A, B, C, D, E, F, G], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(13,[7,8,9,'C'])==9:
        GPIO.output(E, GPIO.LOW)
        GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(13,[7,8,9,'C'])=='C':
        GPIO.output([B, C, G], GPIO.LOW)
        GPIO.output([A, F, E, D], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(6,['*',0,'#','D'])=='*':
        GPIO.output([A, B, C, D, E, F, G], GPIO.LOW)
        #GPIO.output([], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(6,['*',0,'#','D'])==0:
        GPIO.output(G, GPIO.LOW)
        GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(6,['*',0,'#','D'])=='#':
        count = 0
        if count%2==0:
            GPIO.output()
            count = count + 1
        if count%2==1:
            GPIO.output()
            count = count + 1

        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)
    if readKeypad(6,['*',0,'#','D'])=='D':
        GPIO.output([A, F], GPIO.LOW)
        GPIO.output([B, G, E, D, C], GPIO.HIGH)
        GPIO.output(Clk,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(Clk, GPIO.LOW)