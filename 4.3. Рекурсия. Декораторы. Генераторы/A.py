def recursive_sum(*args):
    if not args:
        return 0
    return args[0] + recursive_sum(*args[1:]) 
###
def recursive_sum(*args):
    if len(args) != 0:
        return 0
    return args[0] + recursive_sum(*args[1:]) 
###
def recursive_sum(*args):
    while args[1:]:
        return args[0] + recursive_sum(*args[1:])
    return args[0]
###
def recursive_sum(*args):
    return sum(args)
###
def recursive_sum(*args):
    s = 0
    for index in range(len(args)):
        s += args[index]
    return s
###
def recursive_sum(*args):
    s = 0
    for el in args:
        s += el
    return s