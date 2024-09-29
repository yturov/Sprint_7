import allure
import requests
from data import Url, Message
from helpers import generated_courier


class TestLoginCourier:

    @allure.title('Авторизации курьера со всеми обязательными полями')
    def test_authorization_courier(self, create_courier):
        payload = create_courier
        response = requests.post(Url.LOGIN_COURIER, payload)
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('Авторизации курьера без логина')
    def test_authorization_no_login(self, delete_courier):
        payload = delete_courier
        requests.post(Url.CREATE_COURIER, data=payload)
        payload_no_login = dict(payload)
        payload_no_login['login'] = ''
        response = requests.post(Url.LOGIN_COURIER, data=payload_no_login)
        assert response.status_code == 400
        assert response.json()['message'] == Message.NO_LOGIN_OR_PASSWORD

    @allure.title('Проверка авторизации курьера без пароля')
    def test_authorization_no_password(self, delete_courier):
        payload = delete_courier
        requests.post(Url.CREATE_COURIER, data=payload)
        payload_no_password = dict(payload)
        payload_no_password['password'] = ''
        response = requests.post(Url.LOGIN_COURIER, data=payload_no_password)
        assert response.status_code == 400
        assert response.json()['message'] == Message.NO_LOGIN_OR_PASSWORD

    @allure.title('Авторизации под несуществующим курьером')
    def test_authorization_non_existent_courier(self):
        payload = generated_courier()
        response = requests.post(Url.LOGIN_COURIER, data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == Message.ACCOUNT_NOT_FOUND
