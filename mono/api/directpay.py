from mono.api.utils import get_reference
from .base_api import BaseAPI

class DirectPay(BaseAPI):
    def institutions(self, **kwargs):
        '''
        This resource returns DirectPay institutions.
        
        '''

        url = self._BASE_URL + f'/v1/institutions?scope="payments"'
        status, response = self._make_request('GET', url)

        return status, response




