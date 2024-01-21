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