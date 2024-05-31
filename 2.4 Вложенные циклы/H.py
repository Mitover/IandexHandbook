kids = int(input())
total_name = ''
total_summa = 0
for game in range(kids):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if total_summa <= summa:
        total_summa = summa
        total_name = name
print(name)




kids = int(input())
total_name = ''
total_summa = 0
for game in range(kids):
    name = input()
    number = int(input())
    summa = 0
    for i in str(number):
        summa += int(i)
    if total_summa <= summa:
        total_summa = summa
        total_name = name
print(name)