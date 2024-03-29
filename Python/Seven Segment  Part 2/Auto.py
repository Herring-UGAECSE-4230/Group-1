#Credit: Lucas

import RPi.GPIO as GPIO
from datetime import datetime
import time

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

def runAuto(B_Count):
    def shadow_realm():
        time.sleep(0.4)
        while True:
            if readKeypad(6,['*',0,'#','D'])=='#':
                break
            else:
                GPIO.output([A, B, C, D, E, F, G, DP], GPIO.LOW)
                GPIO.output([Clk1,Clk2,Clk3,Clk4],GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output([Clk1,Clk2,Clk3,Clk4], GPIO.LOW)
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
    #displays H1
    def disp_H1(hr):
        if hr==1:
            GPIO.output([A, D, E, F, G], GPIO.LOW)
            GPIO.output([B, C], GPIO.HIGH)
            GPIO.output(Clk1,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk1, GPIO.LOW)
        if hr==0:
            GPIO.output(G, GPIO.LOW)
            GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
            GPIO.output(Clk1,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk1, GPIO.LOW)
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
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==1:
            GPIO.output([A, D, E, F, G], GPIO.LOW)
            GPIO.output([B, C], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==2:
            GPIO.output([C, F], GPIO.LOW)
            GPIO.output([A, B, G, E, D], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==3:
            GPIO.output([E, F], GPIO.LOW)
            GPIO.output([A, B, G, C, D], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==4:
            GPIO.output([A, D, E], GPIO.LOW)
            GPIO.output([F, G, B, C], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==5:
            GPIO.output([B, E], GPIO.LOW)
            GPIO.output([A, F, G, C, D], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==6:
            GPIO.output(B, GPIO.LOW)
            GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==7:
            GPIO.output([F,E, G, D], GPIO.LOW)
            GPIO.output([A, B, C], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==8:
            GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
        elif min1==9:
            GPIO.output(E, GPIO.LOW)
            GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
            GPIO.output(Clk2,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk2, GPIO.LOW)
    #displays M1
    def disp_M1(min1):
        if min1==0:
            GPIO.output(G, GPIO.LOW)
            GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==1:
            GPIO.output([A, D, E, F, G], GPIO.LOW)
            GPIO.output([B, C], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==2:
            GPIO.output([C, F], GPIO.LOW)
            GPIO.output([A, B, G, E, D], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==3:
            GPIO.output([E, F], GPIO.LOW)
            GPIO.output([A, B, G, C, D], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==4:
            GPIO.output([A, D, E], GPIO.LOW)
            GPIO.output([F, G, B, C], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==5:
            GPIO.output([B, E], GPIO.LOW)
            GPIO.output([A, F, G, C, D], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==6:
            GPIO.output([B], GPIO.LOW)
            GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==7:
            GPIO.output([F,E, G, D], GPIO.LOW)
            GPIO.output([A, B, C], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==8:
            GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
        elif min1==9:
            GPIO.output(E, GPIO.LOW)
            GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
            GPIO.output(Clk3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk3, GPIO.LOW)
    #displays M2
    def disp_M2(min1):
        if min1==0:
            GPIO.output(G, GPIO.LOW)
            GPIO.output([A, B, C, D, E, F], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==1:
            GPIO.output([A, D, E, F, G], GPIO.LOW)
            GPIO.output([B, C], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==2:
            GPIO.output([C, F], GPIO.LOW)
            GPIO.output([A, B, G, E, D], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==3:
            GPIO.output([E, F], GPIO.LOW)
            GPIO.output([A, B, G, C, D], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==4:
            GPIO.output([A, D, E], GPIO.LOW)
            GPIO.output([F, G, B, C], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==5:
            GPIO.output([B, E], GPIO.LOW)
            GPIO.output([A, F, G, C, D], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==6:
            GPIO.output(B, GPIO.LOW)
            GPIO.output([A, F, G, C, D, E], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==7:
            GPIO.output([F,E, G, D], GPIO.LOW)
            GPIO.output([A, B, C], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==8:
            GPIO.output([A, F, G, B, C, D, E], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)
        elif min1==9:
            GPIO.output(E, GPIO.LOW)
            GPIO.output([A, F, G, B, C, D], GPIO.HIGH)
            GPIO.output(Clk4,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(Clk4, GPIO.LOW)

    #main loop
    while True:
        if readKeypad(6,['*',0,'#','D'])=='#':
            shadow_realm()

        #sets variable now to datetime data 
        now = datetime.now()
        
        #takes current hour and removes military time, stores it in variable hour_not_military
        hour_not_military = now.hour
        #if military is 13:00 -> 23:59
        if now.hour > 12:
            hour_not_military -= 12
            PM = True
        #elif military is 00:00 -> 00:59
        elif now.hour == 0:
            hour_not_military += 12
            PM = False
        #else (military is 1:00 to 12:59)
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


        if readKeypad(19,[4,5,6,'B'])=='B':
            B_Count += 1
            print(B_Count)
            time.sleep(0.3)

        if B_Count == 3:
            break


        disp_H1(H1)
        disp_H2(H2, PM)
        disp_M1(M1 )
        disp_M2(M2)
        

