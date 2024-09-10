import pytest
from package_a.module1 import func_zero, is_valid_email


def test_func_zero(fake_setup_and_teardown):
    assert func_zero() == 0


def test_raises_exception():
    with pytest.raises(ValueError) as ex:
        is_valid_email("name-at-example.com")
    assert "not valid" in str(ex.value)


def test_parametrized_fixture(user_factory):
    user = user_factory("John")
    assert user.name == "John"
