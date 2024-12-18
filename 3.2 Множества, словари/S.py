toys = []
unique = []
for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', ')))
for i in sorted(toys):
    if toys.count(i) == 1:
        print(i)
###
toys = []
unique = {}

for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', ')))

for toy in sorted(toys):
    unique[toy] = unique.get(toy, 0) + 1

for toy in unique:
    if unique[toy] == 1:
        print(toy)
###
toys = []
unique = []

for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', ')))  

for i in range(len(toys)):
    toy = toys.pop(0)
    if toy not in toys:
        unique.append(toy)
    toys.append(toy)

print('\n'.join(sorted(unique)))