# Ejercicio 2: Escribe una nueva versión del ejercicio anterior en un programa llamado Equipos.py donde,
# además de la clase Jugador haya una segunda clase llamada Equipo , cuyo único atributo será el
# nombre del equipo (texto), junto con un constructor para darle valor . Haz que cada jugador pueda
# pertenecer a un equipo añadiendo un atributo Equipo a la clase Jugador. En el programa principal, crea
# un jugador y un equipo, y asigna el equipo al jugador. Muestra por pantalla la información del jugador,
# incluyendo el equipo. 

class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None  # Inicialmente, el jugador no pertenece a ningún equipo

    def mostrar_informacion(self):
        if self.equipo:
            print(f"{self.dorsal}. {self.nombre} - Equipo: {self.equipo.nombre}")
        else:
            print(f"{self.dorsal}. {self.nombre} - Sin equipo")

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear instancias de las clases Jugador y Equipo
equipo1 = Equipo("Equipo A")
jugador1 = Jugador(16, "Pau Gasol")

# Asignar el equipo al jugador
jugador1.equipo = equipo1

# Mostrar la información del jugador, incluyendo el equipo
jugador1.mostrar_informacion()
