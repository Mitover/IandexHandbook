from sys import stdin
suma = 0
for line in stdin.readlines():
    for item in line.split():
        suma += int(item)
print(suma)
###
suma = 0
for i in stdin.read().split():
    suma += int(i)
print(suma)
###
summa = sum([int(num) for num in stdin.read().split()])
print(summa)