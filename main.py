from dbcontext import DbContext
from controllers.ActorController import ActorController
from controllers.InventoryController import InventoryController
from models.ActorModel import ActorModel
from models.InventoryModel import InventoryModel
from views.ActorMenu import ActorMenu
from views.InventoryMenu import InventoryMenu


def main():
    db = DbContext()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN SAKILA ===")
        print("1. Gestionar Actores")
        print("2. Gestionar Inventario")
        print("3. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            model = ActorModel(db)
            controller = ActorController(model)
            menu = ActorMenu(controller, db)
            menu.display()
        elif choice == "2":
            model = InventoryModel(db)
            controller = InventoryController(model)
            menu = InventoryMenu(controller, db)
            menu.display()
        elif choice == "3":
            db.close()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
