def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    total = 0
    for char in reversed(s.upper()):
        value = roman.get(char, 0)
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total
