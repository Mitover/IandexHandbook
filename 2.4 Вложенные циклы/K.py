count = int(input())
simple_counter = 0
for i in range(count):
    number = int(input())
    if number >= 2:
        simple = True
        divider = 2
        while divider <= int(number ** 0.5) and simple:
            if number % divider == 0:
                simple = False
            else:
                divider = divider + 1
        if simple is True:
            simple_counter = simple_counter + 1
print(simple_counter)
###
count = int(input())
simple_counter = 0
for i in range(count):
    number = int(input())
    if number >= 2:
        simple = True
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                simple = False
                break
        if simple is True:
            simple_counter = simple_counter + 1
print(simple_counter)