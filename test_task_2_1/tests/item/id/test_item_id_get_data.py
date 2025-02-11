from test_task_2_1.library import *
import allure


class TestItemId:
    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] GET /api/1/item/:id - получение данных о товаре по существующему id')
    def test_get_data_item_by_existing_id(self, add_item):
        item = add_item
        expect_item_data = item[1]
        expect_item_id = item[0].json()['status'].split(' - ')[1]

        with allure.step(f'Выполнить запрос GET /api/1/item/{expect_item_id}'):
            client = ItemApi()
            response = client.get_data_item_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, get_item_data_by_id_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()[0]
            actual_item_id = actual_item_data['id']
            actual_entry_datas = ResponseHandler.check_datas_for_entry(expect_item_data, actual_item_data)

            assert expect_item_id == actual_item_id, f'Ожидалось "id": {expect_item_id}, получено {actual_item_id}'
            assert actual_entry_datas is True, (f'Ожидалось вхождение {expect_item_data} в {actual_item_data}, '
                                                f'получена разница {actual_entry_datas}')

    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] GET /api/1/item/:id - соответствие даты-времени в параметре "createdAt" формату')
    def test_get_item_check_date_format(self, add_item):
        item = add_item
        expect_item_id = item[0].json()['status'].split(' - ')[1]

        with allure.step(f'Выполнить запрос GET /api/1/item/{expect_item_id}'):
            client = ItemApi()
            response = client.get_data_item_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()[0]
            actual_date = actual_item_data['createdAt']
            actual_format_date_is_valid = ResponseHandler.check_date_format(actual_date)

            assert actual_format_date_is_valid is True, (f'Ожидалось соответствие значения параметра "createdAt" '
                                                         f'формату "%Y-%m-%d %H:%M:%S %z", получено {actual_date}')
