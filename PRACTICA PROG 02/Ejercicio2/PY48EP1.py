class Jugador:
    tiempo_restante = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print(f"Jugador: {self.nombre}, Puntaje: {self.puntaje}, Tiempo Restante: {Jugador.tiempo_restante} minutos")

    @classmethod
    def pasar_tiempo(cls):
        cls.tiempo_restante -= 1

# Bloque principal
jugador1 = Jugador("Juan", 0)
jugador2 = Jugador("Maria", 0)

while Jugador.tiempo_restante > 0:
    jugador1.imprimir()
    jugador2.imprimir()
    Jugador.pasar_tiempo()

print("Fin del juego.")
