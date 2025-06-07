class Film_CategoryController:
    def __init__(self, model):
        self.model = model

    def list_film_category(self):
        film_categories = self.model.get_all()
        print("\n--- Lista de Películas por Categoría ---")
        for film_category in film_categories:
            print(f"ID Película: {film_category.film_id}, ID Categoría: {film_category.category_id}, Última actualización: {film_category.last_update}")

    def create_film_category(self):
        try:
            film_id = int(input("ID de la Película: "))
            category_id = int(input("ID de la Categoría: "))
        except ValueError:
            print("Error: Los ID deben ser números enteros.")
            return

        # Verifica existencia de película y categoría
        if not self.model.film_id_exists(film_id):
            print(f"No existe una película con ID {film_id}.")
            return

        if not self.model.category_exists(category_id):
            print(f"No existe una categoría con ID {category_id}.")
            return

        # Verifica si ya existe la relación
        if self.model.film_category_exists(film_id, category_id):
            print("La relación entre esta película y categoría ya existe.")
            return

        from datetime import datetime
        last_update = datetime.now()

        try:
            self.model.create_film_category(film_id, category_id, last_update)
            print("Relación Película-Categoría creada exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1452:
                print("Error: Película o categoría no existen (clave foránea inválida).")
            elif hasattr(err, 'errno') and err.errno == 1062:
                print("Error: Relación duplicada (ya existe en la base de datos).")
            else:
                print(f"Error inesperado al crear relación Película-Categoría: {err}")

    def update_film_category(self):
        try:
            film_id = int(input("ID de la Película de la relación: "))
            category_id = int(input("ID de la Categoría de la relación: "))
        except ValueError:
            print("Error: Los ID deben ser números enteros.")
            return

        if not self.model.film_category_exists(film_id, category_id):
            print(f"No existe una relación entre la Película {film_id} y la Categoría {category_id}.")
            return
        from datetime import datetime
        last_update = datetime.now()

        try:
            self.model.update_film_category(film_id, category_id, last_update)
            print("Se actualizó el campo 'last_update' de la relación Película-Categoría.")
        except Exception as err:
            print(f"Error inesperado al actualizar relación Película-Categoría: {err}")

    def delete_film_category(self):
        try:
            film_id = int(input("ID de la Película de la relación: "))
            category_id = int(input("ID de la Categoría de la relación: "))
        except ValueError:
            print("Error: Los ID deben ser números enteros.")
            return

        if not self.model.film_category_exists(film_id, category_id):
            print(f"No existe una relación entre la Película {film_id} y la Categoría {category_id}.")
            return

        confirm = input(f"¿Estás seguro de que deseas eliminar la relación entre la Película {film_id} y la Categoría {category_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete_film_category(film_id, category_id)
            print("Relación Película-Categoría eliminada exitosamente.")
        except Exception as err:
            print(f"Error inesperado al eliminar relación Película-Categoría: {err}")