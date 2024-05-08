a = int(input())
porridges = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
b = 0
while b < a:
    print(porridges[b % len(porridges)])
    b += 1