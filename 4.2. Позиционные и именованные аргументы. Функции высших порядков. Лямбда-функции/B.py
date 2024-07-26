def make_matrix(size, value=0):
    if type(size) is int:
        return [[value for j in range(size)] for i in range(size)]
    else:
        return [[value for j in range(size[0])] for i in range(size[1])]
###
def make_matrix(size, value=0):
    if type(size) == int:
        return [[value for j in range(size)] for i in range(size)]
    else:
        return [[value for j in range(size[0])] for i in range(size[1])]
###   
def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for j in range(size)] for i in range(size)]
    else:
        return [[value for j in range(size[0])] for i in range(size[1])]
###
def make_matrix(size, value=0):
    list_numbers = []
    if type(size) == int:
        for _ in range(size):
            for _ in range(size):
                list_numbers.append(value)
        return list_numbers
    else:
        for _ in range(size[0]):
            for _ in range(size[1]):
                list_numbers.append(value)
        return list_numbers