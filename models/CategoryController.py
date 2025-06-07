#--Category
class CategoryController:
    def __init__(self, model):
        self.model = model

    def list_categories(self):
        categories = self.model.get_all()
        print("\n--- Lista de Categorías ---")
        for c in categories:
            print(f"{c.category_id}: {c.name}")

    def create_category(self):
        name = input("Nombre de la categoría: ")
        self.model.add(name)
        print("Categoría creada.")

    def update_category(self):
        category_id = int(input("ID de categoría a actualizar: "))
        name = input("Nuevo nombre: ")
        self.model.update(category_id, name)
        print("Categoría actualizada.")

    def delete_category(self):
        category_id = int(input("ID de categoría a eliminar: "))
        self.model.delete(category_id)
        print("Categoría eliminada.")
