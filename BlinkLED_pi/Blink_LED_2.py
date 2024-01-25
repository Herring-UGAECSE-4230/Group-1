import wiringpi

wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(4)
wiringpi.softToneWrite(4,12)

while True:

wiringpi.softToneWrite(4,0)