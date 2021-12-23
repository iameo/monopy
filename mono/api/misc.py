from .base_api import BaseAPI


class Misc(BaseAPI):
    def institutions(self):
        '''
        This resource returns the available institutions on Mono

        Response:
        List of institutions available on Mono (200 status)
        Empty dict (400 status code)
        '''
        url = self._BASE_URL + '/coverage'
        status, response = self._make_request('GET', url)
        return status, response

    def business_lookup(self, **kwargs):
        '''
        This resource returns the information of a business
        params:
            - name: name of the company you want to lookup
        Response:
        Business details (200 status code)
        Empty json (400 status code)
        '''

        url = self._BASE_URL + '/v1/cac/lookup'
        status, response = self._make_request('GET', url, params=kwargs)
        return status, response

    def shareholder_lookup(self, **kwargs):
        '''
        This response returns the information of the shareholder of a business
        params:
            - id: obtained from the business lookup endpoint
        '''

        id = kwargs.pop('id', None)
        url = self._BASE_URL + f'/v1/cac/company/{id}'
        status, response = self._make_request('GET', url)
        return status, response

    def view360(self, **kwargs):
        '''
        This resource returns all the financial accounts that are linked to the BVN specified
        params:
            - bvn: The BVN of the accounts you'd like to retrieve
        '''
        url = self._BASE_URL + '/360view'
        
        status, response = self._make_request('POST', url, json=kwargs)
        return status, response

