# Ejercicio 3:
# En un hospital hay diferentes tipos de personal: médicos, enfermeros y administrativos. De todos
# guardamos su información básica (dni, nombre, dirección y teléfono), de los médicos almacenamos
# también su especialidad, y de los enfermeros la planta en la que trabajan.
# Al hospital acuden pacientes. De todos ellos se guarda un historial con su dni, nombre, dirección,
# teléfono, y un conjunto de pruebas y consultas que hayan hecho en el hospital. De cada prueba o
# consulta guardamos la fecha en que se hizo, y el médico que le atendió
# Define las clases necesarias para el enunciado propuesto en un programa llamado Hospital.py. Define
# un programa principal que cree un array de personal de hospital con varios médicos y enfermeros.
# Define un paciente con sus datos, y dale de alta diversas pruebas realizadas por varios médicos.
# Finalmente, trata de mostrar por pantalla los datos completos del paciente, incluyendo su historial de
# pruebas. 

from datetime import datetime

class PersonalHospital:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Medico(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad

class Enfermero(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta

class Paciente:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial = []

    def agregar_prueba(self, fecha, medico):
        self.historial.append({"fecha": fecha, "medico": medico})


# Crear personal del hospital
medico1 = Medico("12345678A", "Dr. Juan Perez", "Calle Hospital 1", "123456789", "Cardiología")
medico2 = Medico("87654321B", "Dra. Ana Rodriguez", "Calle Hospital 2", "987654321", "Neurología")

enfermero1 = Enfermero("98765432C", "Enfermero Maria", "Calle Hospital 3", "654321987", "Planta 3")

# Crear pacientes
paciente1 = Paciente("11111111X", "Paciente 1", "Calle Paciente 1", "111111111")
paciente2 = Paciente("22222222Y", "Paciente 2", "Calle Paciente 2", "222222222")

# Agregar pruebas al historial de los pacientes
fecha_prueba1 = datetime(2022, 1, 15)
fecha_prueba2 = datetime(2022, 2, 20)
fecha_prueba3 = datetime(2022, 3, 25)

paciente1.agregar_prueba(fecha_prueba1, medico1)
paciente1.agregar_prueba(fecha_prueba2, medico2)

paciente2.agregar_prueba(fecha_prueba3, medico2)

# Mostrar información de los pacientes
print("Información del Paciente 1:")
print(f"DNI: {paciente1.dni}")
print(f"Nombre: {paciente1.nombre}")
print(f"Dirección: {paciente1.direccion}")
print(f"Teléfono: {paciente1.telefono}")

print("\nHistorial de pruebas del Paciente 1:")
for prueba in paciente1.historial:
    fecha_str = prueba["fecha"].strftime("%Y-%m-%d")
    print(f"Fecha: {fecha_str}, Médico: {prueba['medico'].nombre}, Especialidad: {prueba['medico'].especialidad}")

print("\nInformación del Paciente 2:")
print(f"DNI: {paciente2.dni}")
print(f"Nombre: {paciente2.nombre}")
print(f"Dirección: {paciente2.direccion}")
print(f"Teléfono: {paciente2.telefono}")

print("\nHistorial de pruebas del Paciente 2:")
for prueba in paciente2.historial:
    fecha_str = prueba["fecha"].strftime("%Y-%m-%d")
    print(f"Fecha: {fecha_str}, Médico: {prueba['medico'].nombre}, Especialidad: {prueba['medico'].especialidad}")

