# from sys import stdin
# import json
# json_name = "data.json"
# with open(json_name) as file:
#     data = json.load(file)
# lines = stdin.readlines()
# print(lines)
# for line in lines:
#     if line:
#         list = line.split('==')
#         print(list)
#         data[list[0].strip()] = list[1].strip()
# with open(json_name, 'w') as file:
#     json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)
###
# from sys import stdin
# import json
# file_name = input()
# list_words = stdin.read().split('\n')
# with open(file_name) as f:
#     data = json.load(f)
# for line in list_words:
#     if line:
#         spisok2 = line.split('==')
#         print(spisok2)
#         data[spisok2[0].strip()] = spisok2[1].strip()        
# with open(file_name, "w") as file_out:
#     json.dump(data, file_out, ensure_ascii=False, indent=4, sort_keys=False)

import json
text = """one == один
two == два
three == три""".split("\n")

print(text)
file_name = "data.json"
with open(file_name) as f:
    data = json.load(f)
for line in text:
    if line:
        spisok2 = line.split('==')
        print(spisok2)
        data[spisok2[0].strip()] = spisok2[1].strip()  
              
with open(file_name, "w") as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=4, sort_keys=False)
