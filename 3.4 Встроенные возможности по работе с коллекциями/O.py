from itertools import permutations

number = int(input())
names = []
for _ in range(number):
    names += input().split(", ")
names.sort()

for i in permutations(names, 3):
    print(' '.join(i))