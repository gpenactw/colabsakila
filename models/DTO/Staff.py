from datetime import datetime
from typing import Optional

class Staff:
    def __init__(
        self,
        staff_id: int,
        first_name: str,
        last_name: str,
        address_id: int,
        picture: Optional[bytes],
        email: Optional[str],
        store_id: int,
        active: bool,
        username: str,
        password: Optional[str],
        last_update: datetime
    ):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        self.picture = picture
        self.email = email
        self.store_id = store_id
        self.active = bool(active)
        self.username = username
        self.password = password
        self.last_update = last_update
