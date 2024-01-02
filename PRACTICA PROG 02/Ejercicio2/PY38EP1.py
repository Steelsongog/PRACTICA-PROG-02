# Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
# Confeccionar un programa con las siguientes funciones:
# 1) Cargar una lista con 5 palabras.
# 2) Intercambiar la primer palabra con la última.
# 3) Imprimir la lista

    
def cargar_lista():
    palabras = []
    for _ in range(5):
        palabra = input("Ingrese una palabra: ")
        palabras.append(palabra)
    return palabras

def intercambiar_primer_y_ultima(lista):
    if len(lista) >= 2:
        lista[0], lista[-1] = lista[-1], lista[0]

def imprimir_lista(lista):
    print("Lista:")
    print(lista)

# Programa principal
lista_palabras = cargar_lista()
intercambiar_primer_y_ultima(lista_palabras)
imprimir_lista(lista_palabras)
