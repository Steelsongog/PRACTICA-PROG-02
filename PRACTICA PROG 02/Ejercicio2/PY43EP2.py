# Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
# El nombre de la clase llamarla Triangulo.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor del triángulo es: {lado_mayor}")

    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3

# Programa principal
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

triangulo.imprimir_lado_mayor()

if triangulo.es_equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")
