class FilmTextController:
    def __init__(self, model):
        self.model = model

    def list_film_text(self):
        film_texts = self.model.get_all()
        if not film_texts:
            print("No hay textos de películas registrados.")
            return
        print("\n--- Lista de Películas con Texto ---")
        for film_text in film_texts:
            print(f"ID Película: {film_text.film_id}, Título: {film_text.title}, Descripción: {film_text.description}")

    def create_film_text(self):
        try:
            film_id = int(input("ID de la Película: "))
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return

        if not self.model.film_id_exists(film_id):
            print(f"No existe una película con ID {film_id}.")
            return

        title = input("Título: ")
        description = input("Descripción: ")

        if self.model.film_text_exists(film_id):
            print("Ya existe un texto para esta película.")
            return

        try:
            self.model.add(film_id, title, description)
            print("Texto de la película creado exitosamente.")
        except Exception as err:
            print(f"Error inesperado al crear texto de la película: {err}")

    def update_film_text(self):
        try:
            film_id = int(input("ID de la Película a actualizar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return

        if not self.model.film_text_exists(film_id):
            print(f"No existe texto registrado para la película con ID {film_id}.")
            return

        title = input("Nuevo título: ")
        description = input("Nueva descripción: ")

        try:
            self.model.update(film_id, title, description)
            print("Texto de la película actualizado exitosamente.")
        except Exception as err:
            print(f"Error inesperado al actualizar texto de la película: {err}")

    def delete_film_text(self):
        try:
            film_id = int(input("ID de la Película a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return

        if not self.model.film_text_exists(film_id):
            print(f"No existe texto registrado para la película con ID {film_id}.")
            return

        confirm = input(
            f"¿Estás seguro de que deseas eliminar el texto de la película con ID {film_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(film_id)
            print("Texto de la película eliminado exitosamente.")
        except Exception as err:
            print(f"Error inesperado al eliminar texto de la película: {err}")
