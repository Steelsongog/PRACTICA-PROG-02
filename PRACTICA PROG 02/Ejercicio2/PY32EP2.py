# Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
# En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
# Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
# candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
# 1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
# 2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

def cargar_candidatos():
    candidatos = []
    num_candidatos = int(input("Ingrese la cantidad de candidatos: "))

    for _ in range(num_candidatos):
        nombre = input("Ingrese el nombre del candidato: ")
        provincias_votos = []
        num_provincias = int(input("Ingrese la cantidad de provincias en las que recibió votos: "))

        for _ in range(num_provincias):
            provincia = input("Ingrese el nombre de la provincia: ")
            votos = int(input(f"Ingrese la cantidad de votos en {provincia}: "))
            provincias_votos.append((provincia, votos))

        candidatos.append((nombre, provincias_votos))

    return candidatos

def imprimir_total_votos(candidatos):
    for candidato in candidatos:
        nombre = candidato[0]
        total_votos = sum(votos for _, votos in candidato[1])
        print(f"{nombre} - Total de votos: {total_votos}")

# Programa principal
candidatos = cargar_candidatos()
imprimir_total_votos(candidatos)
