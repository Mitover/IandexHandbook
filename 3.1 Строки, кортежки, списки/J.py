# strAll = ""
# b = input().lower()
# while b != "финиш":
#     strAll += b 
#     b = input().lower()
# col = 0
# syb = ""
# strAll = sorted(strAll.lower().replace(" ", "")) 
# for i in strAll:
#     if strAll.count(i) > col:
#         col = strAll.count(i)
#         syb = i   
# print(syb)
#--------

chars = []
count = []

words = input()
while words != "ФИНИШ":
    words = words.lower().replace(" ", "")
    for char in words:
        if char not in chars:
            chars.append(char)
            count.append(1)
        else:
            count[chars.index(char)] += 1
    words = input()

mx = 0
charsMx = [] 

for index in range(len(chars)):
    if count[index] > mx:
        mx = count[index]
        charsMx = [chars[index]]
    elif count[index] == mx:
        charsMx.append(chars[index])

    
charsMx.sort()
if len(charsMx) != 0:
    print(charsMx[0])