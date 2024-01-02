# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
# def retornar_superficie(lado1,lado2):

def retornar_superficie(lado1, lado2):
    # Calcular la superficie del rectángulo
    superficie = lado1 * lado2
    return superficie

# Ejemplo de uso
lado1 = float(input("Ingrese el valor del primer lado del rectángulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del rectángulo: "))

superficie_rectangulo = retornar_superficie(lado1, lado2)
print(f"La superficie del rectángulo con lados {lado1} y {lado2} es: {superficie_rectangulo}")
