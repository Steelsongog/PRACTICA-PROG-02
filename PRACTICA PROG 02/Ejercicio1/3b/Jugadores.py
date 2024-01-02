# Ejercicio 1:
# Escribe un programa en Python llamado Jugadores.py que defina una clase llamada Jugador , con
# atributos dorsal (numérico) y nombre (texto). Define el constructor para darles valor y un método que
# muestre la información de un jugador con el formato dorsal. Nombre. . Por ejemplo:
# 16. Pau Gasol . En el programa principal, crea un par de jugadores con sus datos, y muestra su
# información por pantalla.

class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"{self.dorsal}. {self.nombre}")

# Crear instancias de la clase Jugador
jugador1 = Jugador(16, "Pau Gasol")
jugador2 = Jugador(10, "LeBron James")

# Mostrar la información de los jugadores por pantalla
print("Información del Jugador 1:")
jugador1.mostrar_informacion()

print("\nInformación del Jugador 2:")
jugador2.mostrar_informacion()
