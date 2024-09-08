# Example of a function inside module1 which is part of package_a
# Q: How do we import and test it if tests are outside of the package?
# A: Make sure $PYTHONPATH contains "." (which is not the case by default when running `pytest`)

def func_zero():
    return 0

