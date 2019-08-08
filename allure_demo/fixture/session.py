import pytest
# conftest.py


@pytest.fixture(scope='session')
def test1():
    sex = '男'
    print('获取到%s' % sex)
    return sex