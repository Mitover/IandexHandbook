a = int(input())
b = int(input())
c = int(input())

if (a < b + c) and (b < a + c) and (c < a + b):
    print("YES")
else:
    print("NO")

a = int(input())
b = int(input())
c = int(input())

if a // 10 == b // 10 == c // 10:
    print(a // 10)
elif a % 10 == b % 10 == c % 10:
    print(a % 10)