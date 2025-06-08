from datetime import datetime
from typing import Optional

class Rental:
    def __init__(
        self,
        rental_id: int,
        rental_date: datetime,
        inventory_id: int,
        customer_id: int,
        return_date: Optional[datetime],
        staff_id: int,
        last_update: datetime
    ):
        self.rental_id = rental_id
        self.rental_date = rental_date
        self.inventory_id = inventory_id
        self.customer_id = customer_id
        self.return_date = return_date
        self.staff_id = staff_id
        self.last_update = last_update
