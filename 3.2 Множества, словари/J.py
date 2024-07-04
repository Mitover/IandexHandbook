Transliterate_Dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}
text = input()
textnew = ""
for i in range(len(text)):
    if text[i].isupper():
        textnew += Transliterate_Dict[text[i]]
    elif not text[i].isalpha():
        textnew += text[i]
    else:
        textnew += Transliterate_Dict[text[i].upper()].lower()
print(textnew)

#--------------------

result = ''

for char in input():
    char_copy = char.upper()
    if char_copy in Transliterate_Dict:
        if char.isupper():
            char = Transliterate_Dict[char_copy].capitalize()
        else:
            char = Transliterate_Dict[char_copy].lower()
    result += char

print(result)