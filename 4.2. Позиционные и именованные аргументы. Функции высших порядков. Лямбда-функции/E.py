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
    print(arg)
    string = ""
    for i in range(len(arg)):
        if len(arg) != i:
            string += str(arg[i]) + sep
        else:
            string += str(arg[i]) + end
    return string
###
def to_string(*arg, sep=' ', end='\n'):
    a = ""
    for i in arg[:-1]:
        a += str(i) + sep 
    return(a + str(arg[-1]) + end)









result = to_string(1, 2, 3)
print(result)

result = to_string(1, 2, 3, sep = " ? ", end = " привет")
print(result)


result = to_string(1, 2, 3)
print(result)


data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
print(result)
