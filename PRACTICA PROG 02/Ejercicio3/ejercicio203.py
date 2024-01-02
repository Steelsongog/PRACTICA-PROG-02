# Definir una clase Cliente que almacene un código de cliente y un nombre.
# En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas corrientes.
# Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.

class Cliente:
    cuentas_suspendidas = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.suspendido = False

    def suspender_cuenta(self):
        self.suspendido = True
        if self not in Cliente.cuentas_suspendidas:
            Cliente.cuentas_suspendidas.append(self)

    def imprimir_estado(self):
        estado = "Suspendido" if self.suspendido else "Activo"
        print(f"Código: {self.codigo}, Nombre: {self.nombre}, Estado de cuenta: {estado}")


# Crear instancias de la clase Cliente
cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "María")
cliente3 = Cliente(3, "Pedro")

# Suspender cuentas de algunos clientes
cliente1.suspender_cuenta()
cliente3.suspender_cuenta()

# Imprimir estado de todos los clientes
for cliente in [cliente1, cliente2, cliente3]:
    cliente.imprimir_estado()

# Imprimir clientes con cuentas suspendidas
print("\nClientes con cuentas suspendidas:")
for cliente_suspendido in Cliente.cuentas_suspendidas:
    print(f"Código: {cliente_suspendido.codigo}, Nombre: {cliente_suspendido.nombre}")
