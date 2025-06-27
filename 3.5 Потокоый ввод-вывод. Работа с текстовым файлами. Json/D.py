from sys import stdin
text = stdin.read().split('\n')[:-1]
for i in text[:-1]:
    if text[-1].lower() in i.lower():
        print(i)
###
from sys import stdin
lines = stdin.readlines()
subject = lines[-1].strip('\n').lower()
objects = lines[:-1]
for line in objects:
    if line.lower().find(subject) + 1:
        print(line.strip('\n'))
###
from sys import stdin
lines = stdin.readlines()
subject = lines[-1].strip('\n').lower()
objects = lines[:-1]
for line in objects:
    if subject in line.lower():
        print(line.strip('\n'))



