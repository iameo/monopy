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