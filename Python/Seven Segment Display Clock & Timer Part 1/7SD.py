import RPi.GPIO as GPIO #import RPi
import time #import Time for delays

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

def init_pins():
    #Credit: All members contributed to GPIO setup
    #Sets 4 gpio outputs for the X values on the keypad
    GPIO.setup(26, GPIO.OUT) #X1
    GPIO.setup(19, GPIO.OUT) #X2
    GPIO.setup(13, GPIO.OUT) #X3
    GPIO.setup(6, GPIO.OUT) #X4

    #sets 4 GPIO inputs as the y values on the keypad
    GPIO.setup(5, GPIO.IN) #Y1
    GPIO.setup(27, GPIO.IN) #Y2
    GPIO.setup(17, GPIO.IN) #Y3
    GPIO.setup(4, GPIO.IN) #Y4

    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) #Decimal Point GPIO 12
    DP = 12

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

#Displays letter 'A'
def disp_A():
    GPIO.output([D, DP], GPIO.LOW)
    GPIO.output([A, B, F, G, E, C], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays letter 'B'
def disp_B():
    GPIO.output([A, B, DP], GPIO.LOW)
    GPIO.output([F, G, C, D, E], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays letter 'C'
def disp_C():
    GPIO.output([B, C, G, DP], GPIO.LOW)
    GPIO.output([A, F, E, D], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays letter 'D'
def disp_D():
    GPIO.output([A, F, DP], GPIO.LOW)
    GPIO.output([B, G, E, D, C], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 1
def disp_1():
    GPIO.output([A, D, E, F, G, DP], GPIO.LOW)
    GPIO.output([B, C], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 2
def disp_2():
    GPIO.output([C, F, DP], GPIO.LOW)
    GPIO.output([A, B, G, E, D], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 3
def disp_3():
    GPIO.output([E, F, DP], GPIO.LOW)
    GPIO.output([A, B, G, C, D], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 4
def disp_4():
    GPIO.output([A, D, E, DP], GPIO.LOW)
    GPIO.output([F, G, B, C], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 5
def disp_5():
    GPIO.output([B, E, DP], GPIO.LOW)
    GPIO.output([A, F, G, C, D], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 6
def disp_6():
    GPIO.output([B, DP], GPIO.LOW)
    GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 7
def disp_7():
    GPIO.output([F,E, G, D, DP], GPIO.LOW)
    GPIO.output([A, B, C], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 8
def disp_8():
    GPIO.output(DP, GPIO.LOW)
    GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 9
def disp_9():
    GPIO.output([E, DP], GPIO.LOW)
    GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays number 0
def disp_0():
    GPIO.output([G, DP], GPIO.LOW)
    GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays decimal point
def disp_DP():
    GPIO.output([A, B, C, D, E, F, G], GPIO.LOW)
    GPIO.output(DP, GPIO.HIGH)
    GPIO.output(Clk,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(Clk, GPIO.LOW)

#Displays current value
def disp_current(current):
    if current==1:
        disp_1()
    if current==2:
        disp_2()
    if current==3:
        disp_3()
    if current==4:
        disp_4()
    if current==5:
        disp_5()
    if current==6:
        disp_6()
    if current==7:
        disp_7()
    if current==8:
        disp_8()
    if current==9:
        disp_9()
    if current==0:
        disp_0()
    if current=='A':
        disp_A()
    if current=='B':
        disp_B()
    if current=='C':
        disp_C()
    if current=='D':
        disp_D()
    if current=='*':
        disp_DP()

def shadow_realm():
    while True:
        if readKeypad(6,['*',0,'#','D'])=='#':
            break

#Credit: Nathan and Lucas wrote. Dawson was not yet in group, but had his own working keypad with previous group
#Readkeypad searches through the Y given which row, then sets the output to the list number using char
#Returns Current Value of the keypad output
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

def single_7SD():
    if readKeypad(26,[1,2,3,'A'])==1:
        disp_1()
        current = 1
        disOFF = 0
    if readKeypad(26,[1,2,3,'A'])==2:
        disp_2()
        current = 2
        disOFF = 0
    if readKeypad(26,[1,2,3,'A'])==3:
        disp_3()
        current = 3
        disOFF = 0
    if readKeypad(26,[1,2,3,'A'])=='A':
        disp_A()
        current = 'A'
        disOFF = 0
    if readKeypad(19,[4,5,6,'B'])==4:
        disp_4()
        current = 4
        disOFF = 0
    if readKeypad(19,[4,5,6,'B'])==5:
        disp_5()
        current = 5
        disOFF = 0
    if readKeypad(19,[4,5,6,'B'])==6:
        disp_6()
        current = 6
        disOFF = 0
    if readKeypad(19,[4,5,6,'B'])=='B':
        disp_B()
        current = 'B'
        disOFF = 0
    if readKeypad(13,[7,8,9,'C'])==7:
        disp_7()
        current = 7
        disOFF = 0
    if readKeypad(13,[7,8,9,'C'])==8:
        disp_8()
        current = 8
        disOFF = 0
    if readKeypad(13,[7,8,9,'C'])==9:
        disp_9()
        current = 9
        disOFF = 0
    if readKeypad(13,[7,8,9,'C'])=='C':
        disp_C()
        current = 'C'
        disOFF = 0
    if readKeypad(6,['*',0,'#','D'])=='*':
        disp_DP()
        current = '*'
        disOFF = 0
    if readKeypad(6,['*',0,'#','D'])==0:
        disp_0()
        current = 0
        disOFF = 0
    if readKeypad(6,['*',0,'#','D'])=='#': #Credit: Code wrote by Lucas, Tested and improved by all members
        if disOFF == 1:
            disp_current(current)
            disOFF = 0
            time.sleep(0.5)
        elif disOFF == 0:
            GPIO.output([A, B, C, D, E, F, G, DP], GPIO.LOW)
            disOFF = 1
            shadow_realm()
            time.sleep(0.5)
    if readKeypad(6,['*',0,'#','D'])=='D': 
        disp_D()
        current = 'D'
        disOFF = 0

init_pins()
disOFF = 1 #1 is display off, 0 is display on. Default is display off. NOTE: this does not set it, just tracks if it is on or off
current = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
while True:
    single_7SD()