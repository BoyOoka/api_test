import pytest


@pytest.fixture()
def test1():
    a = 'leo'
    return a


def test2(test1):
    assert test1 == 'leo'


if __name__ == '__main__':
    pytest.main('-q test_fixture.py')