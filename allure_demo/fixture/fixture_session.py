import pytest
from .session import test1


def test3(test1):
    name = '男'
    print('找到name')
    assert test1 == name


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture.py'])