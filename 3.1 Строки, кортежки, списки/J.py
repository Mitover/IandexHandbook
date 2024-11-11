allWord = ""
word = input().lower()
while b != "финиш":
    allWord += b 
    b = input().lower()
maxCountChar = 0
maxChar = ""
strAll = sorted(allWord.lower().replace(" ", "")) 
for char in allWord:
    if allWord.count(char) > maxCountChar:
        maxCountChar = allWord.count(char)
        maxChar = char 
print(maxChar)
###
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

