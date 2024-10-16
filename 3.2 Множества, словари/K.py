namesDict = {}
count = int(input())
for _ in range(count):
    name = input()
    namesDict[name] = namesDict.get(name, 0) + 1
countNames = 0
for name in namesDict:
    if namesDict[name] > 1:
        countNames += namesDict[name]
print(countNames)
###
namesDict = {}
count = int(input())
c = 0
while c < count:
    name = input()
    namesDict[name] = namesDict.get(name, 0) + 1
    c += 1
countNames = 0
for name in namesDict:
    if namesDict[name] > 1:
        countNames += namesDict[name]
print(countNames)
###
namesDict = {}
count = int(input())
for _ in range(count):
    name = input()
    if name not in namesDict:
        namesDict[name] = 1
    else:
        namesDict[name] += 1
countNames = 0
for name in namesDict:
    if namesDict[name] > 1:
        countNames += namesDict[name]

print(countNames)