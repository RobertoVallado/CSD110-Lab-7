import util

import src.lab7_3 as lab

def test_raises_assertion_on_non_string():
    util.expect_assertion_error(lambda: lab.cipher(1.5, 1), 'cipher', 'first', 'is not a string')
def test_raises_correct_assertion_error_message_on_non_string():
    util.assert_assertion_message_equals(lambda: lab.cipher(1.5, 1), "s must be a string", "first", "is not a string")

def test_raises_assertion_on_non_integer():
    util.expect_assertion_error(lambda: lab.cipher("abc", 1.0), 'cipher', 'first', 'is not an integer')
def test_raises_correct_assertion_error_message_on_non_integer():
    util.assert_assertion_message_equals(lambda: lab.cipher("abc", 1.0), "n must be an integer", "first", "is not an integer")
    
def check_cipher(message, shift, expected, paren=""):
    actual = lab.cipher(message, shift)
    assert util.output_is_equivalent(expected, actual), util.format_message(f"Incorrect cipher" + f" ({paren})" if paren else "", expected, actual)

def test_typical_cipher_works():
    check_cipher("hij", 3, "EFG", "positive shifts left")

def test_negative_shift_works():
    check_cipher("HIJ", -3, "KLM", "negative shifts right")

def test_shift_of_0_does_nothing():
    check_cipher("ABC", 0, "ABC", "shift of 0 does nothing")

def test_cipher_capitalizes():
    check_cipher("abcdefghijklmnopqrstuvwxyz", 0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "cipher must convert all letters to upper case")

def test_shift_past_beginning():
    check_cipher("ABC", 3, "XYZ")   

def test_shift_across_beginning():
    check_cipher("ABC", 2, "YZA")   

def test_shift_past_end():
    check_cipher("XYZ", -3, "ABC")   

def test_really_big_shift():
    check_cipher("XYZ", 100, "BCD")   

def test_shift_across_end():
    check_cipher("XYZ", -2, "ZAB")   

def cipher_ignores_non_letters():
    check_cipher("Hello, world!", 23, "KHOOR, ZRUOG!", "cipher must leave non-letters unchanged")

def cipher_inverts():
    assert lab.cipher(lab.cipher("Hello, world!", 3), -3) == "HELLO, WORLD!", "calling the cipher of a cipher with the negative shift of the original shift must decode the original cipher"