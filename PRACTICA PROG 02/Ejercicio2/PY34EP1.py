# Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def cargar_personas():
    personas = {}
    for _ in range(4):
        documento = input("Ingrese el número de documento: ")
        nombre = input("Ingrese el nombre de la persona: ")
        personas[documento] = nombre
    return personas

def listar_personas(personas):
    print("Listado completo del diccionario:")
    for documento, nombre in personas.items():
        print(f"Documento: {documento}, Nombre: {nombre}")

def consultar_nombre_por_documento(personas):
    documento_consulta = input("Ingrese el número de documento para consultar el nombre: ")
    nombre = personas.get(documento_consulta, "No se encontró el documento")
    print(f"Nombre de la persona con documento {documento_consulta}: {nombre}")

# Programa principal
diccionario_personas = cargar_personas()
listar_personas(diccionario_personas)
consultar_nombre_por_documento(diccionario_personas)
