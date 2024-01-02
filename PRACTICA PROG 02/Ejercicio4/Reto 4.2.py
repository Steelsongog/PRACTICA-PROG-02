# Un año es bisiesto si cumple los siguientes criterios:

# Es divisible entre 4.

# Si termina en 00, se comprueba si es divisible entre 400 (2000 y 2400 son bisiestos. 2100, 2200 y 2300 no lo son).

# Más información sobre años bisiestos en https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto

# Escribe una función que reciba un año y devuelva 1 si es bisiesto, 0 en caso contrario. La función no debe leer nada de la entrada estándar ni mandar ningún dato por la salida estándar.

# La función debe definirse con este estilo:

# def esBisiesto(anyo):

def esBisiesto(anyo):
    if anyo % 4 == 0:
        if anyo % 100 == 0:
            return 1 if anyo % 400 == 0 else 0
        else:
            return 1
    else:
        return 0


