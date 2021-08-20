import os
import pytest
import random

from mono.api.misc import Misc
from mono.api.errors import MonoAuthException

TEST_MONO_SEC_KEY = 'test_sk_xxxxxxxxxxxxx'


@pytest.fixture(scope='module')
def mono_instance():
    '''
    mono_instance to handle calls
    '''
    misc = Misc(TEST_MONO_SEC_KEY)
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
        Misc(None)


def test_institutions(mono_instance):
    '''
    test the institutions endpoint to fetch available institutions on MONO
    '''
    status, response = mono_instance.institutions()
    assert status and len(response) >= 1 #at least one or more info present


def test_business_lookup(mono_instance):
    '''
    test the business lookup endpoint to fetch information about a company
    '''
    # I noticed if name isn't in the db -> Response 504 [time out]
    status, response = mono_instance.business_lookup(name='polaris bank')
    assert status and response[0]['status'] #status -> ACTIVE or INACTIVE 