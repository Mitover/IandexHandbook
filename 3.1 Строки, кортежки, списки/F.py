count = int(input())
rabbits  = 0
for _ in range(count):
    string = input()
    rabbits  += string.count('зайка')
print(rabbits )


#----------------
n = int(input())
rabbits = 0
for i in range(n):
    words = input()
    rabbits += words.split().count("зайка")
print(rabbits)