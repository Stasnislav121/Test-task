from test_task_2_1.library.api.base_api_client import BaseApiClient


class SellerIdItemApi(BaseApiClient):
    path = 'item'

    def get_items_by_seller_id(self, seller_id):
        response = self.get(path=f'{seller_id}/{self.path}')
        return response

