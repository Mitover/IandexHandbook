a = int(input())
if a < 3:
    print(a)
delitel = 2
while a > 1:
    if a % delitel == 0:
        print(delitel, end="")
        if a != delitel:
            print(' *', end=' ')
        a //= delitel
        delitel = 1
    delitel += 1