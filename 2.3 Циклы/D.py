a = int(input())
b = int(input())
if b > a:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
###
a = int(input())
b = int(input())
if b > a:
    while a <= b:
        print(a, end=" ")
        a += 1
else:
    while a >= b:
        print(a, end=" ")
        a -= 1

