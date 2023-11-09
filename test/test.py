import pytest


@pytest
def test_login(login):
    if login == True:
        return True
    else:
        return False
    

