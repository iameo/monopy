import os
import pytest
import random

from mono.api.mono_account import Account
from mono.api.errors import MonoAPIException


TEST_MONO_SEC_KEY = 'test_sk_xxxxxxxxxxxx'
acc_ID = 'xxxxxxxxxxxxxxx'


@pytest.fixture(scope="module")
def mono_instance():
    mono_acc = Account(TEST_MONO_SEC_KEY)
    return mono_acc


def test_initialization(mono_instance):
    assert mono_instance is not None


def test_initialization_exception_no_parameters():
    with pytest.raises(MonoAPIException):
        Account(None)


def test_information(mono_instance):
    status, response = mono_instance.information(id=acc_ID)
    assert status and response['account']

def test_statement(mono_instance):
    status, response = mono_instance.statement(id=acc_ID)
    assert status