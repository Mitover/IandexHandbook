word = input()
while word != "":
    if word[:2] == "##":
        word = word.replace("##", "")
    if word[-3:] == "@@@":
        word = input()
        continue
    print(word)
    word = input()
###
string = input()
while string != "":
    if string[-3:] != '@@@':
        if string[0:2] == '##':
            string = string[2:]
        print(string)
    string = input()
###
string = input()
while string != "":
    if not string.endswith('@@@'):
        if string.startswith('##'):
            string = string[2:]
        print(string)
    string = input()
###
word = input()
listWords = []
while word != "":
    if word[:2] == "##":
        listWords.append(word.replace("##", "")) 
    if word[-3:] == "@@@":
        word = input()
        continue
    listWords.append(word)
    word = input()
for i in listWords:
    print(i)