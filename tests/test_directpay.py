import os
import pytest
import random

from mono.api.directpay import DirectPay
from mono.api.errors import MonoAuthException


TEST_MONO_SEC_KEY = os.environ.get('TEST_MONO_SEC_KEY')


@pytest.fixture(scope='module')
def mono_instance():
    '''
    mono_instance to handle calls
    '''
    misc = DirectPay(TEST_MONO_SEC_KEY)
    return misc


def test_initialization(mono_instance):
    '''
    assert that mono_instance is not None
    '''
    assert mono_instance is not None


def test_initialization_exception_no_parameters():
    '''
    raise MonoAuthException when mono_sec_key is set to None
    '''
    with pytest.raises(MonoAuthException):
        DirectPay(None)


def test_institutions(mono_instance):
    '''
    test the institutions endpoint to fetch available institutions on MONO
    '''
    status, response = mono_instance.institutions()
    assert status and len(response) >= 1 #at least one or more info present
