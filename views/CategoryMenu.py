# Category Menu
class CategoryMenu:
    def __init__(self, controller):
        self.controller = controller

    def display(self):
        while True:
            print("\n1. Listar categorías\n2. Crear categoría\n3. Actualizar categoría\n4. Eliminar categoría\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_categories()
            elif choice == "2":
                self.controller.create_category()
            elif choice == "3":
                self.controller.update_category()
            elif choice == "4":
                self.controller.delete_category()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
