# Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. 
# Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
# Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

def cargar_alumnos():
    alumnos = {}
    for _ in range(3):
        dni = input("Ingrese el número de documento del alumno: ")
        materias_notas = []
        for _ in range(int(input("Ingrese la cantidad de materias: "))):
            materia = input("Ingrese el nombre de la materia: ")
            nota = float(input(f"Ingrese la nota de {materia}: "))
            materias_notas.append((materia, nota))
        alumnos[dni] = materias_notas
    return alumnos

def listar_alumnos(alumnos):
    print("Listado de todos los alumnos con sus notas:")
    for dni, materias_notas in alumnos.items():
        print(f"DNI: {dni}")
        for materia, nota in materias_notas:
            print(f"   Materia: {materia}, Nota: {nota}")

def consultar_alumno_por_dni(alumnos):
    dni_consulta = input("Ingrese el número de documento del alumno a consultar: ")
    alumno = alumnos.get(dni_consulta)
    if alumno:
        print(f"Materias y notas del alumno con DNI {dni_consulta}:")
        for materia, nota in alumno:
            print(f"   Materia: {materia}, Nota: {nota}")
    else:
        print(f"No se encontró al alumno con DNI {dni_consulta}")

# Programa principal
diccionario_alumnos = cargar_alumnos()
listar_alumnos(diccionario_alumnos)
consultar_alumno_por_dni(diccionario_alumnos)
