numbers = [3, 1, 2, 3, 2, 2, 1]
w = ' - '.join([str(num) for num in sorted(set(numbers))])
print(w)