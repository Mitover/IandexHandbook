a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("Петя")
elif b > a and b > c:
    print("Вася")
else:
    print("Толя")

###

v = int(input())
p = int(input())
t = int(input())
if p > v:
    if p > t:
        print("Петя")
    else:
        print("Толя")
elif v > p :
    if v > t:
        print("Вася")
    else:
        print("Толя")
else:
    print("Толя")