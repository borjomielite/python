import requests
import pytest

token = 'c9639ba61dd15a01dfb4ee7cf7dfad99'
host = 'https://api.pokemonbattle.me/v2'


def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 2199})
    assert  respons.status_code == 200 
    
def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 2199})
    assert  respons.status_code == 200  


def test_trainer_name_in_response():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 2199})
    assert  respons.json()['data'][0]['trainer_name'] == 'borjomi'