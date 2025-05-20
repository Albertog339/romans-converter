from converter import roman_to_int

def test_roman_to_int():
    assert roman_to_int("I") == 1
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XL") == 40
    assert roman_to_int("XC") == 90
    assert roman_to_int("C") == 100
    assert roman_to_int("CD") == 400
    assert roman_to_int("D") == 500
    assert roman_to_int("CM") == 900
    assert roman_to_int("M") == 1000
