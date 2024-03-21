number = input()
number_reverse = number[::-1]
if number == number_reverse:
    print("YES")
else:
    print("NO")

#--------
num = int(input())

original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print('YES')
else:
    print('NO')