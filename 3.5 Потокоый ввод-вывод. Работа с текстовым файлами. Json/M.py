from sys import stdin
import json
json_name = input()
with open(json_name) as file:
    data = json.load(file)
lines = stdin.readlines()
for line in lines:
    if line:
        list = line.split('==')
        data[list[0].strip()] = list[1].strip()
with open(json_name, 'w') as file:
    json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)