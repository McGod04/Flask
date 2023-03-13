'''Que filme é retornado quando acessamos o endpoint films/1 ?'''

import requests
response = requests.get('https://swapi.dev/api/films/1')

print(response.status_code)
 
from pprint import pprint
pprint(response.json())