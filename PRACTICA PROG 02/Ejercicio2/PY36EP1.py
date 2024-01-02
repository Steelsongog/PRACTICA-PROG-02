# Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
# Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.
# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar_empleados():
    empleados = {}
    for _ in range(int(input("Ingrese la cantidad de empleados a cargar: "))):
        legajo = input("Ingrese el número de legajo del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        profesion = input("Ingrese la profesión del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        empleados[legajo] = [nombre, profesion, sueldo]
    return empleados

def modificar_sueldo_empleado(empleados):
    legajo_modificar = input("Ingrese el número de legajo del empleado para modificar su sueldo: ")
    if legajo_modificar in empleados:
        nuevo_sueldo = float(input("Ingrese el nuevo sueldo del empleado: "))
        empleados[legajo_modificar][2] = nuevo_sueldo
        print("Sueldo modificado exitosamente.")
    else:
        print(f"No se encontró al empleado con número de legajo {legajo_modificar}")

def mostrar_analistas_de_sistemas(empleados):
    print("Empleados con profesión 'analista de sistemas':")
    for legajo, datos in empleados.items():
        if datos[1] == "analista de sistemas":
            print(f"Legajo: {legajo}, Nombre: {datos[0]}, Profesión: {datos[1]}, Sueldo: {datos[2]}")

# Programa principal
diccionario_empleados = cargar_empleados()
modificar_sueldo_empleado(diccionario_empleados)
mostrar_analistas_de_sistemas(diccionario_empleados)
