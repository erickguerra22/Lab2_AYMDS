import pytest
import functions as fn

def test_reverse():
    assert fn.reverse("hola") == "aloh"
    assert fn.reverse("a") == "a"
    with pytest.raises(TypeError):
        fn.reverse(123)