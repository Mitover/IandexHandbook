a = input().split()
c = set()
while a != []:
    for i in range(len(a)):
        if a[i] == "зайка":
            if i > 0 and i < len(a) - 1:
                c.add(a[i - 1])
                c.add(a[i + 1])
            elif i == 0:
                c.add(a[i + 1])
            else:
                c.add(a[i - 1])
    a = input().split()
    
for i in c:
    print(i)