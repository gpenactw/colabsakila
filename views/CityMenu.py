# CityMenu

class CityMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("\n1. Listar ciudades\n2. Crear ciudad\n3. Actualizar ciudad\n4. Eliminar ciudad\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_cities()
            elif choice == "2":
                self.controller.create_city()
            elif choice == "3":
                self.controller.update_city()
            elif choice == "4":
                self.controller.delete_city()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
