# Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa

class AdministradorAlumnos:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def cargar_alumnos(self):
        for _ in range(5):
            nombre = input("Ingrese el nombre del alumno: ")
            nota = float(input("Ingrese la nota del alumno: "))
            self.nombres.append(nombre)
            self.notas.append(nota)

    def listar_alumnos(self):
        print("Lista de Alumnos:")
        for i in range(5):
            print(f"{self.nombres[i]} - Nota: {self.notas[i]}")

    def mostrar_notas_mayores_a_siete(self):
        print("Alumnos con notas mayores o iguales a 7:")
        for i in range(5):
            if self.notas[i] >= 7:
                print(f"{self.nombres[i]} - Nota: {self.notas[i]}")

# Programa principal
administrador = AdministradorAlumnos()

while True:
    print("\nMenú de opciones:")
    print("1- Cargar alumnos.")
    print("2- Listar alumnos.")
    print("3- Mostrar alumnos con notas mayores o iguales a 7.")
    print("4- Finalizar programa.")

    opcion = input("Ingrese la opción deseada (1-4): ")

    if opcion == "1":
        administrador.cargar_alumnos()
    elif opcion == "2":
        administrador.listar_alumnos()
    elif opcion == "3":
        administrador.mostrar_notas_mayores_a_siete()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
