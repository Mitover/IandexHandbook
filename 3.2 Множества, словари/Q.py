a = """Иванов Петров
Иванов Сергеев
Васильев Петров
Сергеев Яковлев
Петров Кириллов
Петров Яковлев"""

print(a.split("\n"))

listFriend = a.split("\n")

for i in listFriend:
    fr1, fr2 = i.split()
    print(fr1, fr2)