row = int(input())
colum = int(input())
num = 1

max_number = row * colum
width = 0
while max_number: 
    width += 1 
    max_number //= 10 

for r in range(row):
    for c in range(colum):
        print(f'{num:>{width}}', end=' ')
        num += 1
    print()
###
row = int(input())
colum = int(input())
num = 1

width = len(str(row * colum))
for r in range(row):
    for c in range(colum):
        print(f'{num:>{width}}', end=' ')
        num += 1
    print()
