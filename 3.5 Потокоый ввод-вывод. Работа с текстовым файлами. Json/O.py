from sys import stdin
import json
f = 'scoring.json'
awnsers = stdin.read().split()
result = 0
with open(f, encoding='UTF-8') as file_in:
    scoring = json.load(file_in)
for i in scoring:
    points = int(i['points']) / len(i['tests'])
    for g in i['tests']:
        if g['pattern'] in awnsers:
            result += points
print(int(result))
#####
from sys import stdin
import json
json_name = 'scoring.json'
with open(json_name) as file:
    data = json.load(file)
answers = stdin.readlines()
score = 0
for tests in data:
    multiplier = int(tests['points'] / len(tests['tests']))
    for test in tests['tests']:
        result = test['pattern']
        for answer in answers:
            if result == answer.strip('\n'):
                score += multiplier
print(score)
#####
from sys import stdin
import json
json_name = 'scoring.json'
with open(json_name) as file:
    data = json.load(file)
answers = stdin.readlines()
score = 0
while data:
    tests = data.pop(0)
    multiplier = int(tests['points'] / len(tests['tests']))
    for test in tests['tests']:
        result = test['pattern']
        answer = answers.pop(0).strip('\n')
        if result == answer:
            score += multiplier

print(score)