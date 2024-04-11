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
