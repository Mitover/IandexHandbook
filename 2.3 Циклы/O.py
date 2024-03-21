# count = int(input())
# countHare = 0
# for i in range(count):
#     words = input()
#     if "зайка" in words:
#         countHare += 1
# print(countHare)
#------

count = int(input())
countHare = 0
i = 0
while i < count:
    words = input()
    if "зайка" in words:
        countHare += 1
    i += 1
print(countHare)
