file_name = 'secret.txt'
with open(file_name, encoding='UTF-8') as file:
    data = file.read()
    decoded = ''
    for char in data:
        code = ord(char)
        code = code % 256 if code >= 128 else code
        decoded += chr(code)
    print(decoded)
#####
with open('secret.txt', encoding='UTF-8') as secret:
    s = secret.read()
    for i in s:
        print(chr(ord(i) % 128), end='')