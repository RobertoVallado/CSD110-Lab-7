import util

from src.lab7_1 import isprime

def test_raises_assertion_on_string():
    util.expect_assertion_error(lambda: isprime(2.5), "isprime", "first", "is not an integer")    
def test_raises_correct_assertion_error_message():
    util.assert_assertion_message_equals(lambda: isprime(2.5), "n must be an integer", "first", "is not an integer")

def test_negative_is_not_prime():
    assert isprime(-12) == False, "Negative numbers must be considered non-prime"

def test_0_is_not_prime():
    assert isprime(0) == False, "0 must be considered non-prime"

def test_1_is_not_prime():
    assert isprime(1) == False, "1 must be considered non-prime"

def test_4_is_not_prime():
    assert isprime(4) == False, "4 must be considered non-prime"

def test_6_is_not_prime():
    assert isprime(6) == False, "6 must be considered non-prime"

def test_8_is_not_prime():
    assert isprime(8) == False, "8 must be considered non-prime"

def test_9_is_not_prime():
    assert isprime(9) == False, "9 must be considered non-prime"

def test_25_is_not_prime():
    assert isprime(25) == False, "25 must be considered non-prime"

def test_1001_is_prime():
    assert isprime(1001) == False, "1001 must be considered non-prime"

def test_2_is_prime():
    assert isprime(2) == True, "2 must be considered prime"

def test_3_is_prime():
    assert isprime(3) == True, "3 must be considered prime"

def test_5_is_prime():
    assert isprime(5) == True, "5 must be considered prime"

def test_7_is_prime():
    assert isprime(7) == True, "7 must be considered prime"

def test_101_is_prime():
    assert isprime(101) == True, "101 must be considered prime"

def test_87178291199_is_prime():
    assert isprime(87178291199) == True, "87178291199 must be considered prime"
