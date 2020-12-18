# coding:utf-8

class ApiResponseError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class Response4xx(ApiResponseError):
    def __init__(self, expression, message):
        super().__init__(expression, message)

class Response5xx(ApiResponseError):
    def __init__(self, expression, message):
        super().__init__(expression, message)

class NonJsonResponse(ApiResponseError):
    def __init__(self, expression, message):
        super().__init__(expression, message)

class UnParsableResponse(ApiResponseError):
    def __init__(self, expression, message):
        super().__init__(expression, message)

class UnknownResponse(ApiResponseError):
    def __init__(self, expression, message):
        super().__init__(expression, message)

