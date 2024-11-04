file_in, file_out = input(), input()
data = []
with open(file_in, "r") as file:
    for string in file:
        data.append(string.strip().replace("\t", "").split())
data = [item for item in data if any(item)]
with open(file_out, "w") as file:
    for string in data:
        print(" ".join(string), file=file)
###
file_in = input()
file_out = input()
with open(file_in, encoding="UTF-8") as file_in:
    text = file_in.read()
while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")
text = "\n".join(string.strip() for string in text.split("\n") if string)
with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write(text)
###
spisok2 = []
with open(input(), encoding='UTF-8') as f:
    spisok = f.read().split("\n")
    for i in range(len(spisok)):
        spisok[i] = spisok[i].replace('\t', '').strip()
        while '  ' in spisok[i]:
            spisok[i] = spisok[i].replace('  ', ' ')
        if spisok[i] == '':
            spisok2 = [i for i in spisok if i != '']
with open(input(), 'w', encoding='UTF-8') as c:
    c.write('\n'.join(spisok2))
###
with open(input(), encoding='utf-8', mode='r') as f:
    b = f.read().split('\n')
for i in range(len(b)):
    if b[i] != '':
        while '  ' in b[i] or '\t' in b[i]:
            b[i] = b[i].replace('\t', '').replace('  ', ' ').strip(' ')
print(b)
n = [i for i in b if i != '']
with open(input(), encoding='utf-8', mode='w') as d:
    d.write('\n'.join(n))