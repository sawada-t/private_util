# coding:utf-8

import json
import requests
from privutils.api_util.api_exception import * 

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

    def get(self, path, headers={}, params={}):
        url = f"{self.endpoint}{path}"
        response = requests.get(
            url,
            headers = headers,
            params = params,
        )
        self.__check_status_code(url, response)
        return self.__extract_json(response)

    def post(self, path, headers={}, params={}):
        url = f"{self.endpoint}{path}"
        response = requests.post(
            url,
            headers = headers,
            json = params,
        )
        self.__check_status_code(url, response)
        return self.__extract_json(response)

    def put(self, path, headers={}, params={}):
        url = f"{self.endpoint}{path}"
        response = requests.put(
            url,
            headers = headers,
            params = params,
        )
        self.__check_status_code(url, response)
        return self.__extract_json(response)

    def delete(self, path, headers={}, params={}):
        url = f"{self.endpoint}{path}"
        response = requests.delete(
            url,
            headers = headers,
            params = params,
        )
        self.__check_status_code(url, response)
        return self.__extract_json(response)

