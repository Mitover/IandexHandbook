with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
length = len(numbers)
total = sum(numbers)
print(length)
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(total)
print(f'{(total / length):.2f}')
###
neg = 0
summ = 0
with open('number.txt', encoding='UTF-8') as f:
    spisok = [int(i) for i in f.read().split()]
    len = len(spisok)
    for _ in spisok:
        if _ > 0:
            neg += 1
    min = min(spisok)
    max = max(spisok)
    summ = sum(spisok)
    sa = summ / len
print(len, neg, min, max, summ, round(sa, 2), sep= '\n')