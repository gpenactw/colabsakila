from datetime import datetime

class Store:
    def __init__(
        self,
        store_id: int,
        manager_staff_id: int,
        address_id: int,
        last_update: datetime
    ):
        self.store_id = store_id
        self.manager_staff_id = manager_staff_id
        self.address_id = address_id
        self.last_update = last_update
