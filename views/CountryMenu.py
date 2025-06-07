# Country Menu

class CountryMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("\n1. Listar países\n2. Crear país\n3. Actualizar país\n4. Eliminar país\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_countries()
            elif choice == "2":
                self.controller.create_country()
            elif choice == "3":
                self.controller.update_country()
            elif choice == "4":
                self.controller.delete_country()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
