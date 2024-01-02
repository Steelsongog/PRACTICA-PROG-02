# Realizar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 10 enteros.
# 2) Recibir una lista y retornar otra con la primera mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
# 3) Imprimir una lista.

def cargar_lista():
    lista = []
    for _ in range(10):
        numero = int(input("Ingrese un número entero: "))
        lista.append(numero)
    return lista

def obtener_primera_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    print("Lista:")
    print(lista)

# Programa principal
lista_enteros = cargar_lista()
primera_mitad = obtener_primera_mitad(lista_enteros)
imprimir_lista(primera_mitad)
