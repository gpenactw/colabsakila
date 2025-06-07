class CustomerMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("\n1. Listar clientes\n2. Crear clientes\n3. Actualizar clientes\n4. Eliminar clientes\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_customers()
            elif choice == "2":
                self.controller.create_customer()
            elif choice == "3":
                self.controller.update_customer()
            elif choice == "4":
                self.controller.delete_customer()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
