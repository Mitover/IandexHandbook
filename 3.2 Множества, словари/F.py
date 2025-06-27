sizeList1 = int(input())
sizeList2 = int(input())
list1 = {input() for i in range(sizeList1)}
list2 = {input() for i in range(sizeList2)}
set1 = set(list1)
set2 = set(list2)

set3 = set1 ^ set2

if len(set3) != 0:
    for i in sorted(set3):
        print(i)
else:
    print("Таких нет")
###
sizeList1 = int(input())
sizeList2 = int(input())
set1 = set()
set2 = set()
for _ in range(sizeList1 + sizeList2):
    eater = input()
    if eater in set1:
        set2.add(eater)
    else:
        set1.add(eater)

set3 = set1 ^ set2
if len(set3) != 0:
    for i in sorted(set3):
        print(i)
else:
    print("Таких нет")