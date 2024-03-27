a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("1. Петя")
    if b > c:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася") 
elif b > a and b > c:
    print("1. Вася")
    if a > c:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
elif c > a and c > b:
    print("1. Толя")
    if a > b:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")

#-----------------
pety = int(input()) 
vasy = int(input()) 
toly = int(input()) 
if pety > vasy and pety > toly: 
    print("1. Петя") 
    if vasy > toly: 
        print("2. Вася\n3. Толя") 
    else: 
        print("2. Толя\n3. Вася") 
elif vasy > pety and vasy > toly: 
    print("1. Вася") 
    if pety > toly: 
        print("2. Петя\n3. Толя") 
    else: 
        print("2. Толя\n3. Петя") 
else: 
    print("1. Толя") 
    if vasy > pety: 
        print("2. Вася\n3. Петя") 
    else: 
        print("2. Петя\n3. Вася")