# words = input()
# if "зайка" in words:
#     print("YES")
# else:
#     print("NO")

# print("--------------")

isHave = False
words = input()
for i in range(len(words)):
    if words[i:i+5] == "зайка":
        isHave = True
if isHave:
    print("YES")
else:
    print("NO")

# words = "березка елочка зайка волк березка"
# for i in range(len(words)):
#     print(i, words[i], words[i:i+5])
