import wiringpi #metthod 2

#Integrate GPIO pins to WiringPi
wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(4) #use gpio 4
wiringpi.softToneWrite(4,12) #setting frequency to gpio 4

#Infinite Loop
while True:
    pass
wiringpi.softToneWrite(4,0)