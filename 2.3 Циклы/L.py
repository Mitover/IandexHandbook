a = input()
i = 0
maxNumber = 0
while i < len(a):
    if int(a[i]) > maxNumber:
        maxNumber = int(a[i])
    i += 1 
print(maxNumber)
