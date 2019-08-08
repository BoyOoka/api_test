import pytest

A = 3
# @pytest.fixture()
# def db():
#     print('Connection successful')
#
#     yield
#
#     print('Connection closed')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


@pytest.fixture(scope='function', autouse=True)
def func_scope():
    print('func_scope')
    pass


@pytest.fixture(scope='module', autouse=True)
def mod_scope():
    print('mod_scope')
    pass


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        # class_scope_step()
        pass
    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='session', autouse=True)
def sess_scope():
    print('session_scope')
    pass


@pytest.fixture(scope='class', autouse=True)
def class_scope():
    print('class_scope1')
    A=+1
    print('class_scope', A)
    yield
    print('class_scope2')


def test_search():
    print('search', 1)
    assert search_user('001') == 'xiaoming'


# @pytest.mark.usefixtures('class_scope')
class TestClassScope(object):

    def test_1(self):
        print('test1', A)

    def test_2(self):
        print('test2', A)
        pass

    def test_3(self):
        print('test3', A)
        pass
