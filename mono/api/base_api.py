import os
import json
import requests


from .errors import MonoAuthException, HttpMethodException
from requests.exceptions import ConnectTimeout, ConnectionError



class BaseAPI:
    """
    Base Mono class
    """
    _BASE_URL = 'https://api.withmono.com'

    def __init__(self, mono_sec_key: str = None) -> None:
        if mono_sec_key is None:
            raise MonoAuthException('your mono secret key is required.')

        self._mono_sec_key = mono_sec_key

    def _headers(self):
        return {
            'Accept': 'application/json',
            'mono-sec-key': self._mono_sec_key,
            'Content-Type': 'application/json'
        }


    def _make_request(self, method, url, **kwargs):

        HTTP_METHODS = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        params = kwargs.get('params', None)
        json = kwargs.get('json', None)

        request = HTTP_METHODS.get(method, None)

        if request is None:
            raise HttpMethodException('unrecognized HTTP method; you may only use POST, GET, PUT or DELETE')

        try:
            response = request(headers=self._headers(), url=url, params=params, json=json)
        except ConnectionError as e:
            return 502, f'Connection Error: {e}'
        except ConnectTimeout as e:
            return 599, f'Connection Timeout: {e}'
        else:
            return response.status_code, response.json()


    def __repr__(self):
        return '%s <%r>' % (self.__class__.__name__, self._mono_sec_key[:5])
