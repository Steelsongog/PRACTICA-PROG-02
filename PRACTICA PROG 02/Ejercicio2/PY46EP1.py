# Plantear una clase Club y otra clase Socio.
# La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
# En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
# La clase Club debe tener como atributos 3 objetos de la clase Socio.
# Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.

class Socio:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del socio: ")
        self.antiguedad = int(input("Ingrese la antigüedad del socio en años: "))

class Club:
    def __init__(self):
        self.socios = [Socio() for _ in range(3)]

    def imprimir_socio_mayor_antiguedad(self):
        socio_mayor_antiguedad = max(self.socios, key=lambda socio: socio.antiguedad)
        print(f"El socio con mayor antigüedad en el club es: {socio_mayor_antiguedad.nombre}")

# Programa principal
club = Club()
club.imprimir_socio_mayor_antiguedad()
