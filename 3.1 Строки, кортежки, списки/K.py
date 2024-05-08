n = int(input())
listWords = [input() for i in range(n)]
w = input().lower()
for i in listWords:
    if w in i.lower():
        print(i)