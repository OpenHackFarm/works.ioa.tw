#!/usr/bin/env python
# encoding: utf-8

import json
import requests
import io

towns = []

c = requests.get('https://works.ioa.tw/weather/api/all.json')

for city in json.loads(c.text):
    print 'fetch', city['id']
    t = requests.get('https://works.ioa.tw/weather/api/cates/%d.json' % int(city['id']))
    for town in json.loads(t.text)['towns']:
        _ = town
        _['city'] = city['name']
        towns.append(_)

with io.open('towns.json', 'w', encoding='utf8') as json_file:
    data = json.dumps(towns, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    json_file.write(data)
