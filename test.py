import random
a = open("D:/GitHub/PythonLearn/2.4 Вложенные циклы/C.py", encoding="UTF-8")
list1 = a.read().split("###")[0]
stringCodes = []
for i in list1.split("\n"):
    stringCodes.append(i.strip())

random.shuffle(stringCodes)
for i in stringCodes:
    if i!="":
        print(i)


range(5)