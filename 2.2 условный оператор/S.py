x = float(input())
y = float(input()) 

if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 0 <= y <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 0 <= y <= 5 and (5 * x - 3 * y) > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif (0.25 * x ** 2 + 0.5 * x - 9) <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')
