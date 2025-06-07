from datetime import datetime
from models.DTO.Payment import Payment

class PaymentModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("""
            SELECT p.*, c.first_name as customer_name, c.last_name as customer_lastname,
                   s.first_name as staff_name, s.last_name as staff_lastname
            FROM payment p
            JOIN customer c ON p.customer_id = c.customer_id
            JOIN staff s ON p.staff_id = s.staff_id
            ORDER BY p.payment_date DESC
        """)
        payments = []
        for row in result.fetchall():
            payment = Payment(
                payment_id=row['payment_id'],
                customer_id=row['customer_id'],
                staff_id=row['staff_id'],
                rental_id=row['rental_id'],
                amount=row['amount'],
                payment_date=row['payment_date'],
                last_update=row['last_update']
            )
            payment.customer_name = f"{row['customer_name']} {row['customer_lastname']}"
            payment.staff_name = f"{row['staff_name']} {row['staff_lastname']}"
            payments.append(payment)
        return payments

    def get_by_id(self, payment_id):
        result = self.db.execute(
            "SELECT * FROM payment WHERE payment_id = %s",
            (payment_id,)
        )
        row = result.fetchone()
        if row:
            return Payment(**row)
        return None

    def add(self, customer_id, staff_id, rental_id, amount, payment_date):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date, last_update) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (customer_id, staff_id, rental_id, amount, payment_date, now)
        )

    def update(self, payment_id, customer_id, staff_id, rental_id, amount, payment_date):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            """UPDATE payment 
               SET customer_id=%s, staff_id=%s, rental_id=%s, amount=%s, payment_date=%s, last_update=%s 
               WHERE payment_id=%s""",
            (customer_id, staff_id, rental_id, amount, payment_date, now, payment_id)
        )

    def delete(self, payment_id):
        self.db.execute("DELETE FROM payment WHERE payment_id=%s", (payment_id,))

    def payment_id_exists(self, payment_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM payment WHERE payment_id=%s",
            (payment_id,)
        )
        return result.fetchone()['count'] > 0

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

    def rental_exists(self, rental_id):
        if rental_id is None:
            return True
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM rental WHERE rental_id=%s",
            (rental_id,)
        )
        return result.fetchone()['count'] > 0

    def get_total_by_customer(self, customer_id):
        result = self.db.execute(
            "SELECT SUM(amount) as total FROM payment WHERE customer_id=%s",
            (customer_id,)
        )
        row = result.fetchone()
        return row['total'] if row['total'] else 0

    def get_payments_by_date_range(self, start_date, end_date):
        result = self.db.execute(
            """SELECT * FROM payment 
               WHERE payment_date BETWEEN %s AND %s 
               ORDER BY payment_date DESC""",
            (start_date, end_date)
        )
        return [Payment(**row) for row in result.fetchall()]