import pytest
import hack

@pytest.fixture
def variable():
    x = 'example message'
    return x

def test_hoge():
    assert 1 == 1

def test_and():
    assert hack.logic.boolLogic.And(1,0) == 0

def test_or():
    assert hack.logic.boolLogic.Or(1,1) == 1

