N = int(input())
dictCoordinates = dict()
for _ in range(N):
    x, y = map(int, input().split())
    key = f"{int(x // 10)} {int(y // 10)}"
    dictCoordinates[key] = dictCoordinates.get(key, 0) + 1
print(max(dictCoordinates.values()))