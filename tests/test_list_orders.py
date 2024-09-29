import allure
import requests
from data import Url


class TestListOrders:

    @allure.title('Проверка получения списка заказов')
    def test_list_orders(self):
        response = requests.get(Url.LIST_ORDERS)
        assert response.status_code == 200
        assert 'orders' and 'track' in response.text
