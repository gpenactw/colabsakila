class RentalMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n=== MENÚ DE ALQUILERES ===")
            print("1. Listar todos los alquileres")
            print("2. Registrar nuevo alquiler")
            print("3. Actualizar alquiler")
            print("4. Eliminar alquiler")
            print("5. Ver alquileres activos (no devueltos)")
            print("6. Registrar devolución")
            print("7. Volver al menú principal")
            
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_rentals()
            elif choice == "2":
                self.controller.create_rental()
            elif choice == "3":
                self.controller.update_rental()
            elif choice == "4":
                self.controller.delete_rental()
            elif choice == "5":
                self.controller.show_active_rentals()
            elif choice == "6":
                self.controller.return_rental()
            elif choice == "7":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")