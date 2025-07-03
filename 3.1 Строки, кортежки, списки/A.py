n = int(input())
v = "YES"
for i in range(n):
    q = input().lower()
    if not q[0] in "абв":
        v = "NO"
print(v)
###
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
###
n = int(input())
c = 0
for i in range(n):
    q = input().lower()
    if q[0] in "абв":
        c += 1
if c > 0:
    print('YES')
else:
    print('NO')