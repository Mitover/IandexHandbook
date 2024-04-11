first = str(input())
second = str(input())
third = str(input())
if (first < second) and (first < third):
    print(first)
elif (second < first) and (second < third):
    print(second)
else:
    print(third)