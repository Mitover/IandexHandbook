from itertools import product
number = int(input())
values = list(product(range(1, number + 1), repeat=2))
print(values)
for i in range(len(values)):
    if i % number == number - 1:
        print(values[i][0] * values[i][1])
    else:
        print(values[i][0] * values[i][1], end=" ")
#####
from itertools import product, islice
size = int(input())
nums = range(1, size + 1)
table = [x * y for x, y in product(nums, repeat=2)]

for row in range(size):
    print(*islice(table, row * size, (row + 1) * size))