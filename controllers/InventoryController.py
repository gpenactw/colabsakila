class InventoryController:
    def __init__(self, model):
        self.model = model

    def list_inventory(self):
        inventory_items = self.model.get_all()
        print("\n--- Lista de Inventario ---")
        for item in inventory_items:
            print(f"ID: {item.inventory_id} | Film ID: {item.film_id} | Store ID: {item.store_id}")

    def create_inventory(self):
        film_id = int(input("ID de la película: "))
        store_id = int(input("ID de la tienda: "))
        self.model.add(film_id, store_id)
        print("Item de inventario creado exitosamente.")

    def update_inventory(self):
        inventory_id = int(input("ID del inventario a actualizar: "))
        film_id = int(input("Nuevo ID de película: "))
        store_id = int(input("Nuevo ID de tienda: "))
        self.model.update(inventory_id, film_id, store_id)
        print("Inventario actualizado.")

    def delete_inventory(self):
        inventory_id = int(input("ID del inventario a eliminar: "))
        self.model.delete(inventory_id)
        print("Item de inventario eliminado.")