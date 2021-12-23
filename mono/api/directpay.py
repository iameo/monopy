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

    def pay(self, **kwargs):
        '''
        This resource initializes payment.
        params:
            - amount: amount in kobo (>= 200)
            - description: description of the payment
            - type: payment type (onetime-debit)
            - reference: unqiue reference (auto-generated)
        '''
        url = self._BASE_URL + '/v1/payments/initiate'

        #auto generate the reference key
        kwargs.update({'reference': get_reference()})

        status, response = self._make_request('POST', url, json=kwargs)
        return status, response


    def status(self, **kwargs):
        '''
        This resource checks payment status using the reference number.
        params:
            - reference: Reference passed when initiating payment
        '''
        url = self._BASE_URL + '/v1/payments/verify'
        
        status, response = self._make_request('POST', url, json=kwargs)
        return status, response     
