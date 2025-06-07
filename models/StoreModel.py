from datetime import datetime
from models.DTO.Store import Store

class StoreModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("""
            SELECT s.*, 
                   st.first_name as manager_first_name, st.last_name as manager_last_name,
                   a.address, a.district, c.city, co.country
            FROM store s
            JOIN staff st ON s.manager_staff_id = st.staff_id
            JOIN address a ON s.address_id = a.address_id
            JOIN city c ON a.city_id = c.city_id
            JOIN country co ON c.country_id = co.country_id
            ORDER BY s.store_id
        """)
        stores = []
        for row in result.fetchall():
            store = Store(
                store_id=row['store_id'],
                manager_staff_id=row['manager_staff_id'],
                address_id=row['address_id'],
                last_update=row['last_update']
            )
            store.manager_name = f"{row['manager_first_name']} {row['manager_last_name']}"
            store.full_address = f"{row['address']}, {row['district']}, {row['city']}, {row['country']}"
            stores.append(store)
        return stores

    def get_by_id(self, store_id):
        result = self.db.execute(
            "SELECT * FROM store WHERE store_id = %s",
            (store_id,)
        )
        row = result.fetchone()
        if row:
            return Store(**row)
        return None

    def add(self, manager_staff_id, address_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """INSERT INTO store (manager_staff_id, address_id, last_update) 
               VALUES (%s, %s, %s)""",
            (manager_staff_id, address_id, now)
        )

    def update(self, store_id, manager_staff_id, address_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """UPDATE store 
               SET manager_staff_id=%s, address_id=%s, last_update=%s 
               WHERE store_id=%s""",
            (manager_staff_id, address_id, now, store_id)
        )

    def delete(self, store_id):
        self.db.execute("DELETE FROM store WHERE store_id=%s", (store_id,))

    def store_id_exists(self, store_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM store WHERE store_id=%s",
            (store_id,)
        )
        return result.fetchone()['count'] > 0

    def staff_exists(self, staff_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM staff WHERE staff_id=%s",
            (staff_id,)
        )
        return result.fetchone()['count'] > 0

    def address_exists(self, address_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM address WHERE address_id=%s",
            (address_id,)
        )
        return result.fetchone()['count'] > 0

    def staff_is_manager(self, staff_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM store WHERE manager_staff_id=%s",
            (staff_id,)
        )
        return result.fetchone()['count'] > 0

    def address_used_by_store(self, address_id, exclude_id=None):
        if exclude_id:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM store WHERE address_id=%s AND store_id != %s",
                (address_id, exclude_id)
            )
        else:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM store WHERE address_id=%s",
                (address_id,)
            )
        return result.fetchone()['count'] > 0

    def get_store_inventory_count(self, store_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM inventory WHERE store_id=%s",
            (store_id,)
        )
        return result.fetchone()['count']

    def get_store_staff_count(self, store_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM staff WHERE store_id=%s",
            (store_id,)
        )
        return result.fetchone()['count']