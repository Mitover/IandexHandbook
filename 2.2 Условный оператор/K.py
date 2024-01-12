number = input()
n1 = number[0]
n2 = number[1]
n3 = number[2]
sumNumbers = sum([int(n1), int(n2), int(n3)])
sumMaxMin = max(int(n1), int(n2), int(n3)) + min(int(n1), int(n2), int(n3)) 
if sumMaxMin == (sumNumbers - sumMaxMin) * 2:
    print("YES")
else:
    print("NO")
