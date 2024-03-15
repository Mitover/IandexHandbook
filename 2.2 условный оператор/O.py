number = input()
number2 = input()

n1 = int(number[0])
n2 = int(number[1])
n3 = int(number2[0])
n4 = int(number2[1])

maxNumber = max(n1, n2, n3, n4)
minNumber = min(n1, n2, n3, n4)
midleNumber = ((n1 + n2 + n3 + n4) - maxNumber - minNumber) % 10

# print(str(maxNumber) + str(midleNumber) + str(minNumber))

#-------------
print(maxNumber * 100 + midleNumber * 10 + minNumber)