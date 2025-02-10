from itertools import product

num = int(input())
nums = range(1, num - 1)
table = list(product(nums, repeat=3))

print('А Б В')
for i in range(len(table)):
    if sum(table[i]) == num:
        print(" ".join([str(j) for j in table[i]]))
#####
from itertools import combinations
count = int(input())
nums = range(1, count)
print("А Б В")
for i, j in list(combinations(nums, 2)):
    print(f"{i} {j - i} {count - j}")
#####
from itertools import product
N = int(input())
print("А Б В")
values = list(product(range(1, N + 1), repeat=3))
for i in values:
    if i[0] + i[1] + i[2] == N:
        print(f'{i[0]} {i[1]} {i[2]}')