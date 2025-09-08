n = int(input())
listWords = [input() for i in range(n)]
w = input().lower()
for i in listWords:
    if w in i.lower():
        print(i)
###
n = int(input())
listWords = []
for i in range(n):
    listWords.append(input())
w = input().lower()
for i in listWords:
    if w in i.lower():
        print(i)
###
n = int(input())
listWords = ""
for i in range(n):
    listWords += input() + "|"
listWords = listWords.split("|")
w = input().lower()
for i in listWords:
    if w in i.lower():
        print(i)