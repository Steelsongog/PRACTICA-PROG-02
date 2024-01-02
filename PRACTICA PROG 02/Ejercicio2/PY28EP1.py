# Confeccionar una función que reciba entre 2 y 5 enteros. 
# La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.

def suma_entre_2_y_5(a, b, c=0, d=0, e=0):
    # Retornar la suma de los valores
    return a + b + c + d + e

# Ejemplos de uso
resultado1 = suma_entre_2_y_5(1, 2)
resultado2 = suma_entre_2_y_5(1, 2, 3)
resultado3 = suma_entre_2_y_5(1, 2, 3, 4)
resultado4 = suma_entre_2_y_5(1, 2, 3, 4, 5)

# Mostrar los resultados
print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")
print(f"Resultado 4: {resultado4}")
