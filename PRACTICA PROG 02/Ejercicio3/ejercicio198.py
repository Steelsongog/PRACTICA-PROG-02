# Plantear un programa que permita jugar a los dados. Las reglas de juego son:
# se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

# Lo primero que hacemos es identificar las clases:

# Podemos identificar la clase Dado y la clase JuegoDeDados.

# Luego los atributos y los métodos de cada clase:

# Dado		
#     atributos
#         valor
#     métodos
#         tirar
#         imprimir
#         retornar_valor

# JuegoDeDados
#     atributos
#         3 Dado (3 objetos de la clase Dado)
#     métodos
#         __init__
#         jugar

import random

class Dado:
    def __init__(self):
        self.valor = 0

    def tirar(self):
        self.valor = random.randint(1, 6)

    def imprimir(self):
        print(f"Dado: {self.valor}")

    def retornar_valor(self):
        return self.valor

class JuegoDeDados:
    def __init__(self):
        self.dados = [Dado() for _ in range(3)]

    def jugar(self):
        for dado in self.dados:
            dado.tirar()
            dado.imprimir()

        valores = [dado.retornar_valor() for dado in self.dados]

        if all(valor == valores[0] for valor in valores):
            print("¡Ganó!")
        else:
            print("Perdió")

# Programa principal
juego = JuegoDeDados()
juego.jugar()
