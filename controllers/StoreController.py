class StoreController:
    def __init__(self, model):
        self.model = model

    def list_stores(self):
        stores = self.model.get_all()
        print("\n--- Lista de Tiendas ---")
        if not stores:
            print("No hay tiendas registradas.")
            return
        
        print(f"{'ID':>4} | {'Gerente':<25} | {'Dirección':<60}")
        print("-" * 95)
        for store in stores:
            print(f"{store.store_id:>4} | {store.manager_name:<25} | {store.full_address:<60}")
        
        print("\n--- Estadísticas por Tienda ---")
        for store in stores:
            inventory_count = self.model.get_store_inventory_count(store.store_id)
            staff_count = self.model.get_store_staff_count(store.store_id)
            print(f"Tienda {store.store_id}: {inventory_count} items en inventario, {staff_count} empleados")

    def create_store(self):
        try:
            manager_staff_id = int(input("ID del gerente (personal): "))
            if not self.model.staff_exists(manager_staff_id):
                print(f"Error: No existe personal con ID {manager_staff_id}.")
                return
            if self.model.staff_is_manager(manager_staff_id):
                print(f"Error: El personal con ID {manager_staff_id} ya es gerente de otra tienda.")
                return
        except ValueError:
            print("ID de gerente inválido.")
            return

        try:
            address_id = int(input("ID de dirección: "))
            if not self.model.address_exists(address_id):
                print(f"Error: No existe una dirección con ID {address_id}.")
                return
            if self.model.address_used_by_store(address_id):
                print(f"Error: La dirección con ID {address_id} ya está siendo usada por otra tienda.")
                return
        except ValueError:
            print("ID de dirección inválido.")
            return

        try:
            self.model.add(manager_staff_id, address_id)
            print("Tienda creada exitosamente.")
        except Exception as err:
            print(f"Error al crear la tienda: {err}")

    def update_store(self):
        try:
            store_id = int(input("ID de la tienda a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.store_id_exists(store_id):
            print(f"No existe una tienda con ID {store_id}.")
            return

        store = self.model.get_by_id(store_id)
        print(f"\nTienda actual - Gerente ID: {store.manager_staff_id}, Dirección ID: {store.address_id}")

        try:
            manager_input = input(f"Nuevo ID del gerente (actual: {store.manager_staff_id}): ")
            manager_staff_id = int(manager_input) if manager_input else store.manager_staff_id
            
            if manager_staff_id != store.manager_staff_id:
                if not self.model.staff_exists(manager_staff_id):
                    print(f"Error: No existe personal con ID {manager_staff_id}.")
                    return
                if self.model.staff_is_manager(manager_staff_id):
                    print(f"Error: El personal con ID {manager_staff_id} ya es gerente de otra tienda.")
                    return
        except ValueError:
            print("ID de gerente inválido.")
            return

        try:
            address_input = input(f"Nuevo ID de dirección (actual: {store.address_id}): ")
            address_id = int(address_input) if address_input else store.address_id
            
            if address_id != store.address_id:
                if not self.model.address_exists(address_id):
                    print(f"Error: No existe una dirección con ID {address_id}.")
                    return
                if self.model.address_used_by_store(address_id, exclude_id=store_id):
                    print(f"Error: La dirección con ID {address_id} ya está siendo usada por otra tienda.")
                    return
        except ValueError:
            print("ID de dirección inválido.")
            return

        try:
            self.model.update(store_id, manager_staff_id, address_id)
            print("Tienda actualizada exitosamente.")
        except Exception as err:
            print(f"Error al actualizar la tienda: {err}")

    def delete_store(self):
        try:
            store_id = int(input("ID de la tienda a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        if not self.model.store_id_exists(store_id):
            print(f"No existe una tienda con ID {store_id}.")
            return

        inventory_count = self.model.get_store_inventory_count(store_id)
        staff_count = self.model.get_store_staff_count(store_id)
        
        if inventory_count > 0 or staff_count > 0:
            print(f"\nAdvertencia: Esta tienda tiene {inventory_count} items en inventario y {staff_count} empleados.")
        
        confirm = input(f"¿Estás seguro de que deseas eliminar la tienda con ID {store_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(store_id)
            print("Tienda eliminada exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1451:
                print("No se puede eliminar la tienda: tiene registros relacionados (inventario, personal, clientes).")
            else:
                print(f"Error al eliminar la tienda: {err}")

    def show_store_details(self):
        try:
            store_id = int(input("ID de la tienda: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.store_id_exists(store_id):
            print(f"No existe una tienda con ID {store_id}.")
            return

        stores = self.model.get_all()
        store = next((s for s in stores if s.store_id == store_id), None)
        
        if store:
            print(f"\n=== Detalles de la Tienda {store_id} ===")
            print(f"Gerente: {store.manager_name}")
            print(f"Dirección: {store.full_address}")
            print(f"Última actualización: {store.last_update}")
            
            inventory_count = self.model.get_store_inventory_count(store_id)
            staff_count = self.model.get_store_staff_count(store_id)
            print(f"\nEstadísticas:")
            print(f"- Items en inventario: {inventory_count}")
            print(f"- Empleados: {staff_count}")