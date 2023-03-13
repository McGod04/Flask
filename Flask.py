from flask import Flask
import requests

app = Flask(__name__)

personagens = [
    {
        "id": 1,
        "link": 'https://swapi.dev/api/people/1',
    }
]


@app.route("/personagens/<id>")
def obter_personagens(id):
    response = requests.get('https://swapi.dev/api/people/' + id)
    print(response.json())
    return response.json()


@app.route("/starship/<id>")
def obter_naves(id):
    response = requests.get('https://swapi.dev/api/starships/' + id)
    print(response.json())
    return response.json()


@app.route("/personagens-nave/<id>")
def obter_personagens_naves(id):
    personagem = requests.get('https://swapi.dev/api/people/' + id)
    url = personagem.json()["starships"][0]
    nave = requests.get(url).json()
    return nave


@app.route("/personagens-filme/<id>")
def obter_personagens_filmes(id):
    personagem = requests.get('https://swapi.dev/api/people/' + id)
    url = personagem.json()["films"][0]
    filme = requests.get(url).json()
    return filme


@app.route("/personagens-planeta/<id>")
def obter_personagens_planetas(id):
    personagem = requests.get('https://swapi.dev/api/people/' + id)
    url = personagem.json()["planets"][0]
    planeta = requests.get(url).json()
    return planeta


app.run(port=5000, host="localhost", debug=True)
