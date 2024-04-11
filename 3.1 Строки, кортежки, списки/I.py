string = input()
while string != "":
    pos = string.find('#') + 1
    if not pos:
        print(string)
    if string[:pos]:
        print(string[:pos])
    string = input()