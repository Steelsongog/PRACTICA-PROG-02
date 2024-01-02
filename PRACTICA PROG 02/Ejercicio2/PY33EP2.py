# Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
# Desarrollar las funciones:
# 1) Cargar por teclado.
# 2) Listar los productos y precios.
# 3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar_productos():
    productos = []
    for _ in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos.append((nombre, precio))
    return productos

def listar_productos(productos):
    print("Lista de productos y precios:")
    for nombre, precio in productos:
        print(f"{nombre}: ${precio}")

def imprimir_precios_entre_10_y_15(productos):
    print("Productos con precios entre 10 y 15:")
    for nombre, precio in productos:
        if 10 <= precio <= 15:
            print(f"{nombre}: ${precio}")

# Programa principal
productos = cargar_productos()
listar_productos(productos)
imprimir_precios_entre_10_y_15(productos)
