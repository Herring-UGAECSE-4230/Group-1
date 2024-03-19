import RPi.GPIO as GPIO #import RPi
import time
import numpy as np
import simpleaudio as sa

frequency = 500 #generated tone frequency
fs = 44100 #sampling fruequency
seconds = 10 #duration tone will be played for
t=np.linspace(0,seconds,seconds * fs, False) #array for sine wave
note = np.sin(frequency*t*2*np.pi) # sine wave creation
audio = note*(2**15-1)/np.max(np.abs(note)) #ensure within output range
audio = audio.astype(np.int16) #audio to 16 bit format
playObj=sa.play_buffer(audio,1,2,fs) #starts audio playback
print("It has been 10 seconds")

dictionary = {
    'ATTENTION': '-.-.-', 'OVER': '-.-', 'OUT': '.-.-.',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def convert(text):
    morse_code = '' #reset morse code to empty
    for word in text.upper().split(): #uppercase for dictionary
        if word in dictionary: #check dictionary for each char
            morse_code += dictionary[word] + ' ' #add definition to morse code file and a space
        elif word == '\n': #new lines should add a new line
            morse_code += '\n'
        else:
            for char in word:
                if char in dictionary:
                    morse_code += dictionary[char] + ' '
                elif char == '\n': #new lines should add a new line
                    morse_code += '\n'
    return morse_code.strip() #return and remove whitespace

input_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/input.txt" #File input locations in the form of r\"FILE_LOCATION"
output_file = r"/home/nnlm/Documents/Group-1/Python/Morse Code/output.txt" #File output locations in the form of r\"FILE_LOCATION"

open(output_file, 'w').write(convert(open(input_file, 'r').read())) #File locations in the form of r\"FILE_LOCATION"