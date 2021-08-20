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
            - name: this should be the name of the company
        Response:
        Business details (200 status code)
        Empty json (400 status code)
        '''

        url = self._BASE_URL + '/v1/cac/lookup'
        status, response = self._make_request('GET', url, params=kwargs)
        return status, response
        