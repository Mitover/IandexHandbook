dict = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'}
#####

text = input().upper()
for index in range(len(text)): 
    if text[index] != ' ':
        print(dict[text[index]], end=" ")
    else:
        print()

#####
text = input().upper()
for char in text: 
    if char != ' ':
        print(dict[char], end = " ")
    else:
        print()

#####
text = input().upper()
for char in text:
    if char != ' ':
        print(dict.get(char, "\n"), end=" ")

#####
for i in text:
    if i == " ":
        print()
        continue
    i = dict[i.upper()]
    print(i, end=" ")
