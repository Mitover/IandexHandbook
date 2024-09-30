def recursive_digit_sum(num):
    while num >= 10:
        return num % 10 + recursive_digit_sum(num // 10)
    return num
###
def recursive_digit_sum(num):
    return num % 10 + recursive_digit_sum(num // 10) if num else 0
###
def recursive_digit_sum(num):
    if num:
        return num % 10 + recursive_digit_sum(num // 10)
    else:
        return 0
###
def recursive_digit_sum(num):
    num = str(num)
    if num:
        return int(num[0]) + recursive_digit_sum(num[1:])
    else:
        return 0
### not recursive
def recursive_digit_sum(num):
    return sum(*map(int, list(str(num))))
### not recursive