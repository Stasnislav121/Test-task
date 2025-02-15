from test_task_2_1.library import *
import allure
import pytest


class TestStatisticId:
    @allure.feature('API')
    @allure.story('API: Statistic')
    @allure.title('[404] GET /api/1/statistic/:id - попытка получения данных о товаре без id')
    def test_get_statistic_item_without_id(self):
        expect_error_text = 'route /api/1/statistic/ not found'
        expect_item_id = ''

        with allure.step(f'Выполнить запрос GET /api/1/statistic/'):
            client = StatisticApi()
            response = client.get_statistic_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_404(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, not_found_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()
            actual_error_text = actual_item_data['message']
            actual_code = actual_item_data['code']

            assert expect_error_text == actual_error_text, (f'Ожидалось "message": {expect_error_text}, получено'
                                                            f' {actual_error_text}')
            assert actual_code == 400, f'Ожидался "code": "400", получено {actual_code}'

    @allure.feature('API')
    @allure.story('API: Statistic')
    @allure.title('[400] GET /api/1/statistic/:id - попытка получения данных с невалидным id')
    @pytest.mark.parametrize('item_id', [123,
                                         'йцукен',
                                         'af0447953c55417b8039c9590bf6b239',
                                         'af044795!3c55-417b-8039-c9590bf6b239',
                                         'af044795-3c55-417b-8039-c9590b-f6b239',
                                         '!@#$%^&*(){}?><~'])
    def test_get_statistic_with_invalid_id(self, item_id):
        expect_error_text = 'передан некорректный идентификатор объявления'
        expect_item_id = item_id

        with allure.step(f'Выполнить запрос GET/api/1/statistic/{expect_item_id}'):
            client = StatisticApi()
            response = client.get_statistic_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_400(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, bad_request_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()
            actual_error_text = actual_item_data['result']['message']
            actual_code = actual_item_data['status']

            assert expect_error_text == actual_error_text, (f'Ожидалось "message": {expect_error_text}, получено'
                                                            f' {actual_error_text}')
            assert actual_code == '400', f'Ожидался "status": "400", получено {actual_code}'

    @allure.feature('API')
    @allure.story('API: Statistic')
    @allure.title('[404] GET /api/1/statistic/:id - попытка получения данных о товаре c несуществующим id')
    def test_get_statistic_item_nonexistent_id(self):
        expect_item_id = 'af044795-3c55-417b-9999-c9590bf6b239'
        expect_error_text = f'statistic {expect_item_id} not found'

        with allure.step(f'Выполнить запрос GET /api/1/statistic/{expect_item_id}'):
            client = StatisticApi()
            response = client.get_statistic_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_404(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, get_item_statistic_not_found_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()
            actual_error_text = actual_item_data['result']['message']
            actual_code = actual_item_data['status']

            assert expect_error_text == actual_error_text, (f'Ожидалось "message": {expect_error_text}, получено'
                                                            f' {actual_error_text}')
            assert actual_code == '404', f'Ожидался "status": "404", получено {actual_code}'

    @allure.feature('API')
    @allure.story('API: Statistic')
    @allure.title('[400] GET /api/1/statistic/:id - попытка получения данных о товаре c превышением '
                  'граничных значений id')
    @pytest.mark.parametrize('item_id', ['af044795-3c55-417b-9999-c9590bf6b23',
                                         'af044795-3c55-417b-9999-c9590bf6b2391'])
    def test_get_statistic_item_boundary_values_id(self, item_id):
        expect_item_id = item_id
        expect_error_text = 'передан некорректный идентификатор объявления'

        with allure.step(f'Выполнить запрос GET /api/1/statistic/{expect_item_id}'):
            client = StatisticApi()
            response = client.get_statistic_by_id(item_id=expect_item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_400(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, bad_request_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_item_data = response.json()
            actual_error_text = actual_item_data['result']['message']
            actual_code = actual_item_data['status']

            assert expect_error_text == actual_error_text, (f'Ожидалось "message": {expect_error_text}, получено'
                                                            f' {actual_error_text}')
            assert actual_code == '400', f'Ожидался "status": "400", получено {actual_code}'
