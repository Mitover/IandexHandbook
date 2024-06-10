import random
a = open("D:/GitHub/PythonLearn/2.3 Циклы/E.py")
list1 = a.read().split("###")[0]
stringCodes = []
for i in list1.split("\n"):
    stringCodes.append(i.strip())

random.shuffle(stringCodes)
for i in stringCodes:
    if i!="":
        print(i)