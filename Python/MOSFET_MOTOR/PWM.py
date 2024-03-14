import RPi.GPIO as GPIO
import time

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)

#Reading GPIO from the GPIO number, not pin placement
GPIO.setmode(GPIO.BCM)

#Define Clock, Data Transfer, and Switch GPIO pins
CLK = 17
DT = 27
SW = 22

#Setup GPIOs as inputs
GPIO.setup(CLK,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW,GPIO.IN,pull_up_down=GPIO.PUD_UP)



count = 0 #counter variable

prev = 1  #variable to keep track of if both CLK and DT were both previously 1
direc = "___"  #variable to current display direction
cntr = 0 #counter for prev variable (used in noMove)
pwm = "not pressed"   #variable to check for pwm presses
counter = 0 #Debouncing counter
holder = "not moving"

def debounce(direc):
        global counter 
        global holder

        if direc == "CCW" or direc == "CW": 
                if holder == "not moving":
                        counter = 1
                elif holder == direc:
                        counter += 1
                holder = direc
                if counter < 3:
                        direc = "not moving"
        elif direc == "not moving":
                counter = 0
                holder = "not moving"
       

def noMove(prev):  # no move checks for how many times in a row prev has been 1. 
                   # If it has been 1 for atleast 3 times in a row it will set direc to say the knob is not moving
       global cntr
       global direc

       if prev:    #if prev is 1, increase the counter
                cntr += 1
       else:               #else set the counter to zero because the knob has started to move
              cntr = 0
       if cntr >= 3:       #if cntr is atleast 3, set direc to not moving
              direc = "not moving"


def pwmpress(input): #pwmpress checks for PWM presses. SW is automatically set to 1, so pressing the knob will set it to 0. 
                     # it doesn't currently toggle on and off (you have to hold the knob down) but this can be implemented if need be
       global pwm

       if input:
                pwm = "not pressed"
       else:
                pwm = "pressed" 


while True:
    currentCLK = GPIO.input(CLK)
    currentDT = GPIO.input(DT)

    if currentCLK and currentDT:  #if CLK and DT are both 1, set prev to be 1 so that the program can tell the knob wasn't previously moving
            prev = 1
            
    elif not currentCLK and not currentDT: #if CLK and DT aren't both 1, then the knob is moving. However, if both are 0, then count shouldn't be changed because the                                # knob has just completed one cycle
            prev = 0
            
    elif not currentCLK and prev:   #given that the program passed the previous statements, if CLK is 0, the knob is moving ClockWise
            direc = "CW"
            
            count += 1
            prev = 0
            
    elif not currentDT and prev:   #Similarly, if the program passes the previous statements and DT is 0, the knob is moving Counter Clockwise
            direc = "CCW"
            
            count -= 1
            prev = 0
            
    noMove(prev)   #Calling noMove to check for NON-movement
    debounce(direc)
    pwmpress(GPIO.input(SW)) #Calling pwmpress to check for PWM press
    
    print("count is ", count,",        direction is ", direc, ",        and PWM status is ", pwm)   #prints out values 
    time.sleep(.05)

    


