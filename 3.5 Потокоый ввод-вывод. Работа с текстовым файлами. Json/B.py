from sys import stdin
lines = stdin.read().split('\n')
delta = 0
count = 0
for line in lines:
    if len(line) != 0:#line
        name, old, now = line.split()
        delta += int(now) - int(old)
        count += 1
print(round(delta / count))
###
from sys import stdin
delta = 0
lines = [line.rstrip('\n') for line in stdin.readlines()]
for line in lines:
    name, old, now = line.split()
    delta += int(now) - int(old)
print(round(delta / len(lines)))