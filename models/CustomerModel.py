from datetime import datetime
from models.DTO.Customer import Customer

class CustomerModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM customer")
        return [Customer(**row) for row in result.fetchall()]

    def customer_exists(self, customer_id):
        result = self.db.execute("SELECT 1 FROM customer WHERE customer_id = %s", (customer_id,))
        return result.fetchone() is not None

    def add(self, store_id, first_name, last_name, email, address_id, active, create_date):
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date, last_update)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (store_id, first_name, last_name, email, address_id, active, create_date, last_update))

    def update(self, customer_id, store_id, first_name, last_name, email, address_id, active):
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            UPDATE customer
            SET store_id = %s,
                first_name = %s,
                last_name = %s,
                email = %s,
                address_id = %s,
                active = %s,
                last_update = %s
            WHERE customer_id = %s
        """, (store_id, first_name, last_name, email, address_id, active, last_update, customer_id))

    def delete(self, customer_id):
        self.db.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))