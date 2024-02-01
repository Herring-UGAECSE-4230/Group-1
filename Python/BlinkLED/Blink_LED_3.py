import pigpio #method 3

#Before Runing, type in terminal: sudo pipiod
#Kill with sudo kill [Task Number]

#Selecting Pi with PigPio
pi=pigpio.pi()

#Frequency and duty cycle adjustent
pi.set_PWM_frequency(4,1)
pi.set_PWM_dutycycle(4,127.50)


#Infinite Loop
while True:
    pass
pi.set_PWM_dutycycle(4,0)