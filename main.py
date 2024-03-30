import requests

token = 'c9639ba61dd15a01dfb4ee7cf7dfad99'
host = 'https://api.pokemonbattle.me/v2'

response = requests.post(f'{host}/pokemons', json = {
    "name": "Iliana",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } ) 

json_response = response.json()

print(json_response["id"])

id = json_response["id"]

response_activation = requests.put ( f'{host}/pokemons', json = {
    "pokemon_id": id,
    "name": "Gus",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
}, headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } )

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": id,
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token })

print(response_pokeball.text)
