number = int(input())
print(str(number % 1000 // 100) + str(number // 1000) + str(number % 10) + str(number // 10 % 10))