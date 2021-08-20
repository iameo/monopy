from .base_api import BaseAPI

class Account(BaseAPI):
    def information(self, id):
        '''
        This resource represents the account details with the financial institution.
        params:
            - id: Account ID returned from token exchange
        '''

        url = self._BASE_URL + f'/accounts/{id}'
        status, response = self._make_request('GET', url)

        return status, response

    def statement(self, **kwargs):
        '''
        This resource represents the bank statement of the connected financial account.\
        You can query 1-12 months bank statement in one single call.
        params:
            - id: Account ID returned from token exchange
            - period: In months(1-12)
            - output: set the output as pdf if you want to receive pdf instead of Json
        '''
        id = kwargs.pop('id')
        url = self._BASE_URL + f'accounts/{id}/statement'
        status, response = self._make_request('GET', url, params=kwargs)

        return status, response

    def poll_pdf_status(self, **kwargs):
        '''
        use this endpoint to poll the status of statement in PDF
        params:
            - id: Account ID returned from token exchange
            - jobId: ID returned from statements API

        '''
        id = kwargs.pop('id')
        jobId = kwargs.pop('jobId')
        url = self._BASE_URL + f'/accounts/{id}/statement/jobs/{jobId}'
        status, response = self._make_request('GET', url)

        return status, response