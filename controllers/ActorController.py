class ActorController:
    def __init__(self, model):
        self.model = model

    def list_actors(self):
        actors = self.model.get_all()
        print("\n--- Lista de Actores ---")
        for actor in actors:
            print(f"{actor.actor_id}: {actor.first_name} {actor.last_name}")

    def create_actor(self):
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        self.model.add(first_name, last_name)
        print("Actor creado exitosamente.")

    def update_actor(self):
        actor_id = int(input("ID del actor a actualizar: "))
        first_name = input("Nuevo nombre: ")
        last_name = input("Nuevo apellido: ")
        self.model.update(actor_id, first_name, last_name)
        print("Actor actualizado.")

    def delete_actor(self):
        actor_id = int(input("ID del actor a eliminar: "))
        self.model.delete(actor_id)
        print("Actor eliminado.")