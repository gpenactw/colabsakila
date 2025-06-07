from controllers.CityController import CityController
from controllers.CountryController import CountryController
from dbcontext import DbContext
from controllers.AddressController import AddressController
from controllers.CategoryController import CategoryController
from controllers.ActorController import ActorController
from controllers.CustomerController import CustomerController
from controllers.FilmController import FilmController
from controllers.FilmActorController import FilmActorController
from controllers.FilmCategoryController import FilmCategoryController
from controllers.FilmTextController import FilmTextController
from controllers.InventoryController import InventoryController
from controllers.LanguageController import LanguageController
from controllers.PaymentController import PaymentController
from controllers.RentalController import RentalController
from controllers.StaffController import StaffController
from controllers.StoreController import StoreController
from models.ActorModel import ActorModel
from models.AddressModel import AddressModel
from models.CategoryModel import CategoryModel
from models.CityModel import CityModel
from models.CountryModel import CountryModel
from models.CustomerModel import CustomerModel
from models.FilmModel import FilmModel
from models.FilmActorModel import FilmActorModel
from models.FilmCategoryModel import FilmCategoryModel
from models.FilmTextModel import FilmTextModel
from models.InventoryModel import InventoryModel
from models.LanguageModel import LanguageModel
from models.PaymentModel import PaymentModel
from models.RentalModel import RentalModel
from models.StaffModel import StaffModel
from models.StoreModel import StoreModel
from views.ActorMenu import ActorMenu
from views.AddressMenu import AddressMenu
from views.CategoryMenu import CategoryMenu
from views.CityMenu import CityMenu
from views.CountryMenu import CountryMenu
from views.CustomerMenu import CustomerMenu
from views.FilmMenu import FilmMenu
from views.FilmActorMenu import Film_ActorMenu
from views.FilmCategoryMenu import Film_CategoryMenu
from views.FilmTextMenu import Film_TextMenu
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
        print("2. Gestionar Direcciones")
        print("3. Gestionar Categorias")
        print("4. Gestionar Ciudad")
        print("5. Gestionar País")
        print("6. Gestionar Clientes")
        print("7. Gestionar Películas")
        print("8. Gestionar Actores de Películas")
        print("9. Gestionar Categoría de Películas")
        print("10. Gestionar Descripción de Películas")
        print("11. Gestionar Inventario")
        print("12. Gestionar Idiomas")
        print("13. Gestionar Pagos")
        print("14. Gestionar Alquileres")
        print("15. Gestionar Personal")
        print("16. Gestionar Tiendas")
        print("17. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            model = ActorModel(db)
            controller = ActorController(model)
            menu = ActorMenu(controller, db)
            menu.display()
        elif choice == "2":
            model = AddressModel(db)
            controller = AddressController(model)
            menu = AddressMenu(controller)
            menu.display()
        elif choice == "3":
            model = CategoryModel(db)
            controller = CategoryController(model)
            menu = CategoryMenu(controller)
            menu.display()
        elif choice == "4":
            model = CityModel(db)
            controller = CityController(model)
            menu = CityMenu(controller)
            menu.display()
        elif choice == "5":
            model = CountryModel(db)
            controller = CountryController(model)
            menu = CountryMenu(controller)
            menu.display()
        elif choice == "6":
            model = CustomerModel(db)
            controller = CustomerController(model)
            menu = CustomerMenu(controller)
            menu.display()
        elif choice == "7":
            model = FilmModel(db)
            controller = FilmController(model)
            menu = FilmMenu(controller)
            menu.display()
        elif choice == "8":
            model = FilmActorModel(db)
            controller = FilmActorController(model)
            menu = Film_ActorMenu(controller, db)
            menu.display()
        elif choice == "9":
            model = FilmCategoryModel(db)
            controller = FilmCategoryController(model)
            menu = Film_CategoryMenu(controller, db)
            menu.display()
        elif choice == "10":
            model = FilmTextModel(db)
            controller = FilmTextController(model)
            menu = Film_TextMenu(controller, db)
            menu.display()
        elif choice == "11":
            model = InventoryModel(db)
            controller = InventoryController(model)
            menu = InventoryMenu(controller, db)
            menu.display()
        elif choice == "12":
            model = LanguageModel(db)
            controller = LanguageController(model)
            menu = LanguageMenu(controller, db)
            menu.display()
        elif choice == "13":
            model = PaymentModel(db)
            controller = PaymentController(model)
            menu = PaymentMenu(controller, db)
            menu.display()
        elif choice == "14":
            model = RentalModel(db)
            controller = RentalController(model)
            menu = RentalMenu(controller, db)
            menu.display()
        elif choice == "15":
            model = StaffModel(db)
            controller = StaffController(model)
            menu = StaffMenu(controller, db)
            menu.display()
        elif choice == "16":
            model = StoreModel(db)
            controller = StoreController(model)
            menu = StoreMenu(controller, db)
            menu.display()
        elif choice == "17":
            db.close()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
