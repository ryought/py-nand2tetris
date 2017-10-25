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
    assert y == 0

def test_aaa(variable):
    print(variable)
    assert variable == 'example message'
