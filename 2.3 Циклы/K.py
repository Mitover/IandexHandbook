a = input()
b = 0
for i in range(len(a)):
    b += int(a[i])
print(b)
###
a = input()
b = 0
for symbol in a:
    b += int(symbol)
print(b)
###
a = int(input())
b = 0
while a > 0:
    b += a % 10
    a //= 10
print(b)