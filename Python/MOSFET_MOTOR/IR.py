import RPi.GPIO as GPIO #RPI.GPIO
import time #Time 
import math #Math

on = 1

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

#PWM pin setup
GPIO.setup(18,GPIO.OUT)

#Define Clock, Data Transfer, and Switch GPIO pins
CLK = 17
DT = 27
SW = 22

#IR Pin
GPIO.setup(24,GPIO.IN)

#Setup GPIOs as inputs
GPIO.setup(CLK,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Initialize variabls for RPM and input control
timer = 0
bladenums = 0 #Num times the sensor sees the blade turn
freq = 500 #Frequeuncy value is set at 500
dc = 100 #Changing the duty cycle (dc) is how to adjust the RPM
pwm = GPIO.PWM(18,int(freq)) #Set the PWM of the motor to the duty cycle
pwm.start(int(dc))
inputSpeed = 0 #counter variable
prev = 1  #variable to keep track of if both CLK and DT were both previously 1
cntr = 0 #counter for prev variable (used in noMove)
pwm = "not pressed"   #variable to check for pwm presses
inputSpeeder = 0 #Debouncing counter
holder = "not moving"
rpm = 0

#set frequency to the motor
pwm = GPIO.PWM(18,int(freq))
       
#Written By Dawson
def noMove(prev):  # no move checks for how many times in a row prev has been 1. 
       global cntr # If it has been 1 for atleast 3 times in a row it will set direc to say the knob is not moving
       global direcs
       if prev:    #if prev is 1, increase the counter
                cntr += 1
       else:               #else set the counter to zero because the knob has started to move
              cntr = 0
       if cntr >= 3:       #if cntr is atleast 3, set direc to not moving
              direc = "not moving"

#Written by Dawson 
def PWM(): #identifies input signal
        global currentCLK; global currentDT; global prev; global inputSpeed; global CLK; global DT; global SW; global timer
        currentCLK = GPIO.input(CLK)
        currentDT = GPIO.input(DT)
        if currentCLK and currentDT:  #if CLK and DT are both 1, set prev to be 1 so that the program can tell the knob wasn't previously moving
                prev = 1
        elif not currentCLK and not currentDT: #if CLK and DT aren't both 1, then the knob is moving. However, if both are 0, then count shouldn't be changed because the                                # knob has just completed one cycle
                prev = 0
        elif not currentCLK and prev:   #given that the program passed the previous statements, if CLK is 0, the knob is moving ClockWise
                inputSpeed += 25
                prev = 0
        elif not currentDT and prev:   #Similarly, if the program passes the previous statements and DT is 0, the knob is moving Counter Clockwise
                inputSpeed -= 25
                prev = 0  
        if inputSpeed < 0: #only one direction, so dont allow input speed to go negative
                inputSpeed = 0
        if inputSpeed > 6000: #max input speed at 6000
               inputSpeed = 6000
        noMove(prev)   #Calling noMove to check for NON-movement
        #print("input speed is ", inputSpeed,",         and PWM status is ", pwm)   #prints out values 
        time.sleep(.05)
        timer += 1

#Written by Lucas, no longer used
def map_value(value, minIn, maxIn, minOut, maxOut):
        global dc
        dc = minOut + (maxOut - minOut) * ((value - minIn) / (maxIn - minIn)) #Maps inputs to outputs

#Written by Lucas, assisted with by Dawson
def calcRPM(): #interupt triggers this callback function
        global bladenums; global timer; global RPM; global inputSpeed
        rotations = bladenums / 3 #3 blades, so each rotation sees each blade once
        if timer == 20:
                if inputSpeed < 4450: #Set RPM for low RPM values based on roations
                        RPM = rotations*35 - inputSpeed/450
                else:
                      RPM = 4450+.0965*inputSpeed #correction factor for high RPM dips
                       
                if RPM < 0:
                       RPM = 0
                print("Output RPM: ", RPM) #Print RPM to terminal
                print("Input speed: ", inputSpeed) #Print input speed to terminal
                timer = 0 #Reset timer after calculation
                bladenums = 0 #Reset bladenums after calculation

#Written by Dawson. No longer used
def rpmCorr(sp):
        global inputSpeed
        
        if sp <= 3000:
          diff = -sp + (20.99*sp+4.7689)
          if diff > 0:
                  sp =   sp + abs(diff) 
          else:
                sp = sp + diff
        else:
          diff = sp - (89.9*sp-9020.6)
          if diff > 0:
                  sp =   sp - diff 
          else:
                sp = sp + abs(diff)

        return sp

#Written by Lucas and Nathan
inputSpeed = 0
def propellerSignal():
        global pwm; global dc; global inputSpeed; global freq
        #freq = input("Define a Frequency: ")
        #dc = input("Define a Duty Cycle: ")
        #map_value(inputSpeed, 0, 6000, 0, 100)
        if inputSpeed == 0: #0 input speed should set duty cycle to 0
               dc = 0
        else:
                 
                dc = math.exp((inputSpeed+3703.5)/1917.2) #maps the input Speed to the duty cycle non linearly
                if dc > 100:
                       dc = 100
        #defien appopriate Frequency
        #convert pwm inputSpeed to DutyCycle
        #print("DC: ", dc, "\n")
        #print("inputSpeed: ", inputSpeed, "\n")
        pwm.ChangeFrequency(int(freq))
        pwm.ChangeDutyCycle(int(dc))

#Written by Lucas
def oneup(num):
        global bladenums
        num = 1
        bladenums += 1 #Increase number of blades seen by IR sensor

        #convert pin signal into RPM

#Function for registering input button press. Written by Nathan
def Shadow_V2(): #button press enters callback function shadow realm from interrupt
        global SW; global inputSpeed; global RPM
        print("") #Pauses output RPM and input speed
        time.sleep(0.8)
        pwm.ChangeDutyCycle(0) #stop rotation by setting PWM to 0
        prev = RPM
        RPM = 0
        while True:
                print("Output RPM: ", RPM) #Print RPM to terminal
                print("Input speed: ", inputSpeed) #Print input speed to terminal
                if GPIO.input(SW) != 1: #ON button press, resume fan
                        time.sleep(0.8)
                        pwm.ChangeDutyCycle(int(dc)) #Set PWM back to the duty cycle value
                        RPM = prev
                        break          

#interrupts written by Dawson
#GPIO.add_event_detect(24,GPIO.RISING,callback=calcRPM,bouncetime=50)
GPIO.add_event_detect(24,GPIO.RISING,callback=oneup,bouncetime=1)

pwm.start(int(dc)) #initialize PWM to duty cycle value
inputSpeed = 0 #Start input speed at 0

# Main loop calling all of the functions. Written by Lucas and Nathan
while True:
        if GPIO.input(SW) != 1: #Upon button press, enter function to stop balde
                Shadow_V2()
        PWM()
        calcRPM()
        propellerSignal()

   