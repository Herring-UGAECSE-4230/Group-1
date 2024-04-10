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
    sa.play_buffer(audio, 1, 2, fs)
    time.sleep(0.05)
    global keypresstime
    keypresstime = 0
    while (GPIO.input(LED_PIN) == 1):
        keypresstime += 1
    sa.stop_all()
    time.sleep(0.05)

def convert(text):
    english = '' #reset morse code to empty
    letter = ''
    for char in text: #uppercase for dictionary
        while char != " " or char != "\n":
            letter += char
    english += dictionary[letter]
    if char == "/":
        engish += " "
    elif char == "\n":
        english += "\n"
def convert_with_text(text):
    morse_code = '' #reset morse code to empty
    word = '' #used to account for words attention, over, out
    temp = ''
    for char in text.upper(): #uppercase for dictionary
        if char == ' ' or char == '\n': #if at the end of a word
            if word in dictionary: #once a word has been added, check if its in the dictionary
                morse_code += dictionary[word] + " | " + word.lower()
            else:
                for f in word: #if the word isnt in the dictionary, add each char of the word
                    if f in dictionary:
                        morse_code += dictionary[f] + " "
                        temp += f
            if char == '\n': # if the char added is a new line, add a new line to morse_code
                if temp != '':
                    morse_code += " | " + temp.lower()
                    temp = ''
                morse_code += '\n'
            if char == ' ': # if the char added is a new line, add a new line to morse_code
                morse_code += '/'
            word = ''
        else: #occurs for words until a new line or space is reached
            word += char
    return morse_code.strip() #return and remove whitespace


def attention():
    global keypresstime; global dot; global dash; global newLine_or_word; global delay; global threshold
    attn_char = [[0,0],[1,0],[2,0],[3,0],[4,0]] #define data structure for attention input
    print("Please type '-.-.-' to calibrate:\n")
    for char in attn_char:
        telegraph_input() #runs telegraph_input subroutine
        attn_char[char[1]] = keypresstime #stores press times for the telegraph key into list of lists
    dot = (attn_char[1[1]] + attn_char[3[1]]) / 2 #calculates the length of a dot
    threshold = dot * 2 #calculates the boundary length
    print("Dot time: ")
    print(dot)
    #add file creation and write attention to it




#GPIO.add_event_detected(LED_PIN, GPIO.RISING, callback=telegraph_input(), bouncetime=50) #interrupt for key presses

input_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/input.txt" #File input locations in the form of r\"FILE_LOCATION"
output_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/output.txt" #File output locations in the form of r\"FILE_LOCATION"

#speaker(convert(open(input_file, 'r').read()))

#print("done")

open(output_file, 'w').write(convert(open(input_file, 'r').read())) 
input_file.close()
attention()