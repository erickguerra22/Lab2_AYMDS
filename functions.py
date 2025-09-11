def reverse(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Se espera una cadena de texto")
    # return s[::-1]
    return s

def count_vowels(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("Se espera una cadena de texto")
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚäëïöüÄËÏÖÜàèìòùÀÈÌÒÙ"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("Se espera una cadena de texto")
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def to_upper(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Se espera una cadena de texto")
    return s.upper()

def concat(a: str, b: str) -> str:
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Se espera la comparación de 2 cadenas de texto")
    return a + b