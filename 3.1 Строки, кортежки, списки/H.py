count = int(input())
for i in range(count):
    b = input()
    isFind = False
    for j in range(len(b)):
        if b[j + 1] == "а" and b[j] == "з":
            isFind = True
            break
    if isFind:
        print(j + 1)
    else:
        print("Заяк нет")


#------------

count = int(input())

for _ in range(count):
    string = input()
    if 'зайка' in string:
        print(string.index('зайка') + 1)
    else:
        print("Заек нет =(")