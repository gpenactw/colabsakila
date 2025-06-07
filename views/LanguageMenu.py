class LanguageMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar idiomas\n2. Crear idioma\n3. Actualizar idioma\n4. Eliminar idioma\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_languages()
            elif choice == "2":
                self.controller.create_language()
            elif choice == "3":
                self.controller.update_language()
            elif choice == "4":
                self.controller.delete_language()
            elif choice == "5":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")