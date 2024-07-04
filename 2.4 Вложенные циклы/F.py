#I
count = int(input())
gcd = int(input())
for _ in range(count - 1):
    number = int(input())
    while number != 0 and gcd != 0:
        if number >= gcd:
            number %= gcd
        else:
            gcd %= number
    gcd = gcd + number
print(gcd)
#II
count = int(input())
gcd = int(input())
number = 0
for _ in range(count - 1):
    number = int(input())
    while number != 0:
        gcd, number = number, gcd % number
print(gcd)