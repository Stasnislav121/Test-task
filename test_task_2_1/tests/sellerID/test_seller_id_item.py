from test_task_2_1.library import *
import allure
import pytest


class TestSellerIdItem:
    @allure.feature('API')
    @allure.story('API: _sellerID_item')
    @allure.title('[200] GET /api/1/:sellerID/item - получение товаров продавца')
    def test_get_data_by_seller_id(self):
        seller_id = SELLER_ID

        with allure.step(f'Выполнить запрос GET /api/1/{seller_id}/item'):
            client = SellerIdItemApi()
            response = client.get_items_by_seller_id(seller_id=seller_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, seller_id_item_has_items_schema)

        with allure.step('Проверка параметров ответа'):
            actual_seller_id_item_data = response.json()
            seller_is_owner_items = ResponseHandler.check_seller_id_in_data(data=actual_seller_id_item_data,
                                                                            seller_id=seller_id)

            assert seller_is_owner_items is True, f'Товар {seller_is_owner_items} не принадлежит продавцу'

    @allure.feature('API')
    @allure.story('API: _sellerID_item')
    @allure.title('[200] GET /api/1/:sellerID/item - получение товаров продавца c отсутствующими товарами')
    def test_get_data_by_seller_id_has_not_item(self):
        seller_id = 86764543

        with allure.step(f'Выполнить запрос GET /api/1/{seller_id}/item'):
            client = SellerIdItemApi()
            response = client.get_items_by_seller_id(seller_id=seller_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Проверка параметров ответа'):
            actual_seller_id_item_data = response.json()
            assert actual_seller_id_item_data == [], f'Ожидался пустой список, получено {actual_seller_id_item_data}'

    @allure.feature('API')
    @allure.story('API: _sellerID_item')
    @allure.title('[200] GET /api/1/:sellerID/item - получение товаров продавца после добавления товара')
    def test_get_data_by_seller_id_after_add_item(self):
        seller_id = SELLER_ID
        data = copy.deepcopy(item_request)
        data['sellerId'] = SELLER_ID

        with allure.step(f'Выполнить запрос GET /api/1/{seller_id}/item'):
            client = SellerIdItemApi()
            before_seller_id_item_data = client.get_items_by_seller_id(seller_id=seller_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(before_seller_id_item_data)

        with allure.step(f'Выполнить запрос POST /api/1/item/'):
            response_add_item = ItemApi().add_item(data=data)
            ResponseHandler.check_status_is_200(response_add_item)

        with allure.step(f'Выполнить запрос GET /api/1/{seller_id}/item'):
            after_seller_id_item_data = client.get_items_by_seller_id(seller_id=seller_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(after_seller_id_item_data)

        with (allure.step('Проверка параметров ответа')):
            before_seller_id_item_data = before_seller_id_item_data.json()
            after_seller_id_item_data = after_seller_id_item_data.json()

            assert before_seller_id_item_data != after_seller_id_item_data, f'Данные не изменились'
            assert len(before_seller_id_item_data) < len(after_seller_id_item_data), (
                f'Длина списка {after_seller_id_item_data} после добавления товара меньше списка'
                f' {before_seller_id_item_data} ')

    @allure.feature('API')
    @allure.story('API: _sellerID_item')
    @allure.title('[400] GET /api/1/:sellerID/item - получение ошибки при запросе товаров продавца с невалидным id')
    @pytest.mark.parametrize('seller_id', [999999999999999999999999999,
                                           'dsfghjk',
                                           'выапролд',
                                           '!@#$%^&*()_+{}|?><,.'])
    def test_get_data_by_invalid_seller_id(self, seller_id):
        expect_error_text = 'передан некорректный идентификатор продавца'

        with allure.step(f'Выполнить запрос GET /api/1/{seller_id}/item'):
            client = SellerIdItemApi()
            response = client.get_items_by_seller_id(seller_id=seller_id)

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
