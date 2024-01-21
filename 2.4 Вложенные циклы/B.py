#I
a = int(input()) + 1
for i in range(1, a):
    for j in range(1, a):
        print(f'{j}*{i}={j * i}')


#II
a = int(input()) + 1
for i in range(1, a):
    for j in range(1, a):
        print(j, "*", i, "=", j * i)