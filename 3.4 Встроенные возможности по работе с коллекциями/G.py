from itertools import combinations
a = int(input())
s = []
for _ in range(a):
    s.append(input())
values = list(combinations(s, 2))
for i in values:
    print(f'{i[0]} - {i[1]}')
#####
from itertools import combinations
names = [input() for _ in range(int(input()))]
print('\n'.join([f'{name1} - {name2}' for name1, name2 in list(combinations(names, 2))]))  