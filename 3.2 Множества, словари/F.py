sizeList1 = int(input())
sizeList2 = int(input())
# list1 = {input() for i in range(sizeList1)}
# list2 = {input() for i in range(sizeList2)}
# set1 = set(list1)
# set2 = set(list2)

# set3 = set1 ^ set2

# if len(set3) != 0:
#     for i in sorted(set3):
#         print(i)
# else:
#     print("Таких нет")

set1 = set()
set2 = set()
for i in range(sizeList1):
    set1.add(input())
    
for i in range(sizeList2):
    set2.add(input())

set3 = set1 ^ set2
if len(set3) != 0:
    for i in sorted(set3):
        print(i)
else:
    print("Таких нет")