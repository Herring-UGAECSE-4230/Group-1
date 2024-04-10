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

def sound_of_silence():
    if GPIO.input(LED_PIN) == 0:
        global opentime
        print("the telegraph is not pressed\n")
        sa.stop_all()
        time.sleep(0.05)
        while True:
            opentime += 1
            time.sleep(.001)
            if GPIO.input(LED_PIN) == 1:
                break   

def telegraph_input():
    global keypresstime; global LED_PIN
    keypresstime = 0
    print("checking pin...\n")

    if GPIO.input(LED_PIN) == 1:
        sa.play_buffer(audio, 1, 2, fs)
        time.sleep(0.05)
        print("the telegraph is pressed!\n")
        while True:
            keypresstime += 1
            time.sleep(.001)
            if GPIO.input(LED_PIN) == 0:
                break
    sa.stop_all()
    print("keypresstime = " + str(keypresstime) + " counts.\n")

def give_me_attention():
    global keypresstime; global dash; global dot; global newLine_or_word; global delay; global threshold; global opentime
    print("Notice me!\n" + "Give me attention: ")
    attnls = [[0,0],[1,0],[2,0],[3,0],[4,0]]
    totalpresstime = 0
    for a in range(5):
        sound_of_silence()
        telegraph_input()
        attnls[a][1] = keypresstime
        totalpresstime += keypresstime
        print("You noticed me for " + str(keypresstime) + " cycles.")
    sa.stop_all()
    time.sleep(0.05)
    print("attnls:\n" + str(attnls[0][1]) + "\n" + str(attnls[1][1]) + "\n" + str(attnls[2][1]) + "\n" + str(attnls[3][1]) + "\n" + str(attnls[4][1]) + "\n")
    threshold = totalpresstime*2/11
    print("Threshold cycles = " + str(threshold) + "\n")

#repaste def convert & def convert_with_text
#repaste def convert_with_text
def silence_sorting():
    global opentime
    print("You have broken the silence. " + "Opentime is equal to: " + str(opentime))
    if opentime < (threshold*1.5):
        print("I'm listening for the same character. \n")
        #do nothing
    elif (threshold*1.5) <= opentime <= (threshold*3.5):
        print("I'm listening for a NEW letter. \n")
        #store the letter
    else:
        print("I'm listening for a NEW word. \n")
        #write the word to text file
    opentime = 0

def press_sorting():
    global keypresstime
    print("New input. " + "Keypresstime is equal to: " + str(opentime))
    if keypresstime < (threshold):
        print("That's a dot. \n")
        #store the dot
    else:
        print("That's a dash. \n")
        #store the dash
    keypresstime = 0


def mail_time():
    print("Incoming data...")
    silence_sorting()
    telegraph_input()
    press_sorting()

    time.sleep(0.1)


# this isn't working: GPIO.add_event_detected(LED_PIN, GPIO.RISING, callback=mail_time(), bouncetime=50) #interrupt for key presses

#uncomment ###
###input_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/input.txt" #File input locations in the form of r\"FILE_LOCATION"
###output_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/output.txt" #File output locations in the form of r\"FILE_LOCATION"

#speaker(convert(open(input_file, 'r').read()))

#print("done")

#open(output_file, 'w').write(convert(open(input_file, 'r').read())) 
#input_file.close()

#main program
print("You've entered the Morse Code Program.\n")
time.sleep(1)
give_me_attention()

print("What's on your mind?")
while True:
    if GPIO.input(LED_PIN) == 1:
        mail_time()
    opentime += 1
    time.sleep(.001)