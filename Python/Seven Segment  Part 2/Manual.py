import RPi.GPIO as GPIO #import RPi
import time #import Time for delays

#Notes:
#for hashtag currently sets a current for each display, doesnt set them when # is pressed

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)
DP = 12
A = 20
B = 16
C = 25
D = 23
E = 18
F = 21
G = 24
Clk = 11 #Default to display 1
stored_PM = False
global disp_Num
disp_Num = 1#variable controlling which display to set
global disOFF #1 is display off, 0 is display on. Default is display off. NOTE: this does not set it, just tracks if it is on or off
disOFF = 0
current1 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
current2 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
current3 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
current4 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'


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

    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 1 -> 7SD 1 (E) -> GPIO 18

    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 2 -> 7SD 2 (D) -> GPIO 23 

    GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 3 -> 7SD 4 (C) -> GPIO 25

    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 5 -> 7SD 6 (B) -> GPIO 16

    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 6 -> 7SD 7 (A) -> GPIO 20

    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 7 -> 7SD 9 (F) -> GPIO 21

    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 8 -> 7SD 10 (G) -> GPIO 24

    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # CLOCK 1 -> GPIO 11 (SPICLOCK)

    GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW) # Clock display 2

    GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) #Clock display 3

    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #Clock display 4

    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) #invalid LED

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

#returns the clock GPIO based on a display input
def setClock(num):
    if num == 1:
        return 11
    if num == 2:
        return 9
    if num == 3:
        return 10
    if num == 4:
        return 8
    
#returns the next display to set based on input 
def nextDisp(num):
    if num==1:
        print("changed to 2")
        return 2
        
    elif num==2:
        print("changed to 3")
        return 3
        
    elif num==3:
        print("changed to 4")
        return 4
        
    elif num==4:
        return 1
        print("changed to 1")
    
#Displays invalid when A is pressed
def disp_A():
    GPIO.output(7, GPIO.HIGH)

#Displays invalid when B is pressed
def disp_B():
    GPIO.output(7, GPIO.HIGH)

#Displays invalid when C is pressed
def disp_C():
    GPIO.output(7, GPIO.HIGH)

#Displays invalid when D is pressed
def disp_D():
    GPIO.output(7, GPIO.HIGH)


#Displays number 1
def disp_1(disp_Num):
    LED_off()
    GPIO.output([A, D, E, F, G], GPIO.LOW)
    GPIO.output([B, C], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 1
    print(disp_Num)

#Displays number 2
def disp_2(disp_Num):
    LED_off()
    GPIO.output([C, F], GPIO.LOW)
    GPIO.output([A, B, G, E, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 2

#Displays number 3
def disp_3(disp_Num):
    LED_off()
    GPIO.output([E, F], GPIO.LOW)
    GPIO.output([A, B, G, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 3

#Displays number 4
def disp_4(disp_Num):
    LED_off()
    GPIO.output([A, D, E], GPIO.LOW)
    GPIO.output([F, G, B, C], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 4

#Displays number 5
def disp_5(disp_Num):
    LED_off()
    GPIO.output([B, E], GPIO.LOW)
    GPIO.output([A, F, G, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 5

#Displays number 6
def disp_6(disp_Num):
    LED_off()
    GPIO.output(B, GPIO.LOW)
    GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 6

#Displays number 7
def disp_7(disp_Num):
    LED_off()
    GPIO.output([F,E, G, D], GPIO.LOW)
    GPIO.output([A, B, C], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 7

#Displays number 8
def disp_8(disp_Num):
    LED_off()
    GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 8

#Displays number 9
def disp_9(disp_Num):
    LED_off()
    GPIO.output(E, GPIO.LOW)
    GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 9

#Displays number 0
def disp_0(disp_Num):
    LED_off()
    GPIO.output([G, DP], GPIO.LOW)
    GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 0

def flash(disp_Num):
    GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    time.sleep(0.01)
    GPIO.output([A, F, G, B, C, D, E], GPIO.LOW)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    time.sleep(0.01)

#Displays current value
def disp_current():  #took out currentDP
    global currentDP
    global current1
    global current2
    global current3
    global current4
    if current1==1:
        disp_1(1)
    if current1==2:
        disp_2(1)
    if current1==3:
        disp_3(1)
    if current1==4:
        disp_4(1)
    if current1==5:
        disp_5(1)
    if current1==6:
        disp_6(1)
    if current1==7:
        disp_7(1)
    if current1==8:
        disp_8(1)
    if current1==9:
        disp_9(1)
    if current1==0:
        disp_0(1)
    if current2==1:
        disp_1(2)
    if current2==2:
        disp_2(2)
    if current2==3:
        disp_3(2)
    if current2==4:
        disp_4(2)
    if current2==5:
        disp_5(2)
    if current2==6:
        disp_6(2)
    if current2==7:
        disp_7(2)
    if current2==8:
        disp_8(2)
    if current2==9:
        disp_9(2)
    if current2==0:
        disp_0(2)
    if current3==1:
        disp_1(3)
    if current3==2:
        disp_2(3)
    if current3==3:
        disp_3(3)
    if current3==4:
        disp_4(3)
    if current3==5:
        disp_5(3)
    if current3==6:
        disp_6(3)
    if current3==7:
        disp_7(3)
    if current3==8:
        disp_8(3)
    if current3==9:
        disp_9(3)
    if current3==0:
        disp_0(3)
    if current4==1:
        disp_1(4)
    if current4==2:
        disp_2(4)
    if current4==3:
        disp_3(4)
    if current4==4:
        disp_4(4)
    if current4==5:
        disp_5(4)
    if current4==6:
        disp_6(4)
    if current4==7:
        disp_7(4)
    if current4==8:
        disp_8(4)
    if current4==9:
        disp_9(4)
    if current4==0:
        disp_0(4)

def shadow_realm():
    
    global currentDP
    global current1
    global current2
    global current3
    global current4
    GPIO.output([A, B, C, D, E, F, G, DP], GPIO.LOW)
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

    GPIO.output(12,GPIO.LOW)
    while True:
        if readKeypad(6,['*',0,'#','D'])=='#':
            disp_current()
            if(stored_PM):
                GPIO.output(12,GPIO.LOW)
            elif(not(stored_PM)):
                GPIO.output(12,GPIO.HIGH)
            time.sleep(0.5)
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

currentDP = 100
current1 = 100
current2 = 100
current3 = 100
current4 = 100
def setCurrent(num, disp_Num):
    global currentDP
    global current1
    global current2
    global current3
    global current4
   
    if disp_Num==2:
        current1 = num
    elif disp_Num==3:
        current2 = num
    elif disp_Num==4:
        current3 = num
    elif disp_Num==1:
        current4 = num

def single_7SD(disp_Num):
    global stored_PM
    while True:
 
        print("[", current1, "] [", current2, "] [", current3, "] [", current4, "]")
        flash(disp_Num)
        if readKeypad(26,[1,2,3,'A'])==1:
            if disp_1(disp_Num) == 1:
                disp_Num = nextDisp(disp_Num)
            setCurrent(1, disp_Num)
        if readKeypad(26,[1,2,3,'A'])==2:
            if disp_2(disp_Num) == 2:
                disp_Num = nextDisp(disp_Num)
            setCurrent(2, disp_Num)
        if readKeypad(26,[1,2,3,'A'])==3:
            if disp_3(disp_Num) == 3:
                disp_Num = nextDisp(disp_Num)
            setCurrent(3, disp_Num)
        if readKeypad(26,[1,2,3,'A'])=='A':
            disp_A()
        if readKeypad(19,[4,5,6,'B'])==4:
            if disp_4(disp_Num) == 4:
                disp_Num = nextDisp(disp_Num)
            setCurrent(4, disp_Num)
        if readKeypad(19,[4,5,6,'B'])==5:
            if disp_5(disp_Num) == 5:
                disp_Num = nextDisp(disp_Num)
            setCurrent(5, disp_Num)
        if readKeypad(19,[4,5,6,'B'])==6:
            if disp_6(disp_Num) == 6:
                disp_Num = nextDisp(disp_Num)
            setCurrent(6, disp_Num)
        if readKeypad(19,[4,5,6,'B'])=='B':
            disp_B()
        if readKeypad(13,[7,8,9,'C'])==7:
            if disp_7(disp_Num) == 7:
                disp_Num = nextDisp(disp_Num)
            setCurrent(7, disp_Num)
        if readKeypad(13,[7,8,9,'C'])==8:
            if disp_8(disp_Num) == 8:
                disp_Num = nextDisp(disp_Num)
            setCurrent(8, disp_Num)
        if readKeypad(13,[7,8,9,'C'])==9:
            if disp_9(disp_Num) == 9:
                disp_Num = nextDisp(disp_Num)
            setCurrent(9, disp_Num)
            disOFF = 0
        if readKeypad(13,[7,8,9,'C'])=='C':
            disp_C()
        if readKeypad(6,['*',0,'#','D'])=='*':
           
            if stored_PM == True:
                stored_PM = False
                GPIO.output(12,GPIO.HIGH)
            elif stored_PM == False:
                stored_PM = True
                GPIO.output(12,GPIO.LOW)
        if readKeypad(6,['*',0,'#','D'])==0:
            if disp_0(disp_Num) == 0:
                disp_Num = nextDisp(disp_Num)
            setCurrent(0, disp_Num)
            disOFF = 0
        if readKeypad(6,['*',0,'#','D'])=='#': #Credit: Code wrote by Lucas, Tested and improved by all members
            
            shadow_realm()
            time.sleep(0.5)
            
        if readKeypad(6,['*',0,'#','D'])=='D': 
            disp_D()

    #Turns off the invalid pin LED
def LED_off():
    GPIO.output(7, GPIO.LOW)

#sets up GPIO PINS
init_pins()

while True:
    single_7SD(disp_Num)