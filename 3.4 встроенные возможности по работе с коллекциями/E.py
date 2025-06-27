from itertools import chain
lst = sorted(set(chain.from_iterable([input().split(", ") for _ in range(3)])))
for index, value in enumerate(lst, 1):
    print(f"{index}. {value}")
#####
text = []
for i in range(3):
    text += input().split(", ")
text = sorted(text)
for i in range(len(text)):
    print(str(i + 1) + ". " + text[i])
####
from itertools import chain
A = input().split(", ")
B = input().split(", ")
C = input().split(", ")
values = list(chain(A, B, C))
X = sorted(values)
for i in range(len(X)):
    print(f"{i + 1}. {X[i]}")