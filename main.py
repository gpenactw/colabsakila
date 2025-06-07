from dbcontext import DbContext
from controllers.ActorController import ActorController
from controllers.InventoryController import InventoryController
from controllers.LanguageController import LanguageController
from controllers.PaymentController import PaymentController
from controllers.RentalController import RentalController
from controllers.StaffController import StaffController
from controllers.StoreController import StoreController
from models.ActorModel import ActorModel
from models.InventoryModel import InventoryModel
from models.LanguageModel import LanguageModel
from models.PaymentModel import PaymentModel
from models.RentalModel import RentalModel
from models.StaffModel import StaffModel
from models.StoreModel import StoreModel
from views.ActorMenu import ActorMenu
from views.InventoryMenu import InventoryMenu
from views.LanguageMenu import LanguageMenu
from views.PaymentMenu import PaymentMenu
from views.RentalMenu import RentalMenu
from views.StaffMenu import StaffMenu
from views.StoreMenu import StoreMenu


def main():
    db = DbContext()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN SAKILA ===")
        print("1. Gestionar Actores")
        print("2. Gestionar Inventario")
        print("3. Gestionar Idiomas")
        print("4. Gestionar Pagos")
        print("5. Gestionar Alquileres")
        print("6. Gestionar Personal")
        print("7. Gestionar Tiendas")
        print("8. Salir")
        
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
            model = LanguageModel(db)
            controller = LanguageController(model)
            menu = LanguageMenu(controller, db)
            menu.display()
        elif choice == "4":
            model = PaymentModel(db)
            controller = PaymentController(model)
            menu = PaymentMenu(controller, db)
            menu.display()
        elif choice == "5":
            model = RentalModel(db)
            controller = RentalController(model)
            menu = RentalMenu(controller, db)
            menu.display()
        elif choice == "6":
            model = StaffModel(db)
            controller = StaffController(model)
            menu = StaffMenu(controller, db)
            menu.display()
        elif choice == "7":
            model = StoreModel(db)
            controller = StoreController(model)
            menu = StoreMenu(controller, db)
            menu.display()
        elif choice == "8":
            db.close()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
