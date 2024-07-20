a = int(input())
for _ in range(a):
    b = input()
    isFind = False
    for j in range(len(b) - 1):
        if b[j + 1] == "а" and b[j] == "з":
            isFind = True
            break
    if isFind:
        print(j + 1)
    else:
        print("Заек нет =(")
###
count = int(input())
bunnies = 0
for _ in range(count):
    position = input().find('зайка') + 1
    if position:
        print(position)
    else:
        print("Заек нет =(")
###
count = int(input())
bunnies = 0
for _ in range(count):
    string = input()
    if 'зайка' in string:
        print(string.index('зайка') + 1)
    else:
        print("Заек нет =(")
###
a = int(input())
for _ in range(a):
    b = input()
    for j in range(len(b) - 1):
        if b[j + 1] == "а" and b[j] == "з":
            print(j + 1)
            break
    else:
        print("Заек нет =(")