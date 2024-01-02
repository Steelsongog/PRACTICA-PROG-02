# Ejercicio 2:
# Haz un programa que le pida al usuario un nombre de imagen, la cargue y, si existe, le pida
# continuamente tamaños a los que la quiera escalar (ancho y alto), y guarde una copia de la imagen
# original con ese tamaño. El nombre de cada imagen escalada tendrá el patrón
# ancho_alto_nombreFicheroOriginal. El proceso terminará cuando el usuario ponga la anchura o altura a
# 0.

from PIL import Image
import os.path

def escalar_imagen(nombre_fichero, ancho, alto):
    # Verificar si el archivo existe
    if not os.path.isfile(nombre_fichero):
        print(f"El archivo '{nombre_fichero}' no existe.")
        return

    # Abrir la imagen original
    imagen_original = Image.open(nombre_fichero)

    # Escalar la imagen
    imagen_escalada = imagen_original.resize((ancho, alto))

    # Obtener el nombre del archivo sin la extensión
    nombre_base, extension = os.path.splitext(nombre_fichero)

    # Crear el nombre del nuevo archivo con el patrón ancho_alto_nombreFicheroOriginal
    nuevo_nombre = f"{ancho}_{alto}_{os.path.basename(nombre_base)}{extension}"

    # Guardar la imagen escalada
    imagen_escalada.save(nuevo_nombre)
    print(f"Imagen escalada guardada como '{nuevo_nombre}'.")


# Pedir al usuario el nombre de la imagen
nombre_imagen = input("Introduce el nombre de la imagen: ")

# Verificar si la imagen existe
if os.path.isfile(nombre_imagen):
    while True:
        try:
            # Pedir al usuario el ancho y alto deseados
            ancho = int(input("Introduce el ancho deseado (0 para salir): "))
            if ancho == 0:
                break
            alto = int(input("Introduce el alto deseado (0 para salir): "))
            if alto == 0:
                break

            # Escalar y guardar la imagen
            escalar_imagen(nombre_imagen, ancho, alto)
        except ValueError:
            print("Por favor, introduce valores numéricos para el ancho y el alto.")
else:
    print(f"El archivo '{nombre_imagen}' no existe.")
