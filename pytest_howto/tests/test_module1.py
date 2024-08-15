from package_a.module1 import func_zero


def test_func_zero(fake_setup_and_teardown):
    assert func_zero() == 0
