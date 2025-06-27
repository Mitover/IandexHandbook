terrainList = []
count = int(input())
for i in range(count):
    a = input().split()
    terrainList.extend(a)
for i in set(terrainList):
    print(i)
    
###
N = int(input())
a = ""
for _ in range(N):
    s = input()
    a = a + " " + s
a = a.split()
a = set(a)
for i in a:
   print(i)