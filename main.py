from functions import reverse, count_vowels, is_palindrome, to_upper, concat

def main():
    menu = """Seleccione una función para probar:
    1. Invertir una cadena
    2. Contar vocales en una cadena
    3. Verificar si una cadena es palíndromo
    4. Convertir una cadena a mayúsculas
    5. Concatenar dos cadenas"""
   
    option = int(input(menu + "\nIngrese el número de la opción: "))
    
    if option == 1:
        s = input("Ingrese una cadena: ")
        print("Cadena invertida:", reverse(s))
    elif option == 2:
        s = input("Ingrese una cadena: ")
        print("Número de vocales:", count_vowels(s))
    elif option == 3:
        s = input("Ingrese una cadena: ")
        print("¿Es palíndromo?:", is_palindrome(s))
    elif option == 4:
        s = input("Ingrese una cadena: ")
        print("Cadena en mayúsculas:", to_upper(s))
    elif option == 5:
        a = input("Ingrese la primera cadena: ")
        b = input("Ingrese la segunda cadena: ")
        print("Cadenas concatenadas:", concat(a, b))
    else:
        print("Opción no válida")
        
    menuRepeat = """¿Desea probar otra función?
    1. Sí
    2. No"""
    
    repeat = int(input(menuRepeat + "\nIngrese el número de la opción: "))
    if repeat == 1:
        main()
    else:
        print("¡Gracias por usar el programa!")

if __name__ == "__main__":
    main()
