import allure
import requests
from data import Url, Message
from helpers import generated_courier


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier(self, delete_courier):
        payload = delete_courier
        response = requests.post(Url.CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.text == Message.SUCCESSFULL_RESPONSE

    @allure.title('Невозможность создания двух одинаковых курьеров')
    def test_impossibility_create_identical_courier(self, delete_courier):
        payload = delete_courier
        requests.post(Url.CREATE_COURIER, data=payload)
        identical_courier = requests.post(Url.CREATE_COURIER, data=payload)
        assert identical_courier.status_code == 409
        assert identical_courier.json()['message'] == Message.CONFLICT_LOGIN

    @allure.title('Создание курьера без логина')
    def test_create_courier_no_login(self):
        payload = generated_courier()
        payload['login'] = ''
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == Message.NOT_ENOUGH_DATA

    @allure.title('Создание курьера без пароля')
    def test_create_courier_no_password(self):
        payload = generated_courier()
        payload['password'] = ''
        response = requests.post(Url.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == Message.NOT_ENOUGH_DATA
