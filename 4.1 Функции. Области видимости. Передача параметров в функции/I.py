def is_prime(number):
    if number < 2:
        return False

    divider = 2
    while divider <= number ** 0.5:
        if number % divider == 0:
            return False
        divider += 1
    return True
#####
def is_prime(number):
    if number < 2:
        return False

    for div in range(2, int(number**0.5)):
        if number % div == 0:
            return False
    return True