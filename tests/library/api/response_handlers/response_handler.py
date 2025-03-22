from datetime import datetime

import pytest
import allure

from requests import Response
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError


class ResponseHandler:
    @staticmethod
    def validate_response(response: Response, schema):
        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as err:
            pytest.fail(f'Ошибка при валидации ответа:\n{err}')

    @staticmethod
    def check_status_code(expect_status_code, actual_status_code):
        with allure.step(f"Проверка кода ответа {expect_status_code}"):
            assert actual_status_code == expect_status_code, (f"Код ответа запроса должен быть {expect_status_code}, "
                                                              f"получен {actual_status_code}")

    @staticmethod
    def check_status_is_200(response):
        ResponseHandler.check_status_code(expect_status_code=200, actual_status_code=response.status_code)

    @staticmethod
    def check_status_is_400(response):
        ResponseHandler.check_status_code(expect_status_code=400, actual_status_code=response.status_code)

    @staticmethod
    def check_status_is_404(response):
        ResponseHandler.check_status_code(expect_status_code=404, actual_status_code=response.status_code)

    @staticmethod
    def check_status_is_500(response):
        ResponseHandler.check_status_code(expect_status_code=500, actual_status_code=response.status_code)

    @staticmethod
    def check_datas_for_entry(expect_data: dict, actual_data: dict):
        if not expect_data.items() <= actual_data.items():
            result = {}
            for k, v in expect_data.items():
                if k not in actual_data:
                    result[k] = v
                elif actual_data[k] != v:
                    result[k] = (v, actual_data[k])
            return result
        return True

    @staticmethod
    def check_date_format(date_string: str):
        try:
            datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %z")
            return True
        except ValueError:
            return False

    @staticmethod
    def check_seller_id_in_data(data: list, seller_id):
        if not data:
            return 'Получен пустой список'
        for el in data:
            if el['sellerId'] != seller_id:
                return el
        return True
