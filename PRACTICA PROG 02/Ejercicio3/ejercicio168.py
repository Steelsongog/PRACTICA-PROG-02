# Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
# 1) Carga de contactos y su número telefónico.
# 2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
# 3) Imprimir la lista completa de contactos con sus números telefónicos.

def cargar_contactos(agenda):
    while True:
        nombre = input("Ingrese el nombre del contacto (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        telefono = input(f"Ingrese el número telefónico de {nombre}: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} almacenado con éxito.\n")

def modificar_telefono(agenda):
    nombre_buscar = input("Ingrese el nombre del contacto cuyo número desea modificar: ")
    if nombre_buscar in agenda:
        nuevo_telefono = input("Ingrese el nuevo número telefónico: ")
        agenda[nombre_buscar] = nuevo_telefono
        print(f"Número telefónico de {nombre_buscar} modificado con éxito.\n")
    else:
        print(f"No se encontró el contacto {nombre_buscar} en la agenda.\n")

def imprimir_agenda(agenda):
    print("\nLista completa de contactos:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
    print()


agenda_telefonica = {}

while True:
    print("1. Cargar contactos")
    print("2. Modificar número telefónico")
    print("3. Imprimir agenda")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        cargar_contactos(agenda_telefonica)
    elif opcion == '2':
        modificar_telefono(agenda_telefonica)
    elif opcion == '3':
        imprimir_agenda(agenda_telefonica)
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")
