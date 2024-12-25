from sys import stdin

search_for, *file_names = [string.strip() for string in stdin]
found = False
for file_name in file_names:
    with open(file_name, encoding='UTF-8') as file:
        data = ' '.join(file.read().replace(' ', ' ').lower().split())

        if search_for.lower() in data:
            print(file_name)
            found = True

if not found:
    print('404. Not Found')

#####
from sys import stdin
phrase = stdin.read().split("\n")
phrase = [i.strip() for i in phrase]
text = phrase[0] 
d = 0
for i in phrase[1:]:
    if i:
        with open(i, encoding='UTF-8') as f:
            f = ' '.join(f.read().lower().replace('&nbsp', ' ').split())
            if text.lower() in f:
                d += 1
                print(i)

if d == 0:
    print('404. Not Found')
