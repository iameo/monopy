import os
import json
import requests


from .errors import MonoAuthException, HttpMethodException


class BaseAPI:
    """
    Base Mono class
    """
    _BASE_URL = 'https://api.withmono.com'

    def __init__(self, mono_sec_key: None = None) -> None:
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

        http_methods = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        params = kwargs.get('params', None)

        request = http_methods.get(method, None)

        if request is None:
            raise HttpMethodException('unrecognized method; you may only use POST, GET, PUT or DELETE')

        response = request(headers=self._headers(), url=url, params=params)

        if response.status_code >= 400:
            return response.status_code, response.json()
        return response.status_code, response.json()


    def __repr__(self):
        return 'MonopyAPI <%r>' % self._mono_sec_key[:5]
