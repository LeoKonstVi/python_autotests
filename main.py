import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '57b67a5524a9d03c6f23439327278682'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# создание покемона
# тело запроса для создания покемона
body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon) 
print(response_create_pokemon.text) 
# получение id созданного покемона
pokemon_id = response_create_pokemon.json()['id']

# смена имени покемона
# тело запроса на смену имени
change_name = {
    "pokemon_id": pokemon_id,
    "name": "Новое имя"
}
# запрос не смену имени покемона
response_change_pokemons_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = change_name)
print(response_change_pokemons_name.text)

# поймать покемона в покебол
# тело запроса для метода поймать покемона в покебол
pokemon_id_pokeboll = {
    "pokemon_id": pokemon_id
}
# запрос поймать покемона в покебол
response_pokemon_in_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokemon_id_pokeboll)
print(response_pokemon_in_pokeboll.text)