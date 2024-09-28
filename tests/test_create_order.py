import allure
import pytest
import requests
from data import Url, PersonalDate


class TestCreateOrder:

    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color",  PersonalDate.personal_date)
    @allure.title('Создания заказа')
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        response = requests.post(Url.CREATE_ORDER, json=payload)
        assert response.status_code == 201
        assert 'track' in response.text
