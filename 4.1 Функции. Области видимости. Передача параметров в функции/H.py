def is_palindrome(value):
    if isinstance(value, int) or isinstance(value, float):
        value = str(abs(value))
    return value == value[::-1]

def is_palindrome(value):
    if type(value) is int or type(value) is float:
        value = str(abs(value))
    return value == value[::-1]