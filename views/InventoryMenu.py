class InventoryMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar inventario\n2. Crear item de inventario\n3. Actualizar inventario\n4. Eliminar inventario\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_inventory()
            elif choice == "2":
                self.controller.create_inventory()
            elif choice == "3":
                self.controller.update_inventory()
            elif choice == "4":
                self.controller.delete_inventory()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")