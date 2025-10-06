import random
import os

print(os.getcwd())
a = open("D:/GitHub/IandexHandbook/2.4 Вложенные циклы/K.py", encoding="UTF-8")
list1 = a.read().split("###")
stringCodes = []
for i in list1:
    stringCodes.append(i.split("\n"))




for i in stringCodes:
    random.shuffle(i)
    print()
    print("###")
    for j in i:
        if j != "":
            print(j.strip())
    
   



