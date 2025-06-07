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
