import json

f = open('towns.json')

data = json.load(f)

for d in data:
    print(d['city'])

    if len(d['name']) > 2:
        print(d['name'][0:-1])
    else:
        print(d['name'])
