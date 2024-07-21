def make_list(lenght, value = 0):
    return [value for i in range(lenght)]
###
def make_list(lenght, value = 0):
    list = []
    for i in range(lenght):
        list.append(value)
    return list