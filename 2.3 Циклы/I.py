a = 1
i = 1
b = int(input())
while i <= b:
    a *= i
    i += 1
print(a)
#----------------

n = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
print(f)