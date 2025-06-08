from datetime import datetime
from models.Entities.Inventory import Inventory

class InventoryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM inventory")
        return [Inventory(**row) for row in result.fetchall()]

    def add(self, film_id, store_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "INSERT INTO inventory (film_id, store_id, last_update) VALUES (%s, %s, %s)",
            (film_id, store_id, now)
        )

    def update(self, inventory_id, film_id, store_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "UPDATE inventory SET film_id=%s, store_id=%s, last_update=%s WHERE inventory_id=%s",
            (film_id, store_id, now, inventory_id)
        )

    def delete(self, inventory_id):
        self.db.execute("DELETE FROM inventory WHERE inventory_id=%s", (inventory_id,))