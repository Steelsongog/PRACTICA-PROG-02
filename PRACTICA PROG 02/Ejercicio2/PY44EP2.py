# Implementar la clase Operaciones. 
# Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor entero: "))
        self.valor2 = int(input("Ingrese el segundo valor entero: "))

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "No se puede dividir por cero"

    def imprimir_resultados(self):
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")

# Programa principal
operaciones = Operaciones()
operaciones.imprimir_resultados()
