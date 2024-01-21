words = input()
count = 0
while words != "Приехали!":
    if "зайка" in words:
        count += 1
    words = input()
print(count)
