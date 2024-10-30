input_file = input()
evens_file = input()
odds_file = input()
equals_file = input()
with open(input_file, encoding="UTF-8") as file:
    strings = [string for string in file.read().split("\n") if string]
even_digits = "02468"
odd_digits = "13579"

for string in strings:
    evens, odds, equals = [], [], []
    for number in string.split():
        total_evens = total_odds = 0
        for char in number:
            if char in even_digits:
                total_evens += 1
            elif char in odd_digits:
                total_odds += 1

        if total_evens > total_odds:
            evens.append(number)
        elif total_evens < total_odds:
            odds.append(number)
        else:
            equals.append(number)

with open(evens_file, "a", encoding="UTF-8") as file:
    file.write(" ".join(evens) + "\n")
with open(odds_file, "a", encoding="UTF-8") as file:
    file.write(" ".join(odds) + "\n")
with open(equals_file, "a", encoding="UTF-8") as file:
    file.write(" ".join(equals) + "\n")
###
input_file = "numbers.txt"
evens_file = "even.txt"
odds_file = "odd.txt"
equals_file = "eq.txt"

with open(input_file, encoding='UTF-8') as file_in:
    list_numbers = [string for string in file_in.read().split("\n") if string]


for numbers in list_numbers:
    even_list = []
    odd_list = []
    equals_list = []

    for number in numbers.split():
        odd = 0
        even = 0
        for num in number:
            if int(num) % 2 == 0:
                even += 1
            else:
                odd += 1

        if even > odd:
            even_list.append(number)
        elif even < odd:
            odd_list.append(number)
        else:
            equals_list.append(number)
    
    with open(evens_file, 'a', encoding='UTF-8') as file_out1:
        file_out1.write(' '.join(even_list) + "\n")
    with open(odds_file, 'a', encoding='UTF-8') as file_out2:
        file_out2.write(' '.join(odd_list) + "\n")
    with open(equals_file, 'a', encoding='UTF-8') as file_out3:
        file_out3.write(' '.join(equals_list) + "\n")
    
    