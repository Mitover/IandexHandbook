from sys import stdin
text = stdin.read().split('\n')
for i in text:
    if i:
        if i[0] == '#':
            continue
        if '#' in i:
            n = i.index('#')
            new_text = i[:n]
            print(new_text.strip("\n"))
        else:
            print(i)
###
from sys import stdin
for string in stdin:
    if string[0] != '#':
        print(string.split('#')[0].rstrip('\n'))