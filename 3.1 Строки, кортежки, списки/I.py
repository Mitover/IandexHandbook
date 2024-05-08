text = "!"
while text != "":
    text = input()
    if text[0] == '#':
        continue
    if '#' in text:
        n = text.index('#')
        new_text = text[:n]
        print(new_text)
    else:
        print(text)
    