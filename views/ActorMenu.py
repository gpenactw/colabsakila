class ActorMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n1. Listar actores\n2. Crear actor\n3. Actualizar actor\n4. Eliminar actor\n5. Salir")
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_actors()
            elif choice == "2":
                self.controller.create_actor()
            elif choice == "3":
                self.controller.update_actor()
            elif choice == "4":
                self.controller.delete_actor()
            elif choice == "5":
                self.db.close()
                print("Ha salido del programa.")
                break
            else:
                print("Opción inválida.")