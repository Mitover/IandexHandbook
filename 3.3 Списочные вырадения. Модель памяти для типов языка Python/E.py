result = set()
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if (int(num ** 0.5)) ** 2 == num:
        result.add(num)

print({num for num in numbers if int(num ** (0.5)) ** 2 == num})