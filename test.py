import random
import os

print(os.getcwd())
a = open(os.getcwd() +"/3.1 Строки, кортежки, списки/J.py", encoding="UTF-8")
list1 = a.read().split("###")[0]
stringCodes = []
for i in list1.split("\n"):
    stringCodes.append(i.strip())

random.shuffle(stringCodes)
for i in stringCodes:
    if i!="":
        print(i)


