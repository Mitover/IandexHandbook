N = int(input())
b = input()
for i in range(N - 1):
    a = input()
    if a < b:
        b = a
print(b)