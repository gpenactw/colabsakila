class StoreMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n=== MENÚ DE TIENDAS ===")
            print("1. Listar todas las tiendas")
            print("2. Crear nueva tienda")
            print("3. Actualizar tienda")
            print("4. Eliminar tienda")
            print("5. Ver detalles de una tienda")
            print("6. Volver al menú principal")
            
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_stores()
            elif choice == "2":
                self.controller.create_store()
            elif choice == "3":
                self.controller.update_store()
            elif choice == "4":
                self.controller.delete_store()
            elif choice == "5":
                self.controller.show_store_details()
            elif choice == "6":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")