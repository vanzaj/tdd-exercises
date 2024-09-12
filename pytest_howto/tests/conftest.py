import pytest
from package_a.module1 import User


@pytest.fixture(scope="module")
def fake_setup_and_teardown():
    print("\n=== setup ===")
    yield
    print("\n=== teardown ===")


@pytest.fixture()
def user_factory():
    def create_user(name):
        return User(name)

    return create_user


@pytest.fixture()
def make_user(name):
    return User(name)
