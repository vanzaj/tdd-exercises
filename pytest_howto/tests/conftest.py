import pytest


@pytest.fixture(scope="module")
def fake_setup_and_teardown():
    print("\n=== setup ===")
    yield
    print("\n=== teardown ===")
