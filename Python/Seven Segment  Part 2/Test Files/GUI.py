import RPi.GPIO as GPIO
from datetime import datetime
import time
import math

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

# AM/PM Variable
PM = False

#initialize pins to variables
DP = 12
A = 20
B = 16
C = 25
D = 23
E = 18
F = 21
G = 24
Clk1= 11 #Default to display 1
Clk2 = 9
Clk3 = 10
Clk4 = 8
stored_PM = False
global disp_Num
disp_Num = 1#variable controlling which display to set
global disOFF #1 is display off, 0 is display on. Default is display off. NOTE: this does not set it, just tracks if it is on or off
disOFF = 0
H1 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
H2 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
M1 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
M2 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
currentDP = 100



#iniialize GPIOs
def init_pins():
    #sets 4 GPIO inputs as the x values on the keypad
    GPIO.setup(26, GPIO.OUT,  initial=GPIO.LOW) #X1
    GPIO.setup(19, GPIO.OUT,  initial=GPIO.LOW) #X2
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #X3
    GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) #X4

    #sets 4 GPIO inputs as the y values on the keypad
    GPIO.setup(5, GPIO.IN) #Y1
    GPIO.setup(27, GPIO.IN) #Y2
    GPIO.setup(17, GPIO.IN) #Y3
    GPIO.setup(4, GPIO.IN) #Y4

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

    #Cycle clocks to start
    GPIO.output(11, GPIO.HIGH)
    delay(.1)
    GPIO.output(11, GPIO.LOW)

    GPIO.output(9, GPIO.HIGH)
    delay(.1)
    GPIO.output(9, GPIO.LOW)

    GPIO.output(10, GPIO.HIGH)
    delay(0.1)
    GPIO.output(10, GPIO.LOW)

    GPIO.output(8, GPIO.HIGH)
    delay(0.1)
    GPIO.output(8, GPIO.LOW)

#custom delay function
def delay(seconds):
    seconds = seconds*4
    sum = 0
    for i in range(math.ceil(seconds*1666334)):  #number in range has been calculated through experimentation
        sum = sum + 1

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
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 1
    print(disp_Num)

#Displays number 2
def disp_2(disp_Num):
    LED_off()
    GPIO.output([C, F], GPIO.LOW)
    GPIO.output([A, B, G, E, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 2

#Displays number 3
def disp_3(disp_Num):
    LED_off()
    GPIO.output([E, F], GPIO.LOW)
    GPIO.output([A, B, G, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 3

#Displays number 4
def disp_4(disp_Num):
    LED_off()
    GPIO.output([A, D, E], GPIO.LOW)
    GPIO.output([F, G, B, C], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 4

#Displays number 5
def disp_5(disp_Num):
    LED_off()
    GPIO.output([B, E], GPIO.LOW)
    GPIO.output([A, F, G, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 5

#Displays number 6
def disp_6(disp_Num):
    LED_off()
    GPIO.output(B, GPIO.LOW)
    GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 6

#Displays number 7
def disp_7(disp_Num):
    LED_off()
    GPIO.output([F,E, G, D], GPIO.LOW)
    GPIO.output([A, B, C], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 7

#Displays number 8
def disp_8(disp_Num):
    LED_off()
    GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 8

#Displays number 9
def disp_9(disp_Num):
    LED_off()
    GPIO.output(E, GPIO.LOW)
    GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 9

#Displays number 0
def disp_0(disp_Num):
    LED_off()
    GPIO.output([G, DP], GPIO.LOW)
    GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    return 0

def flash(disp_Num):
    GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    delay(0.01)
    GPIO.output([A, F, G, B, C, D, E], GPIO.LOW)
    GPIO.output(setClock(disp_Num),GPIO.HIGH)
    delay(0.1)
    GPIO.output(setClock(disp_Num), GPIO.LOW)
    delay(0.01)

#Displays current value
def disp_current():  #took out currentDP
    global currentDP
    global H1
    global H2
    global M1
    global M2
    if H1==1:
        disp_1(1)
    if H1==2:
        disp_2(1)
    if H1==3:
        disp_3(1)
    if H1==4:
        disp_4(1)
    if H1==5:
        disp_5(1)
    if H1==6:
        disp_6(1)
    if H1==7:
        disp_7(1)
    if H1==8:
        disp_8(1)
    if H1==9:
        disp_9(1)
    if H1==0:
        disp_0(1)
    if H2==1:
        disp_1(2)
    if H2==2:
        disp_2(2)
    if H2==3:
        disp_3(2)
    if H2==4:
        disp_4(2)
    if H2==5:
        disp_5(2)
    if H2==6:
        disp_6(2)
    if H2==7:
        disp_7(2)
    if H2==8:
        disp_8(2)
    if H2==9:
        disp_9(2)
    if H2==0:
        disp_0(2)
    if M1==1:
        disp_1(3)
    if M1==2:
        disp_2(3)
    if M1==3:
        disp_3(3)
    if M1==4:
        disp_4(3)
    if M1==5:
        disp_5(3)
    if M1==6:
        disp_6(3)
    if M1==7:
        disp_7(3)
    if M1==8:
        disp_8(3)
    if M1==9:
        disp_9(3)
    if M1==0:
        disp_0(3)
    if M2==1:
        disp_1(4)
    if M2==2:
        disp_2(4)
    if M2==3:
        disp_3(4)
    if M2==4:
        disp_4(4)
    if M2==5:
        disp_5(4)
    if M2==6:
        disp_6(4)
    if M2==7:
        disp_7(4)
    if M2==8:
        disp_8(4)
    if M2==9:
        disp_9(4)
    if M2==0:
        disp_0(4)

def shadow_realm():
    
    global currentDP
    global H1
    global H2
    global M1
    global M2
    GPIO.output([A, B, C, D, E, F, G, DP], GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    delay(0.1)
    GPIO.output(11, GPIO.LOW)

    GPIO.output(9, GPIO.HIGH)
    delay(0.1)
    GPIO.output(9, GPIO.LOW)

    GPIO.output(10, GPIO.HIGH)
    delay(0.1)
    GPIO.output(10, GPIO.LOW)

    GPIO.output(8, GPIO.HIGH)
    delay(0.1)
    GPIO.output(8, GPIO.LOW)

    GPIO.output(12,GPIO.LOW)
    while True:
        if readKeypad(6,['*',0,'#','D'])=='#':
            disp_current()
            if(stored_PM):
                GPIO.output(12,GPIO.LOW)
            elif(not(stored_PM)):
                GPIO.output(12,GPIO.HIGH)
            delay(0.5)
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


def setCurrent(num, disp_Num):
    global currentDP
    global H1
    global H2
    global M1
    global M2
   
    if disp_Num==2:
        H1 = num
    elif disp_Num==3:
        H2 = num
    elif disp_Num==4:
        M1 = num
    elif disp_Num==1:
        M2 = num

def single_7SD(disp_Num):
    global stored_PM
    while True:
 
        print("[", H1, "] [", H2, "] [", M1, "] [", M2, "]")
        flash(disp_Num)
        if readKeypad(26,[1,2,3,'A'])==1:
            #call a verify function right here for every valid number
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
            delay(0.5)
            
        if readKeypad(6,['*',0,'#','D'])=='D': 
            disp_D()

    #Turns off the invalid pin LED
def LED_off():
    GPIO.output(7, GPIO.LOW)



#Hour/Minute Display Function Definitions

#displays H1
def disp_H1(hr):

    if hr==1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
        GPIO.output([B, C], GPIO.HIGH)
        GPIO.output(Clk1,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk1, GPIO.LOW)
    if hr==0:
        GPIO.output(G, GPIO.LOW)
        GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
        GPIO.output(Clk1,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk1, GPIO.LOW)
    #displays H1
#displays H2
def disp_H2(min1, AM_PM):
    if AM_PM == True:
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
        
    if min1==0:
        GPIO.output(G, GPIO.LOW)
        GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
        GPIO.output([B, C], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==2:
        GPIO.output([C, F], GPIO.LOW)
        GPIO.output([A, B, G, E, D], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==3:
        GPIO.output([E, F], GPIO.LOW)
        GPIO.output([A, B, G, C, D], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==4:
        GPIO.output([A, D, E], GPIO.LOW)
        GPIO.output([F, G, B, C], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==5:
        GPIO.output([B, E], GPIO.LOW)
        GPIO.output([A, F, G, C, D], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==6:
        GPIO.output(B, GPIO.LOW)
        GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==7:
        GPIO.output([F,E, G, D], GPIO.LOW)
        GPIO.output([A, B, C], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==8:
        GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
    elif min1==9:
        GPIO.output(E, GPIO.LOW)
        GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
        GPIO.output(Clk2,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk2, GPIO.LOW)
#displays M1
def disp_M1(min1):
    if min1==0:
        GPIO.output(G, GPIO.LOW)
        GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
        GPIO.output([B, C], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==2:
        GPIO.output([C, F], GPIO.LOW)
        GPIO.output([A, B, G, E, D], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==3:
        GPIO.output([E, F], GPIO.LOW)
        GPIO.output([A, B, G, C, D], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==4:
        GPIO.output([A, D, E], GPIO.LOW)
        GPIO.output([F, G, B, C], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==5:
        GPIO.output([B, E], GPIO.LOW)
        GPIO.output([A, F, G, C, D], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==6:
        GPIO.output([B], GPIO.LOW)
        GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==7:
        GPIO.output([F,E, G, D], GPIO.LOW)
        GPIO.output([A, B, C], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==8:
        GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
    elif min1==9:
        GPIO.output(E, GPIO.LOW)
        GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
        GPIO.output(Clk3,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk3, GPIO.LOW)
#displays M2
def disp_M2(min1):
    if min1==0:
        GPIO.output(G, GPIO.LOW)
        GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
        GPIO.output([B, C], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==2:
        GPIO.output([C, F], GPIO.LOW)
        GPIO.output([A, B, G, E, D], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==3:
        GPIO.output([E, F], GPIO.LOW)
        GPIO.output([A, B, G, C, D], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==4:
        GPIO.output([A, D, E], GPIO.LOW)
        GPIO.output([F, G, B, C], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==5:
        GPIO.output([B, E], GPIO.LOW)
        GPIO.output([A, F, G, C, D], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==6:
        GPIO.output(B, GPIO.LOW)
        GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==7:
        GPIO.output([F,E, G, D], GPIO.LOW)
        GPIO.output([A, B, C], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==8:
        GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)
    elif min1==9:
        GPIO.output(E, GPIO.LOW)
        GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
        GPIO.output(Clk4,GPIO.HIGH)
        delay(0.1)
        GPIO.output(Clk4, GPIO.LOW)


#Mode Function Definitions

#Automatic Mode
def Auto():
    # local variable to keep count of how many times B has been pressed in Auto
    bees = 0
    print("You are in Auto Mode") #prints mode into terminal
    while True:
        #checks for how manytimes B has been pressed
        if readKeypad(19,[4,5,6,'B'])=='B':
            bees = bees + 1
        if bees >= 3:
            break

        #sets variable now to datetime data 
        now = datetime.now()
        
        #takes current hour and removes military time, stores it in variable hour_not_military
        hour_not_military = now.hour
        if now.hour > 12:
            hour_not_military -= 12
            PM = True
        else:
            PM = False

        #stores minute into variable at an integer
        minute_int = now.minute

        #takes hour and minute integer and converts to 2 digit string
        hour='{0:02d}'.format(hour_not_military)
        minute='{0:02d}'.format(minute_int)

        #sets each segment to correct hour or minute value
        H1 = int(hour[0])
        H2 = int(hour[1])
        M1 = int(minute[0])
        M2 = int(minute[1])

        #For print purpose only, to show AM or PM as dot below
        if PM==True:
            dot = "*"
        else:
            dot = " "

        print(H1, H2, dot, ":", M1, M2)
        delay(0.33)

        disp_H1(H1)
        disp_H2(H2, PM)
        disp_M1(M1)
        disp_M2(M2)

#Manual Mode
def Manual():
    bees = 0
    print("You are in Manual Mode") #prints mode into terminal
    while True:
    
        #checks for how manytimes B has been pressed
        if readKeypad(19,[4,5,6,'B'])=='B':
            bees = bees + 1
        if bees >= 3:
            break
        delay(.33)
    #Manual code will go here once it is finished

#Menu Function
def Menu():

    while True:
        print("Awating Mode Selection")
        disp_H1(0)
        disp_H2(0, False)
        disp_M1(0)
        disp_M2(0)
        if readKeypad(26,[1,2,3,'A'])=='A':
            Auto()
        elif readKeypad(19,[4,5,6,'B'])=='B':
            Manual()
        delay(.5)


    





#sets up GPIO PINS
init_pins()
Menu()
