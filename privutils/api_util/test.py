import unittest
from unittest import mock
import json
from .api_caller import ApiCaller
from .api_exception import *

def mocked_requests_get(*args, **kwargs):
  class MockResponse:
    def __init__(self, json_data, status_code):
      self.text = json_data
      self.status_code = status_code

    def json(self):
      return json.loads(self.text)

  return MockResponse(kwargs['params'], int(args[0]))

def mocked_requests_post(*args, **kwargs):
  class MockResponse:
    def __init__(self, json_data, status_code):
      self.text = json_data
      self.status_code = status_code

    def json(self):
      return json.loads(self.text)

  return MockResponse(kwargs['json'], int(args[0]))

def mocked_requests_delete(*args, **kwargs):
  class MockResponse:
    def __init__(self, json_data, status_code):
      self.text = json_data
      self.status_code = status_code

    def json(self):
      return json.loads(self.text)

  return MockResponse(kwargs['params'], int(args[0]))



class TestApiCaller(unittest.TestCase):
  def setUp(self):
    self.tgt = ApiCaller(endpoint = '')

  def tearDown(self):
    del self.tgt

  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_get(self, request_get):
    response = self.tgt.get('200', '{"k": "v"}')
    self.assertEqual(response, {"k": "v"})

  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_exception_get(self, request_get):
    with self.assertRaises(Response4xx):
      self.tgt.get('400', '{"k": "v"}')
    with self.assertRaises(Response5xx):
      self.tgt.get('500', '{"k": "v"}')
    with self.assertRaises(NonJsonResponse):
      self.tgt.get('200', '{non_json_response')
    with self.assertRaises(Response5xx):
      self.tgt.get('500', '{non_json_response')

  @mock.patch('requests.post', side_effect=mocked_requests_post)
  def test_post(self, request_post):
    response = self.tgt.post('200', '{"k": "v"}')
    self.assertEqual(response, {"k": "v"})

  @mock.patch('requests.post', side_effect=mocked_requests_post)
  def test_exception_post(self, request_post):
    with self.assertRaises(Response4xx):
      self.tgt.post('400', '{"k": "v"}')
    with self.assertRaises(Response5xx):
      self.tgt.post('500', '{"k": "v"}')
    with self.assertRaises(NonJsonResponse):
      self.tgt.post('200', '{non_json_response')
    with self.assertRaises(Response5xx):
      self.tgt.post('500', '{non_json_response')

  @mock.patch('requests.delete', side_effect=mocked_requests_delete)
  def test_delete(self, request_delete):
    response = self.tgt.delete('200', '{"k": "v"}')
    self.assertEqual(response, {"k": "v"})

  @mock.patch('requests.delete', side_effect=mocked_requests_delete)
  def test_exception_delete(self, request_delete):
    with self.assertRaises(Response4xx):
      self.tgt.delete('400', '{"k": "v"}')
    with self.assertRaises(Response5xx):
      self.tgt.delete('500', '{"k": "v"}')
    with self.assertRaises(NonJsonResponse):
      self.tgt.delete('200', '{non_json_response')
    with self.assertRaises(Response5xx):
      self.tgt.delete('500', '{non_json_response')

