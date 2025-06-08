from datetime import datetime

class Inventory:
    def __init__(self, inventory_id: int, film_id: int, store_id: int, last_update: datetime):
        self.inventory_id = inventory_id
        self.film_id = film_id
        self.store_id = store_id
        self.last_update = last_update
