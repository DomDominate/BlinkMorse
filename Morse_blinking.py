from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import collections
import time
from tkinter.scrolledtext import ScrolledText
RPi.GPIO.setmode(RPi.GPIO.BCM)

TIME = 0.3
DOT_DURATION = TIME
DASH_DURATION = 3 * TIME
SYMBOL_PAUSE = TIME
LETTER_PAUSE = 3 * TIME
WORD_PAUSE = 7 * TIME

MORSE_ENCODING = collections.OrderedDict([
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
    (' ', ' '),
    (',', '--..--'),
    ('.', '.-.-.-'),
    ('?', '..--..'),
    (';', '-.-.-.'),
    (':', '---...'),
    ("'", '.----.'),
    ('-', '-....-'),
    ('/', '-..-.'),
    ('(', '-.--.-'),
    (')', '-.--.-'),
    ('_', '..--.-')
])

led = LED(14)

def splitText(message):
    sep = ' '
    return list(map(list,message.split(sep)))

def convert(symbol):
    if symbol in MORSE_ENCODING:
        return MORSE_ENCODING[symbol]
    else:
        return -1
    
def blinkDot():
    led.on()
    time.sleep(DOT_DURATION)
    led.off()

def blinkDash():
    led.on()
    time.sleep(DASH_DURATION)
    led.off()

def blink():
    message = input.get('1.0', END)
    
    elements = splitText(message.strip())
    
    for element in elements:
        print(element)
        for character in element:
            print(f'{character}: ', end='')
            encoded = convert(character.strip().upper())
            if encoded == -1:
                print("invalid input")
                continue
            print(encoded)
            for symbol in encoded:
                print(symbol)
                if symbol == '.':
                    print('dot')
                    blinkDot()
                else:
                    print('dash')
                    blinkDash()
                time.sleep(SYMBOL_PAUSE)
            time.sleep(LETTER_PAUSE)
        time.sleep(WORD_PAUSE)
        
    

box = Tk()
box.title("Blinking morse code")
box.geometry("600x400")
Font = tkinter.font.Font(family = "Helvetica", size = 10)

input = Text(box, width = 80, height = 20, font = Font)
input.pack(pady=20)

button_frame = Frame(box)
button_frame.pack()

blink_button = Button(button_frame, text = "Blink morse code", command = blink)
blink_button.grid(row=0, column=0)



