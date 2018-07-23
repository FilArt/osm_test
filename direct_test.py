import requests
from json import loads


with open("direct.txt") as test_data:
    for line in test_data.readlines():
        place, test_lat, test_lon = line.split()

        url = "https://nominatim.openstreetmap.org/search/{}?&format=json&limit=1".format(place)
        r = requests.get(url)
        res = loads(r.content.decode('utf-8'))[0]

        real_lon = res['lon']
        real_lat = res['lat']

        if test_lon != real_lon or test_lat != real_lat:
            print('test for {} failed'.format(place), end=': ')
            print('test lat:', test_lat, 'then real lat:', real_lat, end=', ')
            print('test lon:', test_lon, 'then real lon:', real_lon)
