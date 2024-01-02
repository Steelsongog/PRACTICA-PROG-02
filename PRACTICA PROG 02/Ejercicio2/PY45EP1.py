# Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa

class AgendaPersonal:
    def __init__(self):
        self.contactos = []

    def cargar_contacto(self):
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el teléfono de la persona: ")
        mail = input("Ingrese el mail de la persona: ")
        self.contactos.append({"Nombre": nombre, "Teléfono": telefono, "Mail": mail})
        print("Contacto cargado exitosamente.")

    def listar_agenda(self):
        print("Listado completo de la agenda:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}, Mail: {contacto['Mail']}")

    def consultar_contacto(self):
        nombre_consulta = input("Ingrese el nombre de la persona a consultar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre_consulta:
                print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}, Mail: {contacto['Mail']}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el contacto con nombre {nombre_consulta}")

    def modificar_contacto(self):
        nombre_modificar = input("Ingrese el nombre de la persona a modificar: ")
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre_modificar:
                contacto['Teléfono'] = input("Ingrese el nuevo teléfono: ")
                contacto['Mail'] = input("Ingrese el nuevo mail: ")
                print("Contacto modificado exitosamente.")
                break
        else:
            print(f"No se encontró el contacto con nombre {nombre_modificar}")

    def ejecutar_menu(self):
        while True:
            print("\nMenú de la Agenda Personal:")
            print("1- Carga de un contacto en la agenda.")
            print("2- Listado completo de la agenda.")
            print("3- Consulta ingresando el nombre de la persona.")
            print("4- Modificación de su teléfono y mail.")
            print("5- Finalizar programa.")
            
            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                self.cargar_contacto()
            elif opcion == "2":
                self.listar_agenda()
            elif opcion == "3":
                self.consultar_contacto()
            elif opcion == "4":
                self.modificar_contacto()
            elif opcion == "5":
                print("Programa finalizado.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

# Programa principal
agenda = AgendaPersonal()
agenda.ejecutar_menu()
