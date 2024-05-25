import util

import src.lab7_4 as lab

def test_raises_assertion_on_non_string():
    util.expect_assertion_error(lambda: lab.num_vowels(1), 'num_vowels', 'first', 'is not a string')
def test_raises_correct_assertion_error_message_on_non_string():
    util.assert_assertion_message_equals(lambda: lab.num_vowels(1), "word must be a string containing only letters", "first", "is not a string")

def test_raises_assertion_on_non_letters():
    util.expect_assertion_error(lambda: lab.num_vowels("abc!/{def"), 'num_vowels', 'first', 'contains non-letters')
def test_raises_correct_assertion_error_message_on_non_letters():
    util.assert_assertion_message_equals(lambda: lab.num_vowels("a(*&#_ASKJ"), "word must be a string containing only letters", "first", "contains non-letters")

def check_num_vowels(word, expected):
    assert expected == lab.num_vowels(word), f"'{word}' has {expected} vowel" + "s" if expected == 1 else ""

def test_1():
    check_num_vowels("red", 1)

def test_2():
    check_num_vowels("lynx", 1)

def test_3():
    check_num_vowels("yak", 1)

def test_4():
    check_num_vowels("ympt", 1)

def test_5():
    check_num_vowels("wryly", 2)

def test_6():
    check_num_vowels("reed", 2)

def test_7():
    check_num_vowels("read", 2)

def test_8():
    check_num_vowels("ready", 3)

def test_9():
    check_num_vowels("yesterday", 4)

def test_10():
    check_num_vowels("psychology", 4)

def test_11():
    check_num_vowels("aeiou", 5)

def test_12():
    check_num_vowels("aeiouy", 6)

def test_13():
    check_num_vowels("aeiyyou", 7)

def test_14():
    check_num_vowels("yaeiou", 5)

def test_15():
    check_num_vowels("yaeiyou", 6)