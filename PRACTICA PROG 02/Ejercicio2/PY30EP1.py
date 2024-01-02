# Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def contar_mayores_de_edad(*edades):
    mayores_de_edad = [edad for edad in edades if edad >= 18]
    cantidad_mayores = len(mayores_de_edad)
    return cantidad_mayores

# Ejemplo de uso
cantidad_mayores_resultado = contar_mayores_de_edad(25, 16, 20, 30, 17, 18, 22)

# Mostrar el resultado
print(f"Cantidad de edades mayores o iguales a 18: {cantidad_mayores_resultado}")
