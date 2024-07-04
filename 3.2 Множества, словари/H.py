count = int(input())
dictNames = {}
for i in range(count):
    namePorridge = input().split()
    dictNames[namePorridge[0]] = namePorridge[1:]
dictNames = dict(sorted(dictNames.items()))
chooicePorridge = input()
listNames = []
for key in dictNames:
    if chooicePorridge in dictNames[key]:
        listNames.append(key)
if len(listNames) == 0:
    print("Таких нет")
else:
    for i in listNames:
        print(i)
###
a= [["березка", "елочка", "зайка", "волк", "березка"], 
["сосна", "зайка", "сосна", "елочка", "зайка", "медведь"],
["сосна", "сосна", "сосна", "белочка", "сосна", "белочка"]]