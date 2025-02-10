import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '57b67a5524a9d03c6f23439327278682'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18062'

# тест на проверку статус кода запроса тренеров
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

# тест на проверку имени покемона
def test_trainer_name():
    response_trainer = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainer.json()["data"][0]["trainer_name"] == "Lekont"