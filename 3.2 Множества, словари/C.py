terrainList = []
count = int(input())
for i in range(count):
    a = input().split()
    terrainList.extend(a)
for i in set(terrainList):
    print(i)