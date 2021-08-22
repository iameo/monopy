from .base_api import BaseAPI


class Wallet(BaseAPI):
    def balance(self):
        '''
        This resource checks the available balance of the authenticated user
        '''
        url = self._BASE_URL + '/users/stats/wallet'
        status, response = self._make_request('GET', url)
        return status, response