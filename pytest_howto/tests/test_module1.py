import logging
import pytest
from package_a.module1 import func_zero, say_hello, is_valid_email


def test_func_zero(fake_setup_and_teardown):
    assert func_zero() == 0


def test_raises_exception():
    with pytest.raises(ValueError) as ex:
        is_valid_email("name-at-example.com")
    assert "not valid" in str(ex.value)


# built-in fixture
def test_capture_log(caplog):
    caplog.set_level(logging.INFO)
    is_valid_email("name@example.com")
    assert "validating" in caplog.text


# built-in fixture
def test_capture_stdout(capsys):
    say_hello()
    capture = capsys.readouterr()
    assert capture.out == "Hello World\n"


def test_parametrized_fixture(user_factory):
    user = user_factory("John")
    assert user.name == "John"
