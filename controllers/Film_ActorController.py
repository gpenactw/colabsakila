class Film_ActorController:

    def __init__(self, model):
        self.model = model

    def list_film_actor(self):
        films_actor = self.model.get_all()
        print("\n--- Lista de Películas por Actor ---")
        for film_actor in films_actor:
            print(f"ID del Actor: {film_actor.actor_id}, ID Película: {film_actor.film_id}, Última actualización: {film_actor.last_update}")

def create_film_actor(self):
    try:
        actor_id = int(input("ID del Actor: "))
        film_id = int(input("ID de la Película: "))
    except ValueError:
        print("Error: Los ID deben ser números enteros.")
        return

    # Verifica existencia del actor y película
    if not self.model.actor_exists(actor_id):
        print(f"No existe un actor con ID {actor_id}.")
        return

    if not self.model.film_id_exists(film_id):
        print(f"No existe una película con ID {film_id}.")
        return

    # Verifica si ya existe la relación
    if self.model.film_actor_exists(actor_id, film_id):
        print("La relación entre este actor y película ya existe.")
        return

    from datetime import datetime
    last_update = datetime.now()

    try:
        self.model.create_film_actor(actor_id, film_id, last_update)
        print("Relación Actor-Película creada exitosamente.")
    except Exception as err:
        if hasattr(err, 'errno') and err.errno == 1452:
            print("Error: Actor o película no existen (clave foránea inválida).")
        elif hasattr(err, 'errno') and err.errno == 1062:
            print("Error: Relación duplicada (ya existe en la base de datos).")
        else:
            print(f"Error inesperado al crear relación Actor-Película: {err}")

def update_film_actor(self):
    try:
        actor_id = int(input("ID del Actor de la relación: "))
        film_id = int(input("ID de la Película de la relación: "))
    except ValueError:
        print("Error: Los ID deben ser números enteros.")
        return

    if not self.model.film_actor_exists(actor_id, film_id):
        print(f"No existe una relación entre el Actor {actor_id} y la Película {film_id}.")
        return

    from datetime import datetime
    last_update = datetime.now()

    try:
        self.model.update_film_actor(actor_id, film_id, last_update)
        print("Se actualizó el campo 'last_update' de la relación Actor-Película.")
    except Exception as err:
        print(f"Error inesperado al actualizar relación Actor-Película: {err}")

def delete_film_actor(self):
    try:
        actor_id = int(input("ID del Actor de la relación: "))
        film_id = int(input("ID de la Película de la relación: "))
    except ValueError:
        print("Error: Los ID deben ser números enteros.")
        return

    if not self.model.film_actor_exists(actor_id, film_id):
        print(f"No existe una relación entre el Actor {actor_id} y la Película {film_id}.")
        return

    confirm = input(f"¿Estás seguro de que deseas eliminar la relación entre el Actor {actor_id} y la Película {film_id}? (s/n): ").lower()
    if confirm != 's':
        print("Eliminación cancelada.")
        return

    try:
        self.model.delete_film_actor(actor_id, film_id)
        print("Relación Actor-Película eliminada exitosamente.")
    except Exception as err:
        print(f"Error inesperado al eliminar relación Actor-Película: {err}")
