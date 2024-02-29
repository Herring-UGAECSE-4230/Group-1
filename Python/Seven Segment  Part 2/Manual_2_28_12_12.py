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

# cycling clocks
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

#Code Above is repeated in GUI2
#-------------------------------------------------------------------------------------
#Code Below will be part of runManual() function
stored_PM = False
global disp_Num
disp_Num = 1 #variable controlling which display to set
exit_manual = 0
B_Count = 0

H1 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
H2 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
M1 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
M2 = 100 #Tracks what display is set to, used to reset the display to what it was set to previously for '#'
currentDP = 100

def runManual():
    global stored_PM
    global disp_Num
    global exit_manual
    global B_Count
    B_Count = 0
    exit_manual = 0

    global H1
    global H2
    global M1
    global M2
    global currentDP
    currentDP = 100

    #wheel of time rules
    def wheel_of_time():
        print("enter Wheel of time")
        global H1
        global H2
        global M1
        global M2
        global currentDP
        print(H1,H2,M1,M2,currentDP)
        if M2 < 9:
            M2 = M2 + 1
        elif M2 == 9:
            M2 = 0
            if M1 < 5:
                M1 += 1
            elif M1 == 5:
                M1 = 0
                if H1 == 0:
                    if H2 < 9:
                        H2 += 1
                    elif H2 == 9:
                        H2 = 0
                        H1 = 1
                elif H1 == 1:
                    if H2 < 2:
                        H2 += 1
                        if currentDP == 0:
                            currentDP = 1
                        elif currentDP == 1:
                            currentDP = 0
                    elif H2 == 2:
                        H2 = 1
                        H1 = 0
        print("exit Wheel of time")

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
   
    def shadow_realm():
        
        global currentDP
        global H1
        global H2
        global M1
        global M2
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
                    currentDP = 0
                elif(not(stored_PM)):
                    GPIO.output(12,GPIO.HIGH)
                    currentDP = 1
                time.sleep(0.5)
                break            
    
    def tracktime():
        print("Enter Tracktime")
        global B_Count
        while True: #this is not working but I want the display to freeze here.
            for n in range(1):
                time.sleep(.5)
                if readKeypad(19,[4,5,6,'B'])=='B': 
                    B_Count += 1
                    print(B_Count)
                if readKeypad(6,['*',0,'#','D'])=='#': 
                    shadow_realm()

            if B_Count == 3:
                print("return to GUI")
                break
            wheel_of_time()
            disp_current()

    #returns the next display to set based on input 
    def nextDisp(num):
        print("Enter nextDisp")
        global exit_manual
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
            tracktime()
            print("changed to 1")
            exit_manual = 1
            return 1
        
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
        print("disp_current")
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
        if currentDP==1:
                GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)

    def verify(disp_Num, curVal, H1):
        print("curval", curVal)
        print("disp num", disp_Num)
        print("h1", H1)
        print("verify")
        if disp_Num == 1:
            if curVal == 0 or curVal==1:
                return True
            else: # curVal == (2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
                print("bad number")
                return False
        if disp_Num == 2:
            if H1 == 0:
                if curVal == 0:
                    print("bad number")
                    return False
                else:
                    return True
            if H1 == 1:
                if curVal == 0 or curVal == 1 or curVal == 2:
                    return True
                else: # curVal == 3 or 4 or 5 or 6 or 7 or 8 or 9:
                    print("bad number")
                    return False
        if disp_Num == 3:
            if curVal == 0 or curVal == 1 or curVal == 2 or curVal == 3 or curVal == 4 or curVal == 5:
                return True
            else: # curVal == 6 or 7 or 8 or 9:
                print("bad number")
                return False




    def setCurrent(num, disp_Num):
        print("setcurrent")
        global currentDP
        global H1
        global H2
        global M1
        global M2
        print(disp_Num)
    
        if disp_Num==1:
            H1 = num
        elif disp_Num==2:
            H2 = num
        elif disp_Num==3:
            M1 = num
        elif disp_Num==4:
            M2 = num

    def single_7SD(disp_Num):
        global stored_PM
        global H1
        global exit_manual
        while True:
    
            print("[", H1, "] [", H2, "] [", M1, "] [", M2, "]")
            flash(disp_Num)
            if readKeypad(26,[1,2,3,'A'])==1:
                if verify(disp_Num,1,H1) == False:
                    disp_C()
                else:
                    if disp_1(disp_Num) == 1:
                        setCurrent(1, disp_Num)
                        disp_Num = nextDisp(disp_Num)                  
            if readKeypad(26,[1,2,3,'A'])==2:
                if verify(disp_Num,2,H1) == False:
                    disp_C()
                else:
                    if disp_2(disp_Num) == 2:
                        setCurrent(2, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(26,[1,2,3,'A'])==3:
                if verify(disp_Num,3,H1) == False:
                    disp_C()
                else:
                    if disp_3(disp_Num) == 3:
                        setCurrent(3, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(26,[1,2,3,'A'])=='A':
                disp_A()
            if readKeypad(19,[4,5,6,'B'])==4:
                if verify(disp_Num,4,H1) == False:
                    disp_C()
                else:
                    if disp_4(disp_Num) == 4:
                        setCurrent(4, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])==5:
                if verify(disp_Num,5,H1) == False:
                    disp_C()
                else:
                    if disp_5(disp_Num) == 5:
                        setCurrent(5, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])==6:
                if verify(disp_Num,6,H1) == False:
                    disp_C()
                else:
                    if disp_6(disp_Num) == 6:
                        setCurrent(6, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])=='B':
                disp_B()
            if readKeypad(13,[7,8,9,'C'])==7:
                if verify(disp_Num,7,H1) == False:
                    disp_C()
                    print("bad number reognized")
                else:
                    print("number passed verification")
                    if disp_7(disp_Num) == 7:
                        setCurrent(7, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(13,[7,8,9,'C'])==8:
                if verify(disp_Num,8,H1) == False:
                    disp_C()
                else:
                    if disp_8(disp_Num) == 8:
                        setCurrent(8, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(13,[7,8,9,'C'])==9:
                if verify(disp_Num,9,H1) == False:
                    disp_C()
                else:
                    if disp_9(disp_Num) == 9:
                        setCurrent(9, disp_Num)
                        disp_Num = nextDisp(disp_Num)
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
                if verify(disp_Num,0,H1) == False:
                    disp_C()
                else:
                    if disp_0(disp_Num) == 0:
                        setCurrent(0, disp_Num)
                        disp_Num = nextDisp(disp_Num)
            if readKeypad(6,['*',0,'#','D'])=='#': #Credit: Code wrote by Lucas, Tested and improved by all members
                
                shadow_realm()
                time.sleep(0.5)
                
            if readKeypad(6,['*',0,'#','D'])=='D': 
                disp_D()

            if exit_manual == 1:
                print("go back")
                break
    

        #Turns off the invalid pin LED
    def LED_off():
        GPIO.output(7, GPIO.LOW)

    #sets up GPIO PINS
    #REMOVE FOR RUNMANUAL() IMPLEMENTATION
    init_pins()

    while True:
        single_7SD(disp_Num)
        
        break