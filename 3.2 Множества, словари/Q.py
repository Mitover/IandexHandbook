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




# # print(input().split())
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

# a = input().split()

# abc = {}

# while a != []:
#     fr1, fr2 = a[0], a[1]
#     abc[fr1] = abc.get(fr1, set()) | set([fr2])
#     abc[fr2] = abc.get(fr2, set()) | set([fr1])
#     a = input().split()

# abc_abc = {}

# for i in sorted(abc):
#     for ii in abc[i]:
#         abc_abc[i] = abc_abc.get(i, set()) | abc[ii] 

# for i in abc_abc:
#     abc_abc[i].discard(i)
#     abc_abc[i] -= abc[i]
#     abc_abc[i] = sorted(abc[i])
#     print(f'{i}: {", ".join(abc_abc[i])}')

# names = input()
# listFriend = []
# while names != "":
#     listFriend.append(names)
#     names = input()



# listFriend = """Николай Фёдор
# Николай Женя
# Фёдор Женя
# Фёдор Илья
# Илья Фёдор"""

# listFriend = listFriend.split("\n")

# for i in listFriend:
#     fr1, fr2 = i.split()
#     if fr1 in friends:
#         friends[fr1].add(fr2)
#     else:
#         friends[fr1] = set()
#         friends[fr1].add(fr2)
      
#     if fr2 in friends:
#         friends[fr2].add(fr1)
#     else:
#         friends[fr2] = set()
#         friends[fr2].add(fr1)
        
# friends = dict(sorted(friends.items()))
# print(friends)

# friends2 = {name: set() for name in friends}

# for nameKey in friends:
#     for friend in friends[nameKey]:
#         for fr in friends:
#             if friend in friends[fr]  and fr != nameKey:
#                 friends2[nameKey].add(fr)

# for key in friends2:
#     friends2[key] = sorted(friends2[key])
#     print(key, ": ", ", ".join(friends2[key]), sep="")

# """Женя: Илья
# Илья: Женя, Николай
# Николай: Илья
# Фёдор: """


# friends = {}  # словарь прямых друзей

# while pair := input():
#     friend1, friend2 = pair.split()
#     friends[friend1] = friends.get(friend1, set()) | set([friend2])
#     friends[friend2] = friends.get(friend2, set()) | set([friend1])

# friends_of_friends = {}  # словарь друзей друзей

# for name in sorted(friends):
#     for person in friends[name]:
#         friends_of_friends[name] = friends_of_friends.get(
#             name, set()) | friends[person]

# for name in friends_of_friends:
#     friends_of_friends[name].discard(name)  # удаляем самого себя
#     friends_of_friends[name] -= friends[name]  # удаляем прямых друзей

#     friends_of_friends[name] = sorted(friends_of_friends[name])

#     print(f'{name}: {", ".join(friends_of_friends[name])}')


listFriend = """Николай Женя
Фёдор Женя
Фёдор Илья
Илья Фёдор"""

listFriend = listFriend.split("\n")
friends = {}

for i in listFriend:
    friend1, friend2 = i.split()
    print(friends.get(friend1, set()) | set([friend2]))
    friends[friend1] = friends.get(friend1, set()) | set([friend2])
    friends[friend2] = friends.get(friend2, set()) | set([friend1])
print(friends)
friends_of_friends = {}  # словарь друзей друзей

for name in sorted(friends):
    for person in friends[name]:
        friends_of_friends[name] = friends_of_friends.get(
            name, set()) | friends[person]

for name in friends_of_friends:
    friends_of_friends[name].discard(name)  # удаляем самого себя
    friends_of_friends[name] -= friends[name]  # удаляем прямых друзей

    friends_of_friends[name] = sorted(friends_of_friends[name])

    print(f'{name}: {", ".join(friends_of_friends[name])}')