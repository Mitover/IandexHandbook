deti = int(input())
total_name = ''
total_summa = 0
for game in range(deti):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if total_summa <= summa:
        total_summa = summa
        total_name = name
print(total_name)