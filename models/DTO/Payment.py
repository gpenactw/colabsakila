from datetime import datetime
from typing import Optional

class Payment:
    def __init__(
        self,
        payment_id: int,
        customer_id: int,
        staff_id: int,
        rental_id: Optional[int],
        amount: float,
        payment_date: datetime,
        last_update: Optional[datetime]
    ):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.staff_id = staff_id
        self.rental_id = rental_id
        self.amount = amount
        self.payment_date = payment_date
        self.last_update = last_update
