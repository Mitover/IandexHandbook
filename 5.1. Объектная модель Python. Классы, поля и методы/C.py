# def number_length(number):
#     if number < 0:
#         number *= -1
#     return len(str(number))

def number_length(number):
    if number < 0:
        return len(str(number)[1:])
    return len(str(number))

