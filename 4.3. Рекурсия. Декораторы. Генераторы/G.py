def same_type(func):
    def funcion(*args, **kwargs):
        type_of_first = type(args[0])
        if all(type(item) == type_of_first for item in args[1:]):
            return func(*args, **kwargs)
        else:
            print('Обнаружены различные типы данных')
    return funcion
###
def same_type(func):
    def funcion(*args, **kwargs):
        if all(isinstance(item, type(args[0])) for item in args[1:]):
            return func(*args, **kwargs)
        else:
            print('Обнаружены различные типы данных')
    return funcion
###
def same_type(func):
    def funcion(*args, **kwargs):
        if len(set([type(item) for item in args])) == len(args):
            return func(*args)
        print("Обнаружены различные типы данных")
        return False
    return funcion
###
def same_type(func):
    def funcion(*args, **kwargs):
        type_of_first = type(args[0])
        listTrue = []
        for item in args[1:]:
            listTrue.append(type_of_first  == type(item))
        if all(listTrue):
            return func(*args)
        else:
            print("Обнаружены различные типы данных")
    return funcion


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')