import phonenumbers
import opencage
import folium
from test import number

from phonenumbers import geocoder

ch_number=phonenumbers.parse(number,"CH")
print (geocoder.description_for_number(ch_number, "en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
from pprint import pprint


key = '630bfb051f0c4427b5adae02d13c9d9c'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(36.8219, 1.2921)
pprint(results)

lat=results[0]['geometry']['lat']

lng=results[0]['geometry']['lng']

print (lat,lng)

mymap=folium.map(location=[lat,lng],)

folium.Marker([lat,lng],popup=d).add_to(mymap)

mymap.save("index.html")