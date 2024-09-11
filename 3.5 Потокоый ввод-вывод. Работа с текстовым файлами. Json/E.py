from sys import stdin
words = set()
strings = stdin.readlines()
for string in strings:
    for word in string[:-1].split():
        if word.lower() == word.lower()[::-1]:
            words.add(word)
print('\n'.join(sorted(words)))
###
from sys import stdin
words = [word for word in stdin.read().split() if word]
result = [word for word in sorted(set(words)) if word.lower() == word[::-1].lower()]
print("\n".join(result))