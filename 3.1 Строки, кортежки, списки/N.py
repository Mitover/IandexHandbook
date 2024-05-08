b = input().split()
c = int(input())
for i in range(len(b)):
    b[i] = str(int(b[i])**c)
print(" ".join(b))