# a = """Иванов Петров
# Иванов Сергеев
# Васильев Петров
# Сергеев Яковлев
# Петров Кириллов
# Петров Яковлев"""

# print(a.split("\n"))

# listFriend = a.split("\n")
# friends = {}

# for i in listFriend:
#     fr1, fr2 = i.split()
#     print(fr1, fr2)
#     friends[fr1] = friends.get(fr1, set()).add(fr2)
#     friends[fr2] = friends.get(fr2, set()).add(fr1)




# print(input().split())
# b = """Иванов Петров
# Иванов Сергеев
# Васильев Петров
# Сергеев Яковлев
# Петров Кириллов
# Петров Яковлев"""

# b = b.split("\n")

# abc = {}

# for a in b:
#     fr1, fr2 = a.split()
#     abc[fr1] = abc.get(fr1, set()) | set([fr2])
#     abc[fr2] = abc.get(fr2, set()) | set([fr1])
#     # a = input().split()

# abc_abc = {}

# for i in sorted(abc):
#     for ii in abc[i]:
#         abc_abc[i] = abc_abc.get(i, set()) | abc[ii] 

# for i in abc_abc:
#     abc_abc[i].discard(i)
#     abc_abc[i] -= abc[i]
#     abc_abc[i] = sorted(abc[i])
#     print(f'{i}: {", ".join(abc_abc[i])}')



# b = """Иванов Петров
# Иванов Сергеев
# Васильев Петров
# Сергеев Яковлев
# Петров Кириллов
# Петров Яковлев"""

a = input().split()

abc = {}

while a != []:
    fr1, fr2 = a[0], a[1]
    abc[fr1] = abc.get(fr1, set()) | set([fr2])
    abc[fr2] = abc.get(fr2, set()) | set([fr1])
    a = input().split()

abc_abc = {}

for i in sorted(abc):
    for ii in abc[i]:
        abc_abc[i] = abc_abc.get(i, set()) | abc[ii] 

for i in abc_abc:
    abc_abc[i].discard(i)
    abc_abc[i] -= abc[i]
    abc_abc[i] = sorted(abc[i])
    print(f'{i}: {", ".join(abc_abc[i])}')