n = int(input())
v = "YES"
for i in range(n):
    q = input().lower()
    if not q[0] in "абв":
        v = "NO"
print(v)
###
#Вариант со списками
num = int(input())
all_good = True
words = []
for _ in range(num):
    words.append(input())
for word in words:
    if word[0] not in 'абв':
        all_good = False
if all_good:
    print('YES')
else:
    print('NO')