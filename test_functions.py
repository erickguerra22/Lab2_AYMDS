import pytest
import functions as fn

def test_reverse():
    assert fn.reverse("hola") == "aloh"
    assert fn.reverse("a") == "a"
    with pytest.raises(TypeError):
        fn.reverse(123)
        
def test_count_vowels():
    assert fn.count_vowels("hola") == 2
    assert fn.count_vowels("xyz") == 0
    with pytest.raises(TypeError):
        fn.count_vowels(None)