expression = input()
tokens = expression.split()

uno = ['~', '#', '!']
duo = ['+', '-', '*', '/']
trio = ['@']
operators = uno + duo + trio

stack = []

while tokens != []:
    token = tokens.pop(0)
    if token in uno:
        a = stack.pop()
        if token == '~':
            stack.append(-a)
        elif token == '!':
            res = 1
            for i in range(1, a + 1):
                res *= i
            stack.append(res)
        elif token == '#':
            stack.append(a)
            stack.append(a)
    elif token in duo:
        a = stack.pop()
        b = stack.pop()
        if  token == '+':
            stack.append(b + a)
        elif token == '-':
            stack.append(b - a)
        elif token == '*':
            stack.append(b * a)
        elif token == '/':
            stack.append(b // a)
    elif token in trio:
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()
        if token == '@':
            stack.append(b)
            stack.append(a)
            stack.append(c)
    else:
        stack.append(int(token))

print(int(stack[-1]))