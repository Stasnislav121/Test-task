from test_task_2_1.library import *
import allure


class TestItemId:
    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[200] GET /item/:id - получение данных о товаре по существующему id')
    def test_get_data_item_by_existing_id(self):
        expect_item_id = '7a8fe969-2a57-468e-82c9-1982d22023c5'

        with allure.step(f'Выполнить запрос GET /api/1/item/{expect_item_id}'):
            client = ItemApi()
            response = client.get_data_item_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, get_item_data_by_id_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()[0]
            actual_item_id = actual_data['id']
            assert expect_item_id == actual_item_id, f'Ожидалось "id": {expect_item_id}, получено {actual_item_id}'
