Transliterate_Dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}
text, result = "", ""
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for string in file_in:
        text += string
for char in text:
    char_copy = char.upper()
    if char_copy in Transliterate_Dict:
        if char.isupper():
            char = Transliterate_Dict[char_copy].capitalize()
        else:
            char = Transliterate_Dict[char_copy].lower()
    result += char
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(result, file=file_out)