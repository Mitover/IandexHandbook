a = int(input())
for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(i * j, end=" ")
    print()
###
a = int(input())
i = 1
j = 1
while i <= a:
    j = 1
    while j <= a:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1