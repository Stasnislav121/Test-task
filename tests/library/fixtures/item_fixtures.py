import pytest
import copy

from tests.library import *


@pytest.fixture
def add_item():
    data = copy.deepcopy(item_request)
    data['sellerId'] = SELLER_ID
    response = ItemApi().add_item(data=data)
    ResponseHandler.check_status_is_200(response)
    return response, data
