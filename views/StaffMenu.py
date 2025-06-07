class StaffMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n=== MENÚ DE PERSONAL ===")
            print("1. Listar todo el personal")
            print("2. Agregar nuevo personal")
            print("3. Actualizar personal")
            print("4. Eliminar personal")
            print("5. Ver personal activo")
            print("6. Volver al menú principal")
            
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_staff()
            elif choice == "2":
                self.controller.create_staff()
            elif choice == "3":
                self.controller.update_staff()
            elif choice == "4":
                self.controller.delete_staff()
            elif choice == "5":
                self.controller.show_active_staff()
            elif choice == "6":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")