a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("1. Петя")
    if b > c:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася") 
elif b > a and b > c:
    print("1. Вася")
    if a > c:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
elif c > a and c > b:
    print("1. Толя")
    if a > b:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")

#####
pety = int(input()) 
vasy = int(input()) 
toly = int(input()) 
if pety > vasy and pety > toly: 
    print("1. Петя") 
    if vasy > toly: 
        print("2. Вася\n3. Толя") 
    else: 
        print("2. Толя\n3. Вася") 
elif vasy > pety and vasy > toly: 
    print("1. Вася") 
    if pety > toly: 
        print("2. Петя\n3. Толя") 
    else: 
        print("2. Толя\n3. Петя") 
else: 
    print("1. Толя") 
    if vasy > pety: 
        print("2. Вася\n3. Петя") 
    else: 
        print("2. Петя\n3. Вася")
#####
petya = int(input())
vasya = int(input())
tolya = int(input())
if vasya > petya > tolya:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif vasya > tolya > petya:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif petya > vasya > tolya:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif petya > tolya > vasya:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif tolya > petya > vasya:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
elif tolya > vasya > petya:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')

#####
petya = int(input())
vasya = int(input())
tolya = int(input())
if vasya > petya and vasya > tolya:
    print('1. Вася')
elif petya > vasya and petya > tolya:
    print('1. Петя')
elif tolya > vasya and tolya > petya:
    print('1. Толя')

if petya < vasya < tolya or petya > vasya > tolya:
    print('2. Вася')
elif vasya < petya < tolya or vasya > petya > tolya:
    print('2. Петя')
elif vasya < tolya < petya or vasya > tolya > petya:
    print('2. Толя')

if vasya < petya and vasya < tolya:
    print('3. Вася')
elif petya < vasya and petya < tolya:
    print('3. Петя')
elif tolya < vasya and tolya < petya:
    print('3. Толя')
#####
name1 = 'Петя'
name2 = 'Вася'
name3 = 'Толя'
time1 = int(input())
time2 = int(input())
time3 = int(input())
if time1 < time2:
    time1, time2 = time2, time1
    name1, name2 = name2, name1
if time1 < time3:
    time1, time3 = time3, time1
    name1, name3 = name3, name1
if time2 < time3:
    time2, time3 = time3, time2
    name2, name3 = name3, name2
print('1.', name1)
print('2.', name2)
print('3.', name3)