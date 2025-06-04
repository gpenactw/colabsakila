from dbcontext import DbContext
from models import *
from controllers import *

def main():
    db = DbContext()
    model = ActorModel(db)
    controller = ActorController(model)

    while True:
        print("\n1. Listar actores\n2. Crear actor\n3. Actualizar actor\n4. Eliminar actor\n5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            controller.list_actors()
        elif choice == "2":
            controller.create_actor()
        elif choice == "3":
            controller.update_actor()
        elif choice == "4":
            controller.delete_actor()
        elif choice == "5":
            db.close()
            print("Ha salido del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
