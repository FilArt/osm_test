import requests
from json import loads


with open("reverse.txt") as test_data:
    for line in test_data.readlines():
        lat, lon, zoom, result = line.split()

        url = "https://nominatim.openstreetmap.org/reverse.php?format=json&lat={}&lon={}&zoom={}".format(lat, lon, zoom)
        r = requests.get(url)

        res = loads(r.content.decode('utf-8'))
        place = res['display_name']

        if result not in place:
            print("test for {} failed".format(result), end=", ")
            print("real place is {}".format(place))
