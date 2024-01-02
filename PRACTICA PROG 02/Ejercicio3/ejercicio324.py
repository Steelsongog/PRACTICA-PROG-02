# Confeccionar una función de orden superior que reciba un String y una función con un parámetro de tipo String que retorna un Boolean.
# La función debe analizar cada elemento del String llamando a la función que recibe como parámetro, si retorna un True se agrega dicho caracter al String que se retornará.

# En el bloque principal definir un String con una cadena cualquiera.

# Llamar a la función de orden superior y pasar expresiones lambdas para filtrar y generar otro String con las siguientes restricciones:

# Un String solo con las vocales
# Un String solo con los caracteres en minúsculas
# Un String con todos los caracteres no alfabéticos

def filtrar_string(input_string, condicion):
    resultado = ''.join(caracter for caracter in input_string if condicion(caracter))
    return resultado

# Bloque principal
cadena = "Hola Mundo 123!"
print("Cadena original:", cadena)

# Filtrar solo las vocales
vocales = filtrar_string(cadena, lambda x: x.lower() in 'aeiou')
print("Vocales:", vocales)

# Filtrar solo los caracteres en minúsculas
minusculas = filtrar_string(cadena, lambda x: x.islower())
print("Minúsculas:", minusculas)

# Filtrar todos los caracteres no alfabéticos
no_alfabeticos = filtrar_string(cadena, lambda x: not x.isalpha())
print("No alfabéticos:", no_alfabeticos)
