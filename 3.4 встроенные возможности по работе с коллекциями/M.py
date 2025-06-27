from itertools import permutations

number = int(input())
names = [input() for _ in range(number)]
names.sort()

for i in permutations(names, number):
    print(', '.join(i))