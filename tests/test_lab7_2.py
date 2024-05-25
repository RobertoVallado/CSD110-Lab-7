import util

import src.lab7_2 as lab

def test_shift_0():
    actual = lab.shift("abc", 0)
    expected = "abc"
    assert util.output_is_equivalent(actual, expected), util.format_message("Shift of 0 doesn't work", expected, actual)

def test_shift_positive():
    actual = lab.shift("abcdef", 1)
    expected = "fabcde"
    assert util.output_is_equivalent(actual, expected), util.format_message("Shift of 1 doesn't work", expected, actual)

def test_shift_full_length():
    actual = lab.shift("abcdef", 6)
    expected = "abcdef"
    assert util.output_is_equivalent(actual, expected), util.format_message("Full-length shift doesn't work", expected, actual)

def test_shift_full_length_negative():
    actual = lab.shift("abcdef", -6)
    expected = "abcdef"
    assert util.output_is_equivalent(actual, expected), util.format_message("Full-length negative shift doesn't work", expected, actual)

def test_shift():
    actual = lab.shift("abcde", 4)
    expected = "bcdea"
    assert util.output_is_equivalent(actual, expected), util.format_message("Shift of 4 doesn't work", expected, actual)

def test_shift_negative():
    actual = lab.shift("abcdef", -1)
    expected = "bcdefa"
    assert util.output_is_equivalent(actual, expected), util.format_message("Shift of -1 doesn't work", expected, actual)

def test_shift_past_end():
    actual = lab.shift("abcdef", 7)
    expected = "fabcde"
    assert util.output_is_equivalent(actual, expected), util.format_message("Shift past end doesn't work", expected, actual)