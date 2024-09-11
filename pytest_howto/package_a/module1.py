# Example of a function inside module1 which is part of package_a
# Q: How do we import and test it if tests are outside of the package?
# A: Make sure $PYTHONPATH contains "." (which is not the case by default when running `pytest`)
import logging


def func_zero():
    return 0


def is_valid_email(email: str) -> bool | ValueError:
    logging.info(f"validating {email}")
    if "@" not in email:
        raise ValueError(f"{email} is not valid")
    return True


class User:
    def __init__(self, name: str):
        self.name = name
