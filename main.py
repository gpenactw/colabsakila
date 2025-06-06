from dbcontext import DbContext
from controllers.ActorController import ActorController
from models.ActorModel import ActorModel
from views.ActorMenu import ActorMenu


def main():
    db = DbContext()
    model = ActorModel(db)
    controller = ActorController(model)
    
    menu = ActorMenu(controller, db)
    menu.display()

if __name__ == "__main__":
    main()
