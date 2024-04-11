p = 7 - 3 + 2
v = 6 + 3 + 3
n = int(input())
m = int(input())
if (p + n) > (v + m):
    print("Петя")
else:
    print("Вася")

#-------
    
petya = 7
vasya = 6

n_apples = int(input())
m_apples = int(input())

petya = petya - 3 + 2 + n_apples
vasya = vasya + 3 + 5 - 2 + m_apples

if petya > vasya:
    print('Петя')
elif vasya > petya:
    print('Вася')