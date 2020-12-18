# coding:utf-8

import json
import requests
from utils.api_util.api_exception import *

class ApiCaller(object):
    endpoint = ''
    logger = None

    def __init__(self, endpoint, logger=None):
        self.endpoint = endpoint
        self.logger = logger

    def __check_status_code(self, url, response):
        if not hasattr(response, 'status_code'):
            raise UnknownResponse(f"- {url}", response.text)
        elif response.status_code/100 == 4:
            raise Response4xx(f"{response.status_code} {url}", response.text)
        elif response.status_code/100 == 5:
            raise Response5xx(f"{response.status_code} {url}", response.text)
        elif response.status_code/100 != 2:
            raise UnknownResponse(f"{response.status_code} {url}", response.text)

    def __extract_json(self, response):
        try:
            return response.json()
        except json.decoder.JSONDecodeError as e:
            raise NonJsonResponse(response, e.msg)

    def __get_header(self):
        return {}

    def get(self, path, params):
        url = f"{self.endpoint}{path}"
        response = requests.get(
            url,
            headers = self.__get_header(),
            params = params,
        )
        self.__check_status_code(url, response)
        return self.__extract_json(response)

    def post(self, path, params):
        response = requests.post(
            path,
            headers = self.__get_header(),
            json = params,
        )
        self.__check_status_code(path, response)
        return self.__extract_json(response)

    def delete(self, path, params):
        response = requests.delete(
            f"{self.endpoint}{path}",
            headers = self.__get_header(),
            params = params,
        )
        self.__check_status_code(path, response)
        return self.__extract_json(response)

