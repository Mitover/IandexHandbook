ask = 500
delta = ask // 2
str = ''
while str != 'Угадал!':
    print(ask)
    str = input()
    if str == 'Меньше':
        ask = ask - delta
    if str == 'Больше':
        ask = ask + delta
    if delta >= 2:
        delta = (delta + 1) // 2
###
ask = 500
delta = ask // 2
listInput = ["Меньше", "Меньше", "Меньше", "Больше", "Больше", "Больше", "Больше", "Больше" , "Угадал!"]
str = ''
for str in listInput:
 
    print(ask)
    if str == 'Меньше':
        ask = ask - delta
    if str == 'Больше':
        ask = ask + delta
    if delta >= 2:
        delta = (delta + 1) // 2
