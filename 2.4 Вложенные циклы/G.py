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