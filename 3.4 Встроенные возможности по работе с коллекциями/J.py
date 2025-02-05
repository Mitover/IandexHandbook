from itertools import product

num = int(input())
nums = range(1, num - 1)
table = list(product(nums, repeat=3))

print('А Б В')
for i in range(len(table)):
    if sum(table[i]) == num:
        print(" ".join([str(j) for j in table[i]]))
#####
# from itertools import combinations
# count = int(input())
# nums = range(1, count)
# print("А Б В")
# for i, j in list(combinations(nums, 2)):
#     print(f"{i} {j - i} {count - j}")