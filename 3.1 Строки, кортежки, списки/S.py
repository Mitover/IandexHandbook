string = input()
tokens = string.split(' ')

operators = ['+', '-', '*', '/']
stack = []

while tokens != []:
    value = tokens.pop(0)
    if value.isdigit():
        stack.append(int(value))
    else:
        if value == '+':
            stack.append(stack.pop() + stack.pop())
        elif value == '-':
            stack.append(stack.pop(-2) - stack.pop())
        elif value == '*':
            stack.append(stack.pop() * stack.pop())
        elif value == '/':
            stack.append(stack.pop(-2) / stack.pop())

print(stack[-1])