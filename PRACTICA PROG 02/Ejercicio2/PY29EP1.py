# Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
# Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. 
# Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tabla_de_multiplicar(valor, termino=10):
    print(f"Tabla de multiplicar del {valor} hasta el término {termino}:")
    for i in range(1, termino + 1):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")

# Llamar a la función desde el bloque principal con argumentos nombrados
valor_parametro = 5
termino_parametro = 8

tabla_de_multiplicar(valor=valor_parametro, termino=termino_parametro)
