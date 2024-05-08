word = input().lower().replace(" ", "")
if word == word[::-1]:
    print("YES")
else:
    print("NO")