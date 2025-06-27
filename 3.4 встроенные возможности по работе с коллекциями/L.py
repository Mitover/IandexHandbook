listItems = []
for _ in range(int(input())):
    listItems.extend(input().split(', '))
listItems = enumerate(sorted(listItems), 1)
print('\n'.join([f'{num}. {item}' for num, item in listItems]))
#####
listItems = []
for _ in range(int(input())):
    listItems += input().split(', ')
listItems = sorted(listItems)
for i in range(len(listItems)):
    print(i + 1, ". ", listItems[i], sep="")
#####
listItems = []
for _ in range(int(input())):
    listItems += input().split(', ')
listItems.sort()
for i in range(len(listItems)):
    print(i + 1, ". ", listItems[i], sep="")