N = int(input())
M = int(input())
lenght = len(str(N*M))
for i in range(1, N * M + 1):
    print(f"{i:>{lenght}}", end=" ")
    if i % M == 0:
        print()
#####
from itertools import product

x = int(input())
y = int(input())

ln = len(str(x * y))

for i, j in product(range(1, x + 1), range(1, y + 1)):
    print(f'{((i - 1) * y + j):>{ln}}', end=' ')
    if j == y:
        print()