# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def contar_vocales(cadena):
    # Inicializar el contador de vocales
    contador = 0

    # Definir las vocales
    vocales = "aeiouAEIOU"

    # Iterar sobre cada caracter en la cadena
    for caracter in cadena:
        # Verificar si el caracter es una vocal
        if caracter in vocales:
            contador += 1

    # Mostrar la cantidad de vocales
    print(f"La cantidad de vocales en '{cadena}' es: {contador}")

# Llamar a la función desde el bloque principal del programa con tres strings distintos
cadena1 = "Hola, mundo!"
contar_vocales(cadena1)

cadena2 = "Python es genial"
contar_vocales(cadena2)

cadena3 = "Programación"
contar_vocales(cadena3)
