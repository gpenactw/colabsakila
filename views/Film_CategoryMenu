class Film_CategoryMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar categoría de películas\n2. Crear categoría de películas\n3. Actualizar categoría de películas\n4. Eliminar categoría de películas\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_film_category()
            elif choice == "2":
                self.controller.create_film_category()
            elif choice == "3":
                self.controller.update_film_category()
            elif choice == "4":
                self.controller.delete_film_category()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
