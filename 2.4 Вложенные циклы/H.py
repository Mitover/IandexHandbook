cids = int(input())
name = ''
total_summa = 0
for game in range(cids):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if total_summa <= summa:
        total_summa = summa
        name = name
print(name)




cids = int(input())
name = ''
total_summa = 0
for game in range(cids):
    name = input()
    number = int(input())
    summa = 0
    for i in str(number):
        summa += int(i)
    if total_summa <= summa:
        total_summa = summa
        name = name
print(name)