number = int(input())
result = 0
power = 1

while number > 0:
    if number % 2 != 0:
        result += (number % 10) * power
        power *= 10
    number //= 10

print(result)

#######
number = input()
result = ""

for i in range(len(number)):
    if int(number[i]) % 2 != 0:
        result += number[i] 

print(result)


########
number = input()
result = ""

for i in number:
    if int(i) % 2 != 0:
        result += i 

print(result)
