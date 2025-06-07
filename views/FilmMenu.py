class FilmMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar películas\n2. Crear películas\n3. Actualizar películas\n4. Eliminar películas\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_films()
            elif choice == "2":
                self.controller.create_film()
            elif choice == "3":
                self.controller.update_film()
            elif choice == "4":
                self.controller.delete_film()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")
