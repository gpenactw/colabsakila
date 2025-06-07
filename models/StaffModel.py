from datetime import datetime
from models.DTO.Staff import Staff

class StaffModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("""
            SELECT s.*, st.store_id as store_name, a.address, a.district, c.city
            FROM staff s
            LEFT JOIN store st ON s.store_id = st.store_id
            LEFT JOIN address a ON s.address_id = a.address_id
            LEFT JOIN city c ON a.city_id = c.city_id
            ORDER BY s.staff_id
        """)
        staff_list = []
        for row in result.fetchall():
            staff = Staff(
                staff_id=row['staff_id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                address_id=row['address_id'],
                picture=row['picture'],
                email=row['email'],
                store_id=row['store_id'],
                active=row['active'],
                username=row['username'],
                password=row['password'],
                last_update=row['last_update']
            )
            staff.full_address = f"{row['address']}, {row['district']}, {row['city']}" if row['address'] else "N/A"
            staff_list.append(staff)
        return staff_list

    def get_by_id(self, staff_id):
        result = self.db.execute(
            "SELECT * FROM staff WHERE staff_id = %s",
            (staff_id,)
        )
        row = result.fetchone()
        if row:
            return Staff(**row)
        return None

    def add(self, first_name, last_name, address_id, email, store_id, active, username, password):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """INSERT INTO staff (first_name, last_name, address_id, email, store_id, active, username, password, last_update) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (first_name, last_name, address_id, email, store_id, active, username, password, now)
        )

    def update(self, staff_id, first_name, last_name, address_id, email, store_id, active, username, password=None):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if password:
            self.db.execute(
                """UPDATE staff 
                   SET first_name=%s, last_name=%s, address_id=%s, email=%s, store_id=%s, 
                       active=%s, username=%s, password=%s, last_update=%s 
                   WHERE staff_id=%s""",
                (first_name, last_name, address_id, email, store_id, active, username, password, now, staff_id)
            )
        else:
            self.db.execute(
                """UPDATE staff 
                   SET first_name=%s, last_name=%s, address_id=%s, email=%s, store_id=%s, 
                       active=%s, username=%s, last_update=%s 
                   WHERE staff_id=%s""",
                (first_name, last_name, address_id, email, store_id, active, username, now, staff_id)
            )

    def delete(self, staff_id):
        self.db.execute("DELETE FROM staff WHERE staff_id=%s", (staff_id,))

    def staff_id_exists(self, staff_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM staff WHERE staff_id=%s",
            (staff_id,)
        )
        return result.fetchone()['count'] > 0

    def username_exists(self, username, exclude_id=None):
        if exclude_id:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM staff WHERE username=%s AND staff_id != %s",
                (username, exclude_id)
            )
        else:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM staff WHERE username=%s",
                (username,)
            )
        return result.fetchone()['count'] > 0

    def email_exists(self, email, exclude_id=None):
        if exclude_id:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM staff WHERE email=%s AND staff_id != %s",
                (email, exclude_id)
            )
        else:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM staff WHERE email=%s",
                (email,)
            )
        return result.fetchone()['count'] > 0

    def address_exists(self, address_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM address WHERE address_id=%s",
            (address_id,)
        )
        return result.fetchone()['count'] > 0

    def store_exists(self, store_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM store WHERE store_id=%s",
            (store_id,)
        )
        return result.fetchone()['count'] > 0

    def get_active_staff(self):
        result = self.db.execute(
            "SELECT * FROM staff WHERE active = 1 ORDER BY first_name, last_name"
        )
        return [Staff(**row) for row in result.fetchall()]