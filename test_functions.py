import pytest
import functions as fn

def test_reverse():
    assert fn.reverse("hola") == "aloh"
    assert fn.reverse("a") == "a"
    with pytest.raises(TypeError):
        fn.reverse(123)
        
def test_count_vowels():
    assert fn.count_vowels("adiós") == 3
    assert fn.count_vowels("xyz") == 0
    with pytest.raises(TypeError):
        fn.count_vowels(None)
        
def test_is_palindrome():
    assert fn.is_palindrome("Ana") is True
    assert fn.is_palindrome("hello") is False
    assert fn.is_palindrome("A man, a plan, a canal, Panama") is True
    with pytest.raises(TypeError):
        fn.is_palindrome(10)
        
def test_to_upper():
    assert fn.to_upper("hola") == "HOLA"
    assert fn.to_upper("Python") == "PYTHON"
    with pytest.raises(TypeError):
        fn.to_upper(3.14)
        
def test_concat():
    assert fn.concat("hola", "mundo") == "holamundo"
    assert fn.concat("", "test") == "test"
    with pytest.raises(TypeError):
        fn.concat("hola", 5)