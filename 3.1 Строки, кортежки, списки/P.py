length = int(input())
lines = []
for _ in range(int(input())):
    lines.append(input())
for line in lines:
    if length > 3:
        if len(line) >= length - 3:
            line = line[:length - 3] + "..."
        else:
            if length == 4:
                line = line + "..."
        print(line)
        length -= len(line)

