cousins = dict()
for _ in range(int(input())):
    name = input()
    cousins[name] = cousins.get(name, 0) + 1
cousins = dict(sorted(cousins.items()))
isNamesakesHave = False
for name in cousins:
    if cousins[name] > 1:
        print(name, '-', cousins[name])
        isNamesakesHave = True
if not isNamesakesHave:
    print('Однофамильцев нет')
###
