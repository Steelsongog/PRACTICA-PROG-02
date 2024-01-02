# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def encontrar_menor(valor1, valor2, valor3):
    # Encontrar el menor de los tres valores
    return min(valor1, valor2, valor3)

# Solicitar la carga de tres valores y mostrar el menor
valor1 = float(input("Introduce el primer valor: "))
valor2 = float(input("Introduce el segundo valor: "))
valor3 = float(input("Introduce el tercer valor: "))

menor = encontrar_menor(valor1, valor2, valor3)
print(f"El menor de los tres valores es: {menor}")

# Llamar a la función nuevamente
valor4 = float(input("Introduce un cuarto valor: "))
valor5 = float(input("Introduce un quinto valor: "))
valor6 = float(input("Introduce un sexto valor: "))

menor_nueva_llamada = encontrar_menor(valor4, valor5, valor6)
print(f"El menor de los nuevos tres valores es: {menor_nueva_llamada}")
