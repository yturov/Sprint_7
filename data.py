class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER = f'{BASE_URL}/api/v1/courier/login'
    CREATE_ORDER = f'{BASE_URL}/api/v1/orders'
    LIST_ORDERS = f'{BASE_URL}/api/v1/orders'
    DELETE_COURIER = f'{BASE_URL}/api/v1/courier/:'


class Message:
    SUCCESSFULL_RESPONSE = '{"ok":true}'
    CONFLICT_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    NOT_ENOUGH_DATA = 'Недостаточно данных для создания учетной записи'
    NO_LOGIN_OR_PASSWORD = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'


class PersonalDate:
    personal_date = [
        ['Юрий', 'Туров', 'Тверская 34', '1', '+79206539120', '1', '2024-09-09', 'черный', 'BLACK'],
        ['Николай', 'Романов', 'Романовская 93', '10', '+79206539190', '16', '2020-12-31', 'серый', 'GREY'],
        ['Сергей', 'Юсупов', 'Арбатская 32', '15', '+79206539180', '12', '2021-01-01', 'черный и серый', 'BLACK, GREY'],
        ['Елизавета', 'Великая', 'Мясницкая 3', '36', '+79206539170', '5', '2021-07-21', 'без цвета', '']
    ]
