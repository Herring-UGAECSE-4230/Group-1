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
global disp_Num
disp_Num = 1 #variable controlling which display to set
exit_manual = 0 #variable controlling whether or not the program leaves manual mode
B_Count = 0 #variable counting up to three in order to set exit_manual == 1

H1 = 100 #Tracks Hour 1, used to set display and reset the display to what it was set to previously for '#'
H2 = 100 #Tracks Hour 2, used to set display and reset the display to what it was set to previously for '#'
M1 = 100 #Tracks Minute 1, used to set display and reset the display to what it was set to previously for '#'
M2 = 100 #Tracks Minute 2, used to set display and reset the display to what it was set to previously for '#'
currentDP = 100 #Tracks if the time is AM or PM

military_H1 = 100 #Tracks Hour 1 in military time
military_H2 = 100 #Tracks Hour 2 in military time

#Credit: All
def runManual(): #Manual Mode code
    global disp_Num; global exit_manual; global B_Count; global H1; global H2; global M1; global M2; global currentDP
    B_Count = 0; exit_manual = 0; currentDP = 100

    #Turns off the invalid pin LED
    #Credit: All
    def LED_off():
        GPIO.output(7, GPIO.LOW)
    
    #wheel of time: controls how the variables update every time a minute passes. Keeps H1, H2, M1, M2 and DP within valid ranges by incrementing them at appropriate times.
    #Credit: Nathan
    def wheel_of_time():

        
        global H1; global H2; global M1; global M2; global currentDP; global B_Count
        print("enter Wheel of time")
    
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
                        if H2 == 1:
                            if currentDP == 0:
                                currentDP = 1
                            elif currentDP == 1:
                                currentDP = 0
                        H2 += 1
                    elif H2 == 2:
                        H2 = 1
                        H1 = 0
        print("exit Wheel of time")

    #returns the clock GPIO based on a display input. Credit: Lucas
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
    #Credit: All
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

    #runs when hashtag is pressed. Shuts off all displays until hashtag is pressed again, at which point the values are restored. Credit: Nathan and Lucas
    def shadow_realm():
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
                print("exiting realm")
                disp_current()
                break            
    
    #returns the next display to set based on input 
    def nextDisp(num):
        print("The function nextDisp has begun")
        global exit_manual
        if num==1:
            print("Now pointing to display 2")
            GPIO.output(7, GPIO.LOW) #turn off LED
            return 2
            
        elif num==2:
            print("Now pointing to display 3")
            return 3
            
        elif num==3:
            print("Now pointing to display 4")
            return 4
            
        elif num==4:
            tracktime()
            print("Finished!")
            exit_manual = 1
            return 1
        
    #Displays: Credit: All
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

    #Flashes current display on and off. Credit: All
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

    #Displays all the stored H1, H2, M1, M2, currentDP values on displays 1, 2, 3, 4, and DP. Credit: Nathan and Lucas
    def disp_current():
        print("The current variables should be displayed now.")
        global currentDP; global H1; global H2; global M1; global M2
        timevals = [[H1,1], [H2,2], [M1,3], [M2,4]]
        for t in timevals:
            if t[0]==1:
                disp_1(t[1])
            if t[0]==2:
                disp_2(t[1])
            if t[0]==3:
                disp_3(t[1])
            if t[0]==4:
                disp_4(t[1])
            if t[0]==5:
                disp_5(t[1])
            if t[0]==6:
                disp_6(t[1])
            if t[0]==7:
                disp_7(t[1])
            if t[0]==8:
                disp_8(t[1])
            if t[0]==9:
                disp_9(t[1])
            if t[0]==0:
                disp_0(t[1])
        if currentDP==1:
            GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
        if currentDP==0:
            GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

    #tracking mode after time is input manually. Credit: Nathan
    def tracktime(): 
        global H1; global H2; global M1; global M2; global currentDP;  global B_Count #list global variables
        print("Tracktime is Executing")
        while True:
            for n in range(120):
                time.sleep(.5)
                if readKeypad(19,[4,5,6,'B'])=='B': #increase B count when B is pressed
                    B_Count += 1
                    print(B_Count)
                if readKeypad(6,['*',0,'#','D'])=='#': #enter shadow realm when # is pressed
                    print("entering realm")
                    shadow_realm()
                if B_Count >= 3:
                    print("return to GUI")
                    break #leave tracktime, ultimately breaks the infinite loop running the function
            wheel_of_time() #update variables
            disp_current() #update displays
            if B_Count >= 3:
                print("return to GUI")
                H1 = 100 
                H2 = 100 
                M1 = 100 
                M2 = 100 
                currentDP = 100
                break #leave tracktime, ultimately breaks the infinite loop running the function

    #verifies that values returned from read keypad are valid for their display. Updates variables and returns True or False. Credit: Nathan
    def verify(disp_Num, curVal):
        global H1; global H2; global M1; global military_H1; global military_H2; global currentDP
        print("You just pressed", curVal)
        print("We are filling Display #", disp_Num)
        print("H1 is currently equal to", H1)
        print("Verification Begun")
        if disp_Num == 1:
            print("Display 1")
            if curVal == 0:
                H1 = 0
                currentDP = 0
                return True
            elif curVal == 1:
                military_H1 = 1
                return True
            elif curVal == 2:
                military_H1 = 2
                print("Military_H1 = ",military_H1)
                return True
            else: # curVal == (3 or 4 or 5 or 6 or 7 or 8 or 9):
                print("bad number")
                return False
        elif disp_Num == 2:
            if H1 == 0:
                if curVal == 0:
                    H1 = 1
                    H2 = 2
                    return True
                else:
                    H2 = curVal
                    return True
            if military_H1 == 1:
                if curVal < 2:
                    if curVal == 0:
                        H1 = 1
                        H2 = 0
                    if curVal == 1:
                        H1 = 1
                        H2 = 1
                    currentDP = 0
                else:
                    if curVal == 2:
                        H1 = 1
                        H2 = 2
                    elif curVal == 3:
                        H1 = 0
                        H2 = 1
                    elif curVal == 4:
                        H1 = 0
                        H2 = 2
                    elif curVal == 5:
                        H1 = 0
                        H2 = 3
                    elif curVal == 6:
                        H1 = 0
                        H2 = 4
                    elif curVal == 7:
                        H1 = 0
                        H2 = 5
                    elif curVal == 8:
                        H1 = 0
                        H2 = 6
                    elif curVal == 9:
                        H1 = 0
                        H2 = 7
                    currentDP = 1
                return True
            elif military_H1 == 2:
                if curVal < 4:
                    if curVal == 0:
                        H1 = 0
                        H2 = 8
                    elif curVal == 1:
                        H1 = 0
                        H2 = 9
                    elif curVal == 2:
                        H1 = 1
                        H2 = 0
                    elif curVal == 3:
                        H1 = 1
                        H2 = 1
                    currentDP = 1
                    return True
                else:
                    print("bad number")
                    return False
        elif disp_Num == 3:
            if curVal == 0 or curVal == 1 or curVal == 2 or curVal == 3 or curVal == 4 or curVal == 5:
                return True
            else: # curVal == 6 or 7 or 8 or 9:
                print("bad number")
                return False

    #moves pointer around so the program knows which display to update next. Credit: Lucas
    def setCurrent(num, disp_Num):
        print("setcurrent")
        global currentDP; global H1; global H2; global M1; global M2
        print(disp_Num)
    
        if disp_Num==1:
            H1 = num
        elif disp_Num==2:
            H2 = num
        elif disp_Num==3:
            M1 = num
        elif disp_Num==4:
            M2 = num

    #verifies, updates variables, and displays any numeric input
    #lights invalid LED for invalid numeric inputs, star, and letters
    #enters the shadow realm for '#' inputs 
    #loop broken if exit_manual == 1, eventually breaking the runManual infinite loop
    def single_7SD(disp_Num): #Credit: All
        global H1; global exit_manual
        while True:
            #print("[", H1, "] [", H2, "] [", M1, "] [", M2, "]")
            flash(disp_Num)
            if readKeypad(26,[1,2,3,'A'])==1:
                if verify(disp_Num,1) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_1(disp_Num) == 1:
                            setCurrent(1, disp_Num)
                            disp_Num = nextDisp(disp_Num)                  
            if readKeypad(26,[1,2,3,'A'])==2:
                if verify(disp_Num,2) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_2(disp_Num) == 2:
                            setCurrent(2, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(26,[1,2,3,'A'])==3:
                if verify(disp_Num,3) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_3(disp_Num) == 3:
                            setCurrent(3, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(26,[1,2,3,'A'])=='A':
                disp_A()
            if readKeypad(19,[4,5,6,'B'])==4:
                if verify(disp_Num,4) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_4(disp_Num) == 4:
                            setCurrent(4, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])==5:
                if verify(disp_Num,5) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_5(disp_Num) == 5:
                            setCurrent(5, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])==6:
                if verify(disp_Num,6) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_6(disp_Num) == 6:
                            setCurrent(6, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(19,[4,5,6,'B'])=='B':
                disp_B()
            if readKeypad(13,[7,8,9,'C'])==7:
                if verify(disp_Num,7) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_7(disp_Num) == 7:
                            setCurrent(7, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(13,[7,8,9,'C'])==8:
                if verify(disp_Num,8) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_8(disp_Num) == 8:
                            setCurrent(8, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(13,[7,8,9,'C'])==9:
                if verify(disp_Num,9) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
                    else:
                        if disp_9(disp_Num) == 9:
                            setCurrent(9, disp_Num)
                            disp_Num = nextDisp(disp_Num)
            if readKeypad(13,[7,8,9,'C'])=='C':
                disp_C()
            if readKeypad(6,['*',0,'#','D'])=='*':
                disp_C()
            if readKeypad(6,['*',0,'#','D'])==0:
                if verify(disp_Num,0) == False:
                    disp_C()
                else:
                    if disp_Num == 1:
                        if disp_0(disp_Num) == 0:
                            setCurrent(0, disp_Num)
                            disp_Num = nextDisp(disp_Num) 
                    elif disp_Num == 2:
                        disp_current()
                        disp_Num = nextDisp(disp_Num)
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
    
    init_pins()
    #run single_7SD until loop breaks, causing the file to terminate. Credit: All
    while True:
        single_7SD(disp_Num)
        break