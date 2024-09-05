import pytest
from roman_numbers import convert_arabic_to_roman


@pytest.mark.parametrize(
    "arabic, roman",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (7, "VII"),
        (11, "XI"),
        (36, "XXXVI"),
        (51, "LI"),
        (349, "CCCXLIX"),
    ],
)
def test_convert_arabic_to_roman(arabic, roman):
    assert convert_arabic_to_roman(arabic) == roman
