from test_task_2_1.library import *
import allure


class TestStatisticId:
    @allure.feature('API')
    @allure.story('API: Statistic')
    @allure.title('[200] GET /api/1/statistic/:id - получение статистики товара по существующему id')
    def test_get_statistic_item_by_existing_id(self):
        item_id = 'f03efd71-323e-4836-ba64-76e9d353b003'

        with allure.step(f'Выполнить запрос GET /api/1/statistic/{item_id}'):
            client = StatisticApi()
            response = client.get_statistic_by_id(item_id=item_id)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_status_is_200(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, get_item_statistic_schema)

        with allure.step('Проверка параметров ответа'):
            actual_statistic_data = response.json()[0]
            actual_contacts = actual_statistic_data['contacts']
            actual_likes = actual_statistic_data['likes']
            actual_view_count = actual_statistic_data['viewCount']

            assert actual_contacts >= 0, f'Ожидалось "contacts": 0 или больше, получено {actual_contacts}'
            assert actual_likes >= 0, f'Ожидалось "likes": 0 или больше, получено {actual_likes}'
            assert actual_view_count >= 0, f'Ожидалось "viewCount": 0 или больше, получено {actual_view_count}'
