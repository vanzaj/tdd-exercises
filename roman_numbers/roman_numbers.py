def roman_number_letter_map(reverse=False):
    _map = [
        (1, "I"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (50, "L"),
        (90, "XC"),
        (100, "C"),
    ]
    return sorted(_map, key=lambda x: x[0], reverse=reverse)


def convert_arabic_to_roman(arabic):
    result = ""
    for value, symbol in roman_number_letter_map(reverse=True):
        while arabic >= value:
            result += symbol
            arabic -= value
    return result
