# a = int(input())
# row = 1
# collumn = 1
# for i in range(1, a + 1):
#     print(i, end=" ")
#     if row == collumn:
#         row += 1
#         collumn = 1
#         print()
#     else:
#         collumn += 1

#
number = int(input())

count = 1
num = 1

while num <= number:
    for i in range(count):
        if num > number:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1