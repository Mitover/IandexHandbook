number = int(input())
isTrue = True
for i in range(2, int(number **0.5) + 1):
    if number % i == 0:
        isTrue = False
        break
if isTrue and number != 1:
    print("YES")
else:
    print("NO")
###
number = int(input())
isTrue = True
i = 2
while i < int(number ** 0.5) + 1:
    if number % i == 0:
        isTrue = False
        break
    i += 1
if isTrue and number != 1:
    print("YES")
else:
    print("NO")


