s = input()
count = 1
char = s[0]

for i in range(1, len(s)):
    if char == s[i]:
        count += 1
    else:
        print(char, count)
        char = s[i]
        count = 1
print(char, count)        