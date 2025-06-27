number = int(input())
print(str(number % 1000 // 100) + str(number // 1000) + str(number % 10) + str(number // 10 % 10))
###
number = input()
print(number[1] + number[0] + number[3] + number[2])
###
number = 1234
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 10
n4 = number % 100 // 10
print(n1 * 1000 + n2 * 100 + n3 * 10 + n4)