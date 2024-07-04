L = int(input())
n = int(input())
for i in range(n):
    words = input()
    if len(words) > L:
        words = words[:L - 3] + "..."
    print(words)
###
length = int(input())
count = int(input())
listWords = []
for _ in range(count):
    listWords.append(input())  
for word in listWords:
    if len(word) > length:
        print(word[:length - 3] + "...")
    else:
        print(word)