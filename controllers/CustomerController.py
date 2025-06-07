class CustomerController:
    def __init__(self, model):
        self.model = model

    def list_customers(self):
        customers = self.model.get_all()
        print("\n--- Lista de Clientes ---")
        for customer in customers:
            print(f"ID: {customer.customer_id}, Nombre: {customer.first_name} {customer.last_name},"
                  f"Store: {customer.store_id}, Email: {customer.email}, Address ID: {customer.address_id}, Activo: {customer.active},"
                  f"Fecha de creación: {customer.create_date}, Última actualización: {customer.last_update}")

    def create_customer(self):
        store_id = int(input("ID de tienda: "))
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        email = input("Email: ")
        address_id = int(input("ID de dirección: "))
        active_input = input("Activo (1 para sí, 0 para no): ")
        active = int(active_input) if active_input in ['0', '1'] else 1
        create_date = None
        from datetime import datetime
        create_date = datetime.now()

        try:
            self.model.add(store_id, first_name, last_name, email, address_id, active, create_date)
            print("Cliente creado exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno'):
                if err.errno == 1452:
                    print("Error: El ID de tienda no existe en la tabla store.")
                elif err.errno == 1062:
                    print("Error: Ya existe un cliente con ese email.")
                else:
                    print(f"Error inesperado al crear cliente: {err}")
            else:
                print(f"Error inesperado al crear cliente: {err}")

    def update_customer(self):
        customer_id = int(input("ID del cliente a actualizar: "))
        store_id = int(input("Nuevo ID de tienda: "))
        first_name = input("Nuevo nombre: ")
        last_name = input("Nuevo apellido: ")
        email = input("Actualización email: ")
        address_id = int(input("ID de dirección actualizada: "))
        active_input = input("Actualización de actividad (1 para sí, 0 para no): ")
        active = int(active_input) if active_input in ['0', '1'] else 1
        try:
            self.model.update(customer_id, store_id, first_name, last_name, email, address_id, active)
            print("Cliente actualizado exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno'):
                if err.errno == 1452:
                    print("Error: El ID de tienda no existe en la tabla store.")
                elif err.errno == 1062:
                    print("Error: Ya existe un cliente con ese email.")
                else:
                    print(f"Error inesperado al crear cliente: {err}")
            else:
                print(f"Error inesperado al crear cliente: {err}")

    def delete_customer(self):
        customer_id = int(input("ID del cliente a eliminar: "))
        try:
            self.model.delete(customer_id)
            print("Cliente eliminado exitosamente.")
        except Exception as err:
            print(f"Error inesperado al eliminar cliente: {err}")