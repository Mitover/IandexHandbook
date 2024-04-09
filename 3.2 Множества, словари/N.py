# a = {"масло", "хлеб"}
# b = set(["хлеб", "масло"])
# print(a & b)
# print(a & b == {"масло", "хлеб"})

N = int(input())
productes = set()
vivod = []

for _ in range(N):
    product = input()
    productes.add(product)

M = int(input())
spisok_pridyctes = set()

for _ in range(M):
    dish = input()
    P = int(input())
    spisok_pridyctes = set()
    for _ in range(P):
        nado = input()
        spisok_pridyctes.add(nado)

    if productes & spisok_pridyctes == spisok_pridyctes:
        vivod.append(dish)

vivod.sort()
if len(vivod) == 0:
    print("Готовить нечего") 
else:
    for i in vivod:
        print(i)




N = int(input())
productes = set()
vivod = []
for _ in range(N):
    product = input()
    productes.add(product)
M = int(input())
spisok_pridyctes = set()
for _ in range(M):
    dish = input()
    P = int(input())
    spisok_pridyctes = set()
    for _ in range(P):
        nado = input()
        spisok_pridyctes.add(nado)
    if productes & spisok_pridyctes == spisok_pridyctes:
        vivod.append(dish)


if len(vivod) == 0:
    print("Готовить нечего") 
else:
    for i in vivod:
        print(i)