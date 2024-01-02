# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
# Definir dos objetos de la clase Alumno.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")

    def esta_regular(self):
        return self.nota >= 4

# Crear dos objetos de la clase Alumno
alumno1 = Alumno("Juan", 6)
alumno2 = Alumno("Maria", 3)

# Imprimir información de los alumnos
alumno1.imprimir_informacion()
alumno2.imprimir_informacion()

# Verificar si los alumnos están regulares
print(f"{alumno1.nombre} está regular: {alumno1.esta_regular()}")
