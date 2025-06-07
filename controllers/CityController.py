class CityController:
    def __init__(self, model):
        self.model = model

    def list_cities(self):
        cities = self.model.get_all()
        print("\n--- Lista de Ciudades ---")
        for c in cities:
            print(f"{c.city_id}: {c.city} (País ID: {c.country_id})")

    def create_city(self):
        city = input("Nombre de la ciudad: ")
        country_id = int(input("ID del país: "))
        self.model.add(city, country_id)
        print("Ciudad creada.")

    def update_city(self):
        city_id = int(input("ID de ciudad a actualizar: "))
        city = input("Nuevo nombre de ciudad: ")
        country_id = int(input("Nuevo ID de país: "))
        self.model.update(city_id, city, country_id)
        print("Ciudad actualizada.")

    def delete_city(self):
        city_id = int(input("ID de ciudad a eliminar: "))
        self.model.delete(city_id)
        print("Ciudad eliminada.")
