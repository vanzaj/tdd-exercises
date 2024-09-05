import pytest
from roman_numbers import convert_arabic_to_roman


def test_convert_arabic_to_roman():
    assert convert_arabic_to_roman(1) == "I"
