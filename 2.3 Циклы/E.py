a = float(input())
b = 0
while a != 0:
    if a >= 500:
        b += a * 0.9
    else:
        b += a
    a = float(input())    
print(b)