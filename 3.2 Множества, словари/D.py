a = int(input())
b = int(input())
m = []
o = []
for i in range(a):
    name = input()
    m.append(name)
for i in range(b):
    name = input()
    o.append(name)
m = set(m)
o = set(o)
M_O = m & o
if len(M_O) == 0:
    print("Таких нет")
else:
    print(len(M_O))
###
a = int(input())
b = int(input())
m = [input() for i in range(a)]
o = [input() for i in range(b)]
m = set(m)
o = set(o)
krygockec_elera = m & o
if len(krygockec_elera) == 0:
    print("Таких нет")
else:
    print(len(krygockec_elera))
###
a = int(input())
b = int(input())
listNames = [input() for i in range(a + b)]
newList = []
for i in listNames:
    if listNames.count(i) == 1:
        newList.append(i)
if len(newList) == 0:
    print("Таких нет")
else:
    print(len(newList))