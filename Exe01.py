'''Agora vamos analisar o objeto response. Quais seus métodos e atributos?
 Como saber qual foi o status code da resposta? Quais foram os dados retornados?'''

import requests
response = requests.get('https://swapi.dev/api/people/1')

print(response.status_code)
 
from pprint import pprint
pprint(response.json())