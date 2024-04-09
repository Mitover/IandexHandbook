number = int(input())

result = 0
power = 1

while number > 0:
    if number % 2 != 0:
        result += (number % 10) * power
        power *= 10
    number //= 10

print(result)

