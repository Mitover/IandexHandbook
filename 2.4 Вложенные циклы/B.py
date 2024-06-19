a = int(input()) + 1
for i in range(1, a):
    for j in range(1, a):
        print(f'{j} * {i} = {j * i}')
###
a = int(input()) + 1
for i in range(1, a):
    for j in range(1, a):
        print(j, "*", i, "=", j * i)
###
a = int(input())
for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(i * j, end=" ")
    print()