number = input()
n1 = number[0]
n2 = number[1]
n3 = number[2]
sumNumbers = sum([int(n1), int(n2), int(n3)])
sumMaxMin = max(int(n1), int(n2), int(n3)) + min(int(n1), int(n2), int(n3)) 
if sumMaxMin == (sumNumbers - sumMaxMin) * 2:
    print("YES")
else:
    print("NO")


#-----------------------
num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10

middle = first + second + third - max(first, second, third) - min(first, second, third)

if max(first, second, third) + min(first, second, third) == middle * 2:
    print('YES')
else:
    print('NO')

#------------------------
# n = int(input())
# a = n % 10
# b = n // 10 % 10
# c = n // 100 % 10
# if a >= b and a >= c:
#     maxi = a
#     if b >= c:
#         mini = c
#         sred = b
#     else:
#         mini = b
#         sred = c
# elif b >= a and b >= c:
#     maxi = b
#     if a >= c:
#         mini = c
#         sred = a
#     else:
#         mini = a
#         sred = c
# else:
#     maxi = c
#     if b >= a:
#         mini = a
#         sred = b
#     else:
#         mini = b
#         sred = a
 
# if maxi + mini == (sred * 2):
#     print('YES')
# else:
#     print('NO')