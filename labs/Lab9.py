import json
import requests

r = requests.get('http://localhost:3000/')
data=r.json()
length = len(data)

x = 0
while x < length:
    
    print(data[x]['name'], 'is', data[x]['color'])
    x = x+1

