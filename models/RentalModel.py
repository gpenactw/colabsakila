from datetime import datetime
from models.Entities.Rental import Rental

class RentalModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("""
            SELECT r.*, 
                   c.first_name as customer_first_name, c.last_name as customer_last_name,
                   s.first_name as staff_first_name, s.last_name as staff_last_name,
                   i.inventory_id, f.title as film_title
            FROM rental r
            JOIN customer c ON r.customer_id = c.customer_id
            JOIN staff s ON r.staff_id = s.staff_id
            JOIN inventory i ON r.inventory_id = i.inventory_id
            JOIN film f ON i.film_id = f.film_id
            ORDER BY r.rental_date DESC
        """)
        rentals = []
        for row in result.fetchall():
            rental = Rental(
                rental_id=row['rental_id'],
                rental_date=row['rental_date'],
                inventory_id=row['inventory_id'],
                customer_id=row['customer_id'],
                return_date=row['return_date'],
                staff_id=row['staff_id'],
                last_update=row['last_update']
            )
            rental.customer_name = f"{row['customer_first_name']} {row['customer_last_name']}"
            rental.staff_name = f"{row['staff_first_name']} {row['staff_last_name']}"
            rental.film_title = row['film_title']
            rentals.append(rental)
        return rentals

    def get_by_id(self, rental_id):
        result = self.db.execute(
            "SELECT * FROM rental WHERE rental_id = %s",
            (rental_id,)
        )
        row = result.fetchone()
        if row:
            return Rental(**row)
        return None

    def add(self, rental_date, inventory_id, customer_id, staff_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """INSERT INTO rental (rental_date, inventory_id, customer_id, staff_id, last_update) 
               VALUES (%s, %s, %s, %s, %s)""",
            (rental_date, inventory_id, customer_id, staff_id, now)
        )

    def update(self, rental_id, rental_date, inventory_id, customer_id, return_date, staff_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """UPDATE rental 
               SET rental_date=%s, inventory_id=%s, customer_id=%s, return_date=%s, staff_id=%s, last_update=%s 
               WHERE rental_id=%s""",
            (rental_date, inventory_id, customer_id, return_date, staff_id, now, rental_id)
        )

    def delete(self, rental_id):
        self.db.execute("DELETE FROM rental WHERE rental_id=%s", (rental_id,))

    def rental_id_exists(self, rental_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM rental WHERE rental_id=%s",
            (rental_id,)
        )
        return result.fetchone()['count'] > 0

    def inventory_exists(self, inventory_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM inventory WHERE inventory_id=%s",
            (inventory_id,)
        )
        return result.fetchone()['count'] > 0

    def inventory_available(self, inventory_id):
        result = self.db.execute(
            """SELECT COUNT(*) as count FROM rental 
               WHERE inventory_id=%s AND return_date IS NULL""",
            (inventory_id,)
        )
        return result.fetchone()['count'] == 0

    def customer_exists(self, customer_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM customer WHERE customer_id=%s",
            (customer_id,)
        )
        return result.fetchone()['count'] > 0

    def staff_exists(self, staff_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM staff WHERE staff_id=%s",
            (staff_id,)
        )
        return result.fetchone()['count'] > 0

    def get_active_rentals(self):
        result = self.db.execute("""
            SELECT r.*, 
                   c.first_name as customer_first_name, c.last_name as customer_last_name,
                   f.title as film_title
            FROM rental r
            JOIN customer c ON r.customer_id = c.customer_id
            JOIN inventory i ON r.inventory_id = i.inventory_id
            JOIN film f ON i.film_id = f.film_id
            WHERE r.return_date IS NULL
            ORDER BY r.rental_date
        """)
        rentals = []
        for row in result.fetchall():
            rental = Rental(
                rental_id=row['rental_id'],
                rental_date=row['rental_date'],
                inventory_id=row['inventory_id'],
                customer_id=row['customer_id'],
                return_date=row['return_date'],
                staff_id=row['staff_id'],
                last_update=row['last_update']
            )
            rental.customer_name = f"{row['customer_first_name']} {row['customer_last_name']}"
            rental.film_title = row['film_title']
            rentals.append(rental)
        return rentals

    def return_rental(self, rental_id, return_date):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """UPDATE rental 
               SET return_date=%s, last_update=%s 
               WHERE rental_id=%s""",
            (return_date, now, rental_id)
        )