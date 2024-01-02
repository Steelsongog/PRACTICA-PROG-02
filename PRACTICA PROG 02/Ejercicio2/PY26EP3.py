# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

def calcular_producto(lista):
    # Inicializar el producto
    producto = 1

    # Multiplicar cada elemento de la lista
    for elemento in lista:
        producto *= elemento

    return producto

# Ejemplo de uso
lista_enteros = [2, 3, 4, 5]

# Llamar a la función para calcular el producto de la lista
producto_resultante = calcular_producto(lista_enteros)

# Mostrar el resultado en el bloque principal
print(f"El producto de los elementos de la lista {lista_enteros} es: {producto_resultante}")
