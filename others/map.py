import pandas as pd

from metroList import metroList
import geopy
import requests


G = None
ne = None
locator = geopy.Nominatim(user_agent="my_app")

lat = []
lon = []

for i in metroList:
    lat.append(float(i[1]))
    lon.append(float(i[2]))




def req(s):
    loc1 = locator.geocode(s)
    url = 'http://router.project-osrm.org/table/v1/walking/' + str(loc1.latitude) + ',' + str(loc1.longitude)

    for i in metroList:
        url += ';'
        url += i[1]
        url += ','
        url += i[2]

    url += '?sources=0'

    page = requests.get(url)
    ss = page.text[page.text.find('duration') + 15:]
    ns = ""

    for i in ss:
        if i == ']':
            break
        ns += i

    lis = list(map(float, ns.split(',')))

    mi = 100000000000000
    ami = ''

    for i in range(len(lis)):
        if lis[i] < mi:
            mi = lis[i]
            ami = metroList[i][0]

    return (mi, ami)

s = input()
print(req(s))