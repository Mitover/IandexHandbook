result = {}
numbers = {1, 2, 3, 4, 5, 10, 20, 30 , 40 , 50}
for number in numbers:
    dividers = []
    for divider in range(1, number):
        if number % divider == 0:
            dividers.append(divider)
    result[number] = dividers
print(result)

с = {number: [divider for divider in range(1, number + 1) if number % divider == 0] for number in numbers}
