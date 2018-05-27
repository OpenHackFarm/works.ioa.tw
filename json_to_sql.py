import json

f = open('towns.json')
stations = json.load(f)

for s in stations:
    print("INSERT INTO `weather_stations` (`source`, `station_id`, `name`, `city`, `town`, `lat`, `lng`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % ('CWB_OA', s['id'], s['name'], s['city'], s['name'], s['position']['lat'], s['position']['lng']))
