# Ejercicio 4:
# Adapta el ejercicio 2 anterior en un archivo llamado ContarExcepciones.py , y controla el caso en
# que los datos que escriba el usuario como parámetros no sean números enteros, mostrando el mensaje
# "Datos incorrectos" en ese caso.

import sys

def contar(desde, hasta):
    for i in range(desde, hasta + 1):
        print(i)


try:
    # Verificar si se proporcionan dos argumentos numéricos
    if len(sys.argv) != 3:
        raise ValueError("Error: Debes proporcionar dos números como argumentos.")

    # Obtener los argumentos desde la línea de comandos
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])

    # Llamar a la función contar
    contar(desde, hasta)

except ValueError as e:
    print(f"Datos incorrectos. {e}")
    sys.exit(1)


