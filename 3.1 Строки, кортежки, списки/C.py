L = int(input())
n = int(input())
for i in range(n):
    words = input()
    if len(words) > L:
        words  = words[0:L - 3] + "..."
    print(words)

#------------
# length = int(input())
# count = int(input())

# for _ in range(count):
#     string = input()
#     if len(string) <= length:
#         print(string)
#     else:
#         print(f'{string[:length - 3]}...')