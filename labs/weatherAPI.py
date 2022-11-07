import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=f95b1eff1c38bb0bbc41e1902fcfa686' % zip)
data=r.json()
print(data['weather'][0])