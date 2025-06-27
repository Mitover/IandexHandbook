from itertools import cycle, islice
porridges = [input() for _ in range(int(input()))]
days = int(input())
for i in islice(cycle(porridges), days):
    print(i)
#####
from itertools import cycle, islice
porridges = [input() for _ in range(int(input()))]
days = int(input())
print('\n'.join(islice(cycle(porridges), days)))
#####
from itertools import cycle
porridges = []
for _ in range(int(input())):
    porridges.append(input())
max_len = int(input())
count = 0
for i in cycle(porridges):
    if count < max_len:
        print(i)
        count += 1
    else:
        break