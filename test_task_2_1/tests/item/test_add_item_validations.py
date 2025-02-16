from test_task_2_1.library import *
import allure


class TestAddItem:
    @allure.feature('API')
    @allure.story('API: Item')
    @allure.title('[400] POST /api/1/item - создание объявления без обязательных параметров')
    @pytest.mark.parametrize('param', ['name', 'price', 'sellerId'])
    def test_add_item_without_params(self, param):
        expect_error_text = 'Не передан обязательный параметр'
        data = copy.deepcopy(item_request)
        del data[param]

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

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
    @allure.story('API: Item')
    @allure.title('[400] POST /api/1/item - создание объявления с пустыми значениями параметров')
    @pytest.mark.parametrize('param, value', [('name', ''), ('price', None), ('sellerId', None)])
    def test_add_item_with_empty_value_params(self, param, value):
        expect_error_text = 'Не передан обязательный параметр'
        data = copy.deepcopy(item_request)
        data[param] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

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
    @allure.story('API: Item')
    @allure.title('[400] POST /api/1/item -создание объявления с неверным типом данных в значениях '
                  'параметров')
    @pytest.mark.parametrize('param, value', [
        ('name', 12345),
        ('price', '12345'),
        ('price', 12.34),
        ('sellerId', '12345'),
        ('sellerId', 12.34)
    ])
    def test_add_item_with_bad_type_value_params(self, param, value):
        expect_error_text = f'Передан неверный тип данных у параметра {param}'
        data = copy.deepcopy(item_request)
        data[param] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

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
    @allure.story('API: Item')
    @allure.title('[400] POST /api/1/item - создание объявления с невалидными значениями')
    @pytest.mark.parametrize('param, value', [
        ('name', '!@#$%^&*()'),
        ('name', '1234567890'),
        ('name', ' '),
        ('name', 'Ваня Ваня'),
        ('name', 'Ва-ня-Ва-ня'),
        ('name', 'Ваня!Ваня'),
        ('price', -12345),
        ('sellerId', -12345)
    ])
    def test_add_item_with_invalid_values(self, param, value):
        expect_error_text = f'Передан неверный тип данных у параметра {param}'
        data = copy.deepcopy(item_request)
        data[param] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

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
    @allure.story('API: Item')
    @allure.title('[400] POST /api/1/item - создание объявления с превышением граничных значений')
    @pytest.mark.parametrize('param, value', [
        ('name', ''),
        ('name', 'Расположениключевыхсловпогруппамипочастотевключаетв'),
        ('price', 0),
        ('price', 6000000001),
        ('sellerId', 111110),
        ('sellerId', 1000000)
    ])
    def test_add_item_with_exceeding_boundary_values(self, param, value):
        expect_error_text = f'Превышены допустимые значения у параметра {param}'
        data = copy.deepcopy(item_request)
        data[param] = value

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            client = ItemApi()
            response = client.add_item(data=data)

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
