count = int(input())
number = 0
summa = 0
for _ in range(count):
    number = int(input())
    while 0 < number:
        summa += number % 10
        number //= 10
print(summa)
###
count = int(input())
summa = 0
for _ in range(count):
    number = input()
    for i in range(len(number)):
        summa += int(number[i])
print(summa)
###
count = int(input())
number = 0
summa = 0
for _ in range(count):
    number = input()
    for i in number:
        summa += int(i)
print(summa)