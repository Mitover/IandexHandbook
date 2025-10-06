row = int(input())
colum = int(input())
num = 1

width = len(str(row * colum))

for r in range(1, row + 1): 
    num = r
    for c in range(colum): 
        print(f'{num:>{width}}', end=' ')
        num += row
    print()