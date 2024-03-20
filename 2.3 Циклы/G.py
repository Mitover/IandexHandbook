a = int(input())
b = int(input())
n = max(a, b)
while (n % min(a, b) != 0):
    n += max(a, b)
print(n)
     