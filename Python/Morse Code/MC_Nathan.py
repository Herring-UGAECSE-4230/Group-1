import RPi.GPIO as GPIO #import RPi
import time
import numpy as np
import simpleaudio as sa

LED_PIN = 9
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.IN)

keypresstime = 0

dash = 1 #seconds for a dash
dot = .33 #seconds for a dot
newLine_or_word = 3.3 #seconds between new lines or words
delay = 0.3 #seconds for delay after each dot or dash
threshold = .66 #defines the boundary between dot and dash
opentime = 0 #time the key is not pressed

frequency = 500 #generated tone frequency
fs = 44100 #sampling fruequency
seconds = 10 #duration tone will be played for
t=np.linspace(0,seconds,seconds * fs, False) #array for sine wave
note = np.sin(frequency*t*2*np.pi) # sine wave creation
audio = note*(2**15-1)/np.max(np.abs(note)) #ensure within output range
audio = audio.astype(np.int16) #audio to 16 bit format


            

dictionary = {
    '-.-.-': 'ATTENTION', '-.-': 'OVER', '.-.-.': 'OUT',
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

def telegraph_input():
    global keypresstime; global LED_PIN
    keypresstime = 0
    print("checking pin...")
    
    while True:
        if GPIO.input(LED_PIN) == 0:
            print("the telegraph is not pressed")
            sa.stop_all()
            time.sleep(0.05)
            while True:
                if GPIO.input(LED_PIN) == 1:
                    break        
        if GPIO.input(LED_PIN) == 1:
            sa.play_buffer(audio, 1, 2, fs)
            time.sleep(0.05)
            print("the telegraph is pressed!")
            while True:
                keypresstime += 1
                if GPIO.input(LED_PIN) == 0:
                    break
        print("keypresstime = " + str(keypresstime) + " counts.")

#repaste def convert & def convert_with_text
#repaste def convert_with_text

#attention goes here




#GPIO.add_event_detected(LED_PIN, GPIO.RISING, callback=telegraph_input(), bouncetime=50) #interrupt for key presses

#uncomment ###
###input_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/input.txt" #File input locations in the form of r\"FILE_LOCATION"
###output_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/output.txt" #File output locations in the form of r\"FILE_LOCATION"

#speaker(convert(open(input_file, 'r').read()))

#print("done")

#open(output_file, 'w').write(convert(open(input_file, 'r').read())) 
#input_file.close()
telegraph_input()