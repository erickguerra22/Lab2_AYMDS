from functions import reverse, count_vowels, is_palindrome, to_upper

def main():
    texto = "Hola Mundo"
    print("Texto original:", texto)

    # reverse
    print("Texto invertido:", reverse(texto))

    # count_vowels
    print("Cantidad de vocales:", count_vowels(texto))
    
    # is_palindrome
    palabra1 = "Ana"
    palabra2 = "Python"
    print(f"¿'{palabra1}' es palíndromo?", is_palindrome(palabra1))
    print(f"¿'{palabra2}' es palíndromo?", is_palindrome(palabra2))
    
    # to_upper
    print("Texto en mayúsculas:", to_upper(texto))

if __name__ == "__main__":
    main()
