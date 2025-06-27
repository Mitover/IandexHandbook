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
    
###
list1size = int(input())
list2size = int(input())
set1 = set()
set2 = set()
for i in range(list1size + list2size):
    eater = input()
    if eater not in set1:
        set1.add(eater)
    else:
        set2.add(eater)
set1_set2 = set1 ^ set2  
if len(set1_set2) != 0:
    print(len(set1_set2))
else:
    print('Таких нет')
###

list1size = int(input())
list2size = int(input())
porridge_eaters = {}
for _ in range(list1size + list2size):
    eater = input()
    porridge_eaters[eater] = porridge_eaters.get(eater, 0) + 1
one_porridge_lovers = []
for eater in porridge_eaters:
    if porridge_eaters[eater] == 1:
        one_porridge_lovers.append(eater)
if len(one_porridge_lovers) != 0:
    print(len(one_porridge_lovers))
else:
    print('Таких нет')