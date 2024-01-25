import pigpio

pi=pigpio.pi()
pi.set_PWM_frequency(4,12)
pi.set_PWM_dutycycle(4,150)

while True:
    pass

pi.set_PWM_dutycycle(4,0)