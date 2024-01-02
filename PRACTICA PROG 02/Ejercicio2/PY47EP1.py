# Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
# Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. 
# Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
# En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.


class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def depositar(self, monto):
        self.monto += monto
        print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.monto}")

    def retirar(self, monto):
        if monto <= self.monto:
            self.monto -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.monto}")
        else:
            print("Saldo insuficiente.")

class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def generar_intereses(self):
        print("La caja de ahorro no genera intereses.")

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa_interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasa_interes = tasa_interes

    def calcular_intereses(self):
        intereses = (self.monto * self.tasa_interes * self.plazo) / 36500
        print(f"Intereses generados por plazo fijo: ${intereses}")

# Bloque principal
caja_ahorro = CajaAhorro("Juan Perez", 5000)
plazo_fijo = PlazoFijo("Maria Rodriguez", 10000, 30, 0.05)

caja_ahorro.depositar(2000)
caja_ahorro.retirar(1000)
caja_ahorro.generar_intereses()

plazo_fijo.depositar(5000)
plazo_fijo.retirar(2000)
plazo_fijo.calcular_intereses()
