class AddressMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar direcciones\n2. Crear dirección\n3. Actualizar dirección\n4. Eliminar dirección\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_addresses
            elif choice == "2":
                self.controller.create_address()
            elif choice == "3":
                self.controller.update_address()
            elif choice == "4":
                self.controller.delete_address()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")