from datetime import datetime
from models.DTO.Address import Address
class AddressModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM address")
        return [Address(**row) for row in result.fetchall()]

    def add(self, address, address2, district, city_id, postal_code, phone, location):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            INSERT INTO address (address, address2, district, city_id, postal_code, phone, location, last_update)
            VALUES (%s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), %s)
        """, (address, address2, district, city_id, postal_code, phone, location, now))

    def update(self, address_id, address, address2, district, city_id, postal_code, phone, location):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            UPDATE address SET address=%s, address2=%s, district=%s, city_id=%s,
            postal_code=%s, phone=%s, location=ST_GeomFromText(%s), last_update=%s
            WHERE address_id=%s
        """, (address, address2, district, city_id, postal_code, phone, location, now, address_id))

    def delete(self, address_id):
        self.db.execute("DELETE FROM address WHERE address_id=%s", (address_id,))