class CountryController:
    def __init__(self, model):
        self.model = model

    def list_countries(self):
        countries = self.model.get_all()
        print("\n--- Lista de Países ---")
        for c in countries:
            print(f"{c.country_id}: {c.country}")

    def create_country(self):
        country = input("Nombre del país: ")
        self.model.add(country)
        print("País creado.")

    def update_country(self):
        country_id = int(input("ID del país a actualizar: "))
        country = input("Nuevo nombre del país: ")
        self.model.update(country_id, country)
        print("País actualizado.")

    def delete_country(self):
        country_id = int(input("ID del país a eliminar: "))
        self.model.delete(country_id)
        print("País eliminado.")
