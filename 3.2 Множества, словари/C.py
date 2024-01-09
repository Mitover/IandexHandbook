spisok = []
colMestnostei = int(input())
for i in range(colMestnostei):
    a = input().split()
    spisok.extend(a)

for i in set(spisok):
    print(i)