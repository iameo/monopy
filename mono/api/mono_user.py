from .base_api import BaseAPI

class UserMono(BaseAPI):

    def transaction(self, **kwargs):
        """
        Fetch all transactions done by Account ID.
        params:
            - id: Account ID
            - start: start period of the transactions eg. 01-10-2020
            - end: end period of the transactions eg. 07-10-2020
            - narrationstringfilters all transactions by narration e.g Uber transactions
            - type: filters transactions by debit or credit
            - paginate: true or false (If you want to receive the data all at once or you want it paginated)
            - limit: limit the number of transactions returned per API call
        """
        id = kwargs.pop('id')
        url = self._BASE_URL + f'/accounts/{id}/transactions'
        status, response = self._make_request('GET', url, params=kwargs)
        
        return status, response

    def income(self, **kwargs):
        '''
        This resource will return income information on the account. (Beta)
        params:
            - id: Account ID returned from token exchange

        response:
            Type: INCOME (Regular income) or AVG_INCOME (Irregular income)
            Amount: The monthly salary/income
            Confidence: Confidence value in the predicted income
        '''
        id = kwargs['id']
        url = self._BASE_URL + f'accounts/{id}/income'

        status, response = self._make_request('GET', url)
        return status, response


    def identity(self, **kwargs):
        '''
        This resource provides a high level overview of an account identity data.
        params:
            -  id: Account id from token exchange

        note:
            Not all banks will return the identity information. See here https://docs.mono.co/docs/bvn-coverage
        '''

        id = kwargs['id']

        url = self._BASE_URL + f'/accounts/{id}/identity'
        status, response = self._make_request('GET', url)
        return status, response
