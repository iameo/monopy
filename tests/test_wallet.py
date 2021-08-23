import os
import pytest


from mono.api.mono_wallet import Wallet
from mono.api.errors import MonoAPIException



TEST_MONO_SEC_KEY = os.environ.get('TEST_MONO_SEC_KEY')


@pytest.fixture(scope="module")
def mono_instance():
    mono_user = Wallet(TEST_MONO_SEC_KEY)
    return mono_user


def test_initialization(mono_instance):
    assert mono_instance is not None


def test_initialization_exception_no_parameters():
    with pytest.raises(MonoAPIException):
        Wallet(None)


def test_wallet_balance(mono_instance):
    # 23rd, August 2019 - this endpoint doesn't run on the main api, \
    # perhaps because of a TEST secret key or no widget selected yet
    status, response = mono_instance.balance()
    assert status and response['balance']
