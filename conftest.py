import pytest
import requests
from data import Url
from helpers import generated_courier


@pytest.fixture(scope="function")
def create_courier():
    payload = generated_courier()
    requests.post(Url.CREATE_COURIER, data=payload)

    yield payload
    receiving_id = requests.post(Url.LOGIN_COURIER, data=payload)
    courier_id = receiving_id.json()['id']
    requests.delete(f'{Url.DELETE_COURIER}/{courier_id}')


@pytest.fixture(scope="function")
def delete_courier():
    data = generated_courier()

    yield data
    receiving_id = requests.post(Url.LOGIN_COURIER, data=data)
    courier_id = receiving_id.json()['id']
    requests.delete(f'{Url.DELETE_COURIER}/{courier_id}')
