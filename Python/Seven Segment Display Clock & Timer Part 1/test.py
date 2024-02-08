import RPi.GPIO as GPIO
from time import sleep

#Disable warnings so they are not displayed repeatedly
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 1 -> 7SD 1 (E) -> GPIO 18
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 2 -> 7SD 2 (D) -> GPIO 23 
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 3 -> 7SD 4 (C) -> GPIO 25
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 4 -> 7SD 5 (DP) -> GPIO 12
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 5 -> 7SD 6 (B) -> GPIO 16
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 6 -> 7SD 7 (A) -> GPIO 20
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 7 -> 7SD 9 (F) -> GPIO 21
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # DFF Pin 8 -> 7SD 10 (G) -> GPIO 24
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # ENABLE -> GPIO 22
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH) # CLOCK -> GPIO 11 (SPICLOCK)
GPIO.output(20,GPIO.HIGH)
GPIO.output(16,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
GPIO.output(25,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)