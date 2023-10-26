from playsound import playsound
import time
text = input("Enter the text you would like to convert into Morse Code: ")

morse_code_text = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

clean_text = text.replace(" ", "")
print("Listen and/or read your morse code below:")

for character in clean_text:
    for symbol in morse_code_text[character.upper()]:
        print(symbol, end="")
        if symbol == ".":
            playsound("morse_code_dit_sound.mp3")
        else:
            playsound("morse_code_dah_sound.mp3")
    time.sleep(0.4)








