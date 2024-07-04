stroka1 = set(input())
stroka2 = set(input())
for i in stroka1 & stroka2:
    print(i, end="")

stroka1 = set(input())
stroka2 = set(input())
print("".join(stroka1 & stroka2))
