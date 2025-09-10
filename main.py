from functions import reverse, count_vowels

def main():
    texto = "Hola Mundo"
    print("Texto original:", texto)

    # reverse
    print("Texto invertido:", reverse(texto))

    # count_vowels
    print("Cantidad de vocales:", count_vowels(texto))

if __name__ == "__main__":
    main()
