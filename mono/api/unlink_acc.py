from .base_api import BaseAPI


class UnlinkAccount(BaseAPI):
    def unlink_account(self, **kwargs):
        '''
        This enables you to provide your customers with the option to unlink their financial account(s)
        params:
            - id: account id
        '''
        id = kwargs['id']
        url = f'https://api.withmono.com/accounts/{id}/unlink'

        status, response = self._make_request('POST', url)
        return status, response

