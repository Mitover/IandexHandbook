# text = input()
# while text != "":
#     if text[0] == '#':
#         continue
#     if '#' in text:
#         n = text.index('#')
#         new_text = text[:n]
#         print(new_text)
#     else:
#         print(text)
#     text = input()
# ###
# while text := input():
#     if text[0] == '#':
#         continue
#     if '#' in text:
#         n = text.index('#')
#         new_text = text[:n]
#         print(new_text)
#     else:
#         print(text)

textList = """# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы""".split("\n")

print(textList[1])
print(textList[1].startswith('#'))
# for text in textList:
#     if text[0] == '#':
#         continue
#     if '#' in text:
#         n = text.index('#')
#         new_text = text[:n]
#         print(new_text)
#     else:
#         print(text)

code = input()
while code != '':
    lines = code.split('\n')
    result = ''
    for line in lines:
        if '#' in line:
            n = line.index('#')
            new_text = line[:n]
            result += new_text+ '\n'
        else:
            result += line + '\n'
    code = input()
    print(result.strip())