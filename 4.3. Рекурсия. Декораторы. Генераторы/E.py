def result_accumulator(func):
    listQueue = []
    def funcion(*args, method="accumulate", **kwargs):
        listQueue.append(func(*args, **kwargs))
        #print(*args, method, kwargs)
        if method == "drop":
            res = list(listQueue)
            listQueue.clear()
            return res

    return funcion
###
def result_accumulator(func):
    queue = []
    def wrapper(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            queue.append(func(*args, **kwargs))
        elif method == 'drop':
            queue.append(func(*args, **kwargs))
            result = queue[:]
            queue.clear()
            return result
    return wrapper

#example I
@result_accumulator
def a_plus_b(a, b):
    return a + b

print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

#example II
@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))