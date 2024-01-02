# Ejercicio 3:
# Crea un programa llamado Loteria.py que le pida al usuario que introduzca los 6 números que
# juega a la lotería (separados por espacios). Entonces, deberá crear una lista con ellos, ordenarla
# 4. Nociones sobre programación funcional
# ascendentemente e imprimirla en pantalla. Además, el programa debe indicar si es una lista válida (es
# decir, los números deben estar entre 1 y 49, inclusive, sin repetirse). 

def validar_lista(numeros):
    # Verificar si la lista tiene 6 elementos
    if len(numeros) != 6:
        return False
    
    # Verificar que los números estén en el rango [1, 49] y no se repitan
    return all(1 <= num <= 49 for num in numeros) and len(set(numeros)) == 6


# Solicitar al usuario que introduzca los 6 números
try:
    entrada = input("Introduce 6 números para la lotería (separados por espacios): ")
    numeros = list(map(int, entrada.split()))
except ValueError:
    print("Error: Introduce números válidos.")

# Verificar y procesar la lista
if validar_lista(numeros):
    # Ordenar la lista
    numeros.sort()

    # Imprimir la lista ordenada
    print("\nLista ordenada de números válidos:")
    print(numeros)

    # Verificar y mostrar información adicional
    print("\nLa lista es válida.")
else:
    print("\nLa lista NO es válida:")
    if len(set(numeros)) != 6:
        print("Hay números repetidos.")
    if any(num < 1 or num > 49 for num in numeros):
        print("Hay números menores que 1 o mayores que 49.")
