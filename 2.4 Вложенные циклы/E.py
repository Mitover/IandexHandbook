size = int(input())
words = ""
terrain = input()
count = 0

for i in range(size):
    while terrain != 'ВСЁ':
        words += terrain
        terrain = input()

    if "зайка" in words:
        count += 1
    words = ""  
    terrain = ""

print(count)

#списки


n = int(input())
a = 0
name = ""
for _ in range(n):
    answers = []
    name = ""
    while name != "ВСЁ": 
        name = input()
        answers.append(name)
    if 'зайка' in answers:
        a += 1    
print(a)