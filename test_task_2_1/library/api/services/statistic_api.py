from test_task_2_1.library.api.base_api_client import BaseApiClient


class StatisticApi(BaseApiClient):
    path = 'statistic'

    def get_statistic_by_id(self, item_id):
        response = self.get(path=f'{self.path}/{item_id}')
        return response
