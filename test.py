import random
a = open("C:/Work/IandexHandbook/3.1 Строки, кортежки, списки/F.py", encoding="UTF-8")
list1 = a.read().split("###")[1]
stringCodes = []
for i in list1.split("\n"):
    stringCodes.append(i.strip())

random.shuffle(stringCodes)
for i in stringCodes:
    if i!="":
        print(i)


