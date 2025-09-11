def reverse(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

def count_vowels(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def to_upper(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s.upper()

def concat(a: str, b: str) -> str:
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")
    return a + b