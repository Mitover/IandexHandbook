direc = input()
x = 0
y = 0
while direc != "СТОП":
    if direc == "ЮГ":
        y -= int(input())
    elif direc == "СЕВЕР":
        y += int(input())
    elif direc == "ЗАПАД":
        x -= int(input())
    elif direc == "ВОСТОК":
        x += int(input())
    direc = input()
print(y)
print(x)