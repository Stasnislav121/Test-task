import requests


class BaseApiClient:
    base_address = 'https://qa-internship.avito.com/api/1'

    def post(self, path='/', data=None):
        url = self.base_address + path
        response = requests.post(url=url, data=data)
        return response

    def get(self, path='/', params=None):
        url = self.base_address + path
        response = requests.get(url=url, params=params)
        return response

