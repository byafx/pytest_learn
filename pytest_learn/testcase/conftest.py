import pytest


@pytest.fixture(scope='function')
def my_fixture():
    print('前置')
    yield     # return和yield都表示返回的意思，但是return的后面不能有代码，yield返回后面可以接代码
    print('后置')
