number = input()
n1 = int(number[0])
n2 = int(number[1])
n3 = int(number[2])

maxNumber = max(n1, n2, n3)
minNumber = min(n1, n2, n3)
midleNumber = n1 + n2 + n3 - maxNumber - minNumber

maxAnswer = maxNumber * 10 + midleNumber
minAnswer = 0

if minNumber == 0:
    minAnswer = midleNumber * 10
else:
    minAnswer = minNumber * 10 + midleNumber

print(minAnswer, maxAnswer)
######
a = int(input())
b = a % 10
c = a // 100
d = a // 10 % 10
mx = max(b, c, d)
mn = min(b, c, d)
mid = (b + c + d) - mx - mn
if mn != 0:
    print(str(mn) + str(mid), str(mx) + str(mid))
else:
    print(str(mid) + str(mn), str(mx) + str(mid))
#####
number = input()
n1 = int(number[0])
n2 = int(number[1])
n3 = int(number[2])

maxNumber = max(n1, n2, n3)
minNumber = min(n1, n2, n3)
midleNumber = n1 + n2 + n3 - maxNumber - minNumber
if minNumber == 0:
    print(midleNumber * 10 + minNumber, maxNumber * 10 + midleNumber)
else:
    print(minNumber * 10 + midleNumber, maxNumber * 10 + midleNumber)

if minNumber == 0:
    print(str(midleNumber) + str(minNumber), str(maxNumber) + str(midleNumber))
else:
    print(str(minNumber) +  str(midleNumber), str(maxNumber) + str(midleNumber))