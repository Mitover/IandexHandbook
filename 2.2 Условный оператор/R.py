a = float(input())
b = float(input())
c = float(input())

maxC = max(a, b, c) ** 2 
other =  a ** 2 + b ** 2 + c ** 2 - maxC

if maxC > other:
    print("велика")
elif maxC < other:
    print("крайне мала")
else:
    print("100%")



a = int(input())
b = int(input())
c = int(input()) 
if a + b > c or a + c > b or c + b > a:
    if a >= b and a >= c:
        if a ** 2 == b ** 2 + c ** 2:
            print('100%')
        elif a ** 2 > b ** 2 + c ** 2:
            print('велика') 
        else:
            print('крайне мала') 
    if b > a and b >= c:
        if b ** 2 == a ** 2 + c ** 2:
            print('100%') 
        elif b ** 2 > a ** 2 + c ** 2:
            print('велика') 
        else:
            print('крайне мала') 
    if c > a and c > b:
        if c ** 2 == a ** 2 + b ** 2:
            print('100%') 
        elif c ** 2 > a ** 2 + b ** 2:
            print('велика')
        else:
            print('крайне мала')