from tests.library.api.base_api_client import BaseApiClient


class ItemApi(BaseApiClient):
    path = 'item'

    def get_data_item_by_id(self, item_id):
        response = self.get(path=f'{self.path}/{item_id}')
        return response

    def add_item(self, data):
        response = self.post(path=self.path, data=data)
        return response

