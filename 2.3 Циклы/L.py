a = input()
i = 0
maxNumber = 0
while i < len(a):
    if int(a[i]) > maxNumber:
        maxNumber = int(a[i])
    i += 1 
print(maxNumber)
###
a = input()
b = 0
while a > 0:
    if a % 10 > b:
        b = a % 10
    a //= 10
print(b)
###
a = input()
b = 0
for i in a:
    if int(i) > b:
        b = int(i)
print(b)
###
a = input()
b = 0
for i in range(len(a)):
    if int(a[i]) > b:
        b = int(a[i])
print(b)
