class ActorController:
    # --Actor
    
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
        
    #--Address
    
class AddressController:
    def __init__(self, model):
        self.model = model

    def list_addresses(self):
        addresses = self.model.get_all()
        print("\n--- Lista de Direcciones ---")
        for a in addresses:
            print(f"{a.address_id}: {a.address}, {a.district}")

    def create_address(self):
        address = input("Dirección: ")
        address2 = input("Dirección 2 (opcional): ")
        district = input("Distrito: ")
        city_id = int(input("ID de Ciudad: "))
        postal_code = input("Código Postal: ")
        phone = input("Teléfono: ")
        location = input("Ubicación (binaria o texto según DB): ")
        self.model.add(address, address2, district, city_id, postal_code, phone, location)
        print("Dirección creada exitosamente.")

    def update_address(self):
        address_id = int(input("ID de dirección a actualizar: "))
        address = input("Dirección: ")
        address2 = input("Dirección 2: ")
        district = input("Distrito: ")
        city_id = int(input("ID de Ciudad: "))
        postal_code = input("Código Postal: ")
        phone = input("Teléfono: ")
        location = input("Ubicación: ")
        self.model.update(address_id, address, address2, district, city_id, postal_code, phone, location)
        print("Dirección actualizada.")

    def delete_address(self):
        address_id = int(input("ID de dirección a eliminar: "))
        self.model.delete(address_id)
        print("Dirección eliminada.")

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

#--City

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

#--Country

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

#--Customer 
class CustomerController:
    def __init__(self, model):
        self.model = model

    def list_customers(self):
        customers = self.model.get_all()
        print("\n--- Lista de Clientes ---")
        for c in customers:
            print(f"{c.customer_id}: {c.first_name} {c.last_name} - Email: {c.email}")

    def create_customer(self):
        store_id = int(input("ID de la tienda: "))
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        email = input("Email: ")
        address_id = int(input("ID de dirección: "))
        active = int(input("Activo (1=Sí, 0=No): "))
        self.model.add(store_id, first_name, last_name, email, address_id, active)
        print("Cliente creado.")

    def update_customer(self):
        customer_id = int(input("ID del cliente a actualizar: "))
        store_id = int(input("ID de la tienda: "))
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        email = input("Email: ")
        address_id = int(input("ID de dirección: "))
        active = int(input("Activo (1=Sí, 0=No): "))
        self.model.update(customer_id, store_id, first_name, last_name, email, address_id, active)
        print("Cliente actualizado.")

    def delete_customer(self):
        customer_id = int(input("ID del cliente a eliminar: "))
        self.model.delete(customer_id)
        print("Cliente eliminado.")


       
