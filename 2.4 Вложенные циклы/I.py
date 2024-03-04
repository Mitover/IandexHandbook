# count_kids = int(input())
# total_number = ""
# max_number= 0
# for _ in range(count_kids):
#     number = input()
#     for i in range(len(number)):
#         if int(number[i]) > max_number:
#             max_number = int(number[i])
#     total_number += str(max_number)
#     max_number = 0
# print(total_number)

# count_kids = int(input())
# total_number = ""
# max_number= 0
# for _ in range(count_kids):
#     number = input()
#     for i in number:
#         if int(i) > max_number:
#             max_number = int(i)
#     total_number += str(max_number)
#     max_number = 0
# print(total_number)

# count_kids = int(input())
# total_number = ""
# max_number= 0
# for _ in range(count_kids):
#     number = int(input())
#     while number > 0:
#         if number % 10 > max_number:
#             max_number = number % 10
#         number //= 10
#     total_number += str(max_number)
#     max_number = 0
# print(total_number)

count_kids = int(input())
total_number = ""
max_number= 0
for _ in range(count_kids):
    number = input()
    for i in range(len(number)):
        max_number = max(max_number, int(number[i]))
    total_number += str(max_number)
    max_number = 0
print(total_number)