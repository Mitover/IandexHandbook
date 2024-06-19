i = 0
word = input()
n = int(input())
while i < n:
    print(word)
    i += 1
###
word = input()
n = int(input())
for i in range(n):
    print(word)
###
word = input()
n = int(input())
words = (word + "\n") * n
print(words)