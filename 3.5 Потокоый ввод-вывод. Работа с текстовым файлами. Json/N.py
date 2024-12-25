import json
json_name = input()
json_update = input()
with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)
name_key = 'name'
new_dict = {}
for data in source:
    name = data.pop(name_key)
    new_dict[name] = data
for data in updates:
    name = data.pop(name_key)
    if name not in new_dict:  
        new_dict[name] = {}
    for key in data.keys():
        if new_dict[name].get(key, '') < data[key]:
            new_dict[name][key] = data[key]
with open(json_name, 'w') as file:
    json.dump(new_dict, file, sort_keys=False, indent=4, ensure_ascii=False)
###
import json
json_name = input()
json_update = input()
with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)
name_key = 'name'
new_dict = {}
for update in updates:
    for data in source:
        if update[name_key] == data[name_key]:
            for key in update.keys():
                if update[key] > data.get(key, ''):
                    data[key] = update[key]
for data in source:
    name = data.pop(name_key)
    new_dict[name] = data
with open(json_name, 'w') as file:
    json.dump(new_dict, file, sort_keys=False, indent=4, ensure_ascii=False)
###
import json
json_name = input()
json_update = input()
with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)
users = {}
for data in source:
    name = data['name']
    value = {}
    users[name] = value
    for key in data.keys():
        if key != 'name':
            value[key] = data[key]

for user in updates:
    name = user['name']
    for key in user.keys():
        if key != 'name':
            if users[name].get(key, '') < user[key]:
                users[name][key] = user[key]
with open(json_name, 'w') as file:
    json.dump(users, file, indent=4, ensure_ascii=False)
#####
import json
json_name = input()
json_update = input()
with open(json_name, encoding="UTF-8") as file_in:
    filen = json.load(file_in)
with open(json_update, encoding="UTF-8") as file_in:
    filek = json.load(file_in)
a = {}
for i in filek:
    a[i["name"]] = {}
    for v in i:
        if v != "name":
            a[i["name"]][v] = i[v]
for i in filen:
    for v in i:
        if v != "name": 
            if v in a[keyName]:
                if i[v] > a[keyName][v]:
                    a[i["name"]][v] = i[v]
            else:
                a[i["name"]][v] = i[v]   
        else:
            keyName = i[v]
print(a)
with open(json_name, 'w') as file:
    json.dump(a, file, indent=4, ensure_ascii=False)