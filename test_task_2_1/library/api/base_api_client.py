import requests


class BaseApiClient:
    base_address = 'https://qa-internship.avito.com/api/1/'
    headers = {
        "Content-Type": "application/json"
    }

    def post(self, path='/', headers=None, data=None):
        url = self.base_address + path
        if headers is None:
            headers = self.headers
        response = requests.post(url=url, headers=headers, json=data)
        return response

    def get(self, path='/', headers=None, params=None):
        url = self.base_address + path
        if headers is None:
            headers = self.headers
        response = requests.get(url=url, headers=headers, params=params)
        return response

