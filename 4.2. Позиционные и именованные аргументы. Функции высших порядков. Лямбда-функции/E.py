def to_string(*arg, sep=' ', end='\n'):
    string = ''
    arg = list(arg)
    while arg:
        item = arg.pop(0)
        string += str(item)
        if arg:
            string += sep
    return string + end
###
def to_string(*arg, sep=' ', end='\n'):
    return sep.join(str(item) for item in arg) + end
###
def to_string(*arg, sep=' ', end='\n'):
    return sep.join(str(arg[i]) for i in range(len(arg))) + end
###
def to_string(*arg, sep=' ', end='\n'):
    string = ""
    for i in range(len(arg)):
        if len(arg) != i:
            string += str(arg[i]) + sep
        else:
            string += str(arg[i]) + end
    return string

