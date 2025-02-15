from test_task_2_1.library import *
import allure


class TestAddItem:
    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] POST /api/1/item - создание объявления')
    def test_add_item(self):
        expect_text = 'Сохранили объявление - '
        data = copy.deepcopy(item_request)
        data['sellerId'] = SELLER_ID

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, add_item_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_id = response.json()['status'].split(' - ')[1]
            actual_status = expect_text + actual_item_id

            assert expect_text in actual_status, (f'Ожидалось вхождение {expect_text} в значении параметра "status", '
                                                  f'получено {actual_status}')
            assert len(actual_status) == 59, (f'Ожидалась длина значения "status" = 59, '
                                              f'получено разница {len(actual_status)}')

    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] POST /api/1/item - создание объявления (граничные значения параметров)')
    @pytest.mark.parametrize('param, value', [
        ('sellerId', 111111),
        ('sellerId', 999999),
        ('name', 'й'),
        ('name', 'Абдурахмангаджи'),
        ('price', 1),
        ('price', 6000000000)
    ])
    def test_add_item_boundary_values_params(self, param, value):
        expect_text = 'Сохранили объявление - '
        data = copy.deepcopy(item_request)
        data['sellerId'] = SELLER_ID
        data[param] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, add_item_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_id = response.json()['status'].split(' - ')[1]
            actual_status = expect_text + actual_item_id

            assert expect_text in actual_status, (f'Ожидалось вхождение {expect_text} в значении параметра "status", '
                                                  f'получено {actual_status}')
            assert len(actual_status) == 59, (f'Ожидалась длина значения "status" = 59, '
                                              f'получено разница {len(actual_status)}')

    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] POST /api/1/item - создание объявления (виды имени)')
    @pytest.mark.parametrize('value', ['Анна-Мария', 'КИРИЛЛ', 'sergey', 'MAX', 'Ёжик', 'вася', 'Aркадий', 'КоЛяН'])
    def test_add_item_any_values_name(self, value):
        expect_text = 'Сохранили объявление - '
        data = copy.deepcopy(item_request)
        data['sellerId'] = SELLER_ID
        data['name'] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, add_item_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_id = response.json()['status'].split(' - ')[1]
            actual_status = expect_text + actual_item_id

            assert expect_text in actual_status, (f'Ожидалось вхождение {expect_text} в значении параметра "status", '
                                                  f'получено {actual_status}')
            assert len(actual_status) == 59, (f'Ожидалась длина значения "status" = 59, '
                                              f'получено разница {len(actual_status)}')