import pytest

from hack.arch import CPU, memory
#import hack

@pytest.fixture
def variable():
    x = 'example message'
    return x

def test_hoge():
    y = CPU.cpu()
    print(y)
    assert y == 10

def test_aa():
    y = CPU.increment(11)
    assert y == 12

def test_aaa(variable):
    print(variable)
    assert variable == 'example message'
