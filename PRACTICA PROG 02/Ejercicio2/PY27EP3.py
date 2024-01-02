# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
# 3) Imprimir las dos listas generadas.

# 1) Cargar una lista de 10 elementos enteros.
def cargar_lista():
    lista = []
    for i in range(10):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
    return lista

# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
def separar_positivos_negativos(lista):
    positivos = []
    negativos = []
    for elemento in lista:
        if elemento >= 0:
            positivos.append(elemento)
        else:
            negativos.append(elemento)
    return positivos, negativos

# 3) Imprimir las dos listas generadas.
def imprimir_listas(positivos, negativos):
    print("Lista de valores positivos:", positivos)
    print("Lista de valores negativos:", negativos)


 # 1) Cargar una lista de 10 elementos enteros.
lista_original = cargar_lista()

# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
positivos, negativos = separar_positivos_negativos(lista_original)

# 3) Imprimir las dos listas generadas.
imprimir_listas(positivos, negativos)
