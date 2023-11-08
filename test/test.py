import pytest
from app import *


@pytest
def test_login(login):
    assert login == login_user
    if login == True:
        return True
    else:
        return False