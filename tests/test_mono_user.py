import os
import pytest
import random

from mono.api.mono_user import UserMono
from mono.api.errors import MonoAPIException



TEST_MONO_SEC_KEY = 'test_sk_xxxxxxxxxxxx'
acc_ID = 'xxxxxxxxxxxxxxx'



@pytest.fixture(scope="module")
def mono_instance():
    mono_user = UserMono(TEST_MONO_SEC_KEY)
    return mono_user


def test_initialization(mono_instance):
    assert mono_instance is not None


def test_initialization_exception_no_parameters():
    with pytest.raises(MonoAPIException):
        UserMono(None)


def test_transaction_log(mono_instance):
    status, response = mono_instance.transaction(id=acc_ID)
    assert status and response['data']

def test_income(mono_instance):
    status, response = mono_instance.income(id=acc_ID)
    assert status

def test_identity(mono_instance):
    status, response = mono_instance.identity(id=acc_ID)
    assert status and response['addressLine1']
