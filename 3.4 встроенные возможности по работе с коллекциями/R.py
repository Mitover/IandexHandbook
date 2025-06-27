text = input()
print("a b c f")
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            print(a, b, c, int(eval(text)))

#####

from itertools import product

expression = input()
print('a b c f')
for a, b, c in product([0, 1], repeat=3):
    print(a, b, c, int(eval(expression)))

#####

from itertools import product

expression = input()
print('a b c f')
for a, b, c in product([0, 1], repeat=3):
    print(a, b, c, int(eval(expression, {"a": a, "b": b, "c": c})) )