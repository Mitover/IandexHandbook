from itertools import accumulate
for string in accumulate([word + ' ' for word in input().split()]):
    print(string)
#####
from itertools import accumulate
print('\n'.join(list(accumulate([word + ' ' for word in input().split()]))))
#####
b = input().split()
f = ""
for i in b:
    f += i + " "
    print(f.strip())
#####
from itertools import accumulate
b = [word + ' ' for word in input().split()]
for string in accumulate():
    print(string)