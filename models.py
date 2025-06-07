from datetime import datetime
from entities import *

class ActorModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM actor")
        return [Actor(**row) for row in result.fetchall()]

    def add(self, first_name, last_name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "INSERT INTO actor (first_name, last_name, last_update) VALUES (%s, %s, %s)",
            (first_name, last_name, now)
        )

    def update(self, actor_id, first_name, last_name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "UPDATE actor SET first_name=%s, last_name=%s, last_update=%s WHERE actor_id=%s",
            (first_name, last_name, now, actor_id)
        )

    def delete(self, actor_id):
        self.db.execute("DELETE FROM actor WHERE actor_id=%s", (actor_id,))

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
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (address, address2, district, city_id, postal_code, phone, location, now))

    def update(self, address_id, address, address2, district, city_id, postal_code, phone, location):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            UPDATE address SET address=%s, address2=%s, district=%s, city_id=%s,
            postal_code=%s, phone=%s, location=%s, last_update=%s
            WHERE address_id=%s
        """, (address, address2, district, city_id, postal_code, phone, location, now, address_id))

    def delete(self, address_id):
        self.db.execute("DELETE FROM address WHERE address_id=%s", (address_id,))


class CategoryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM category")
        return [Category(**row) for row in result.fetchall()]

    def add(self, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("INSERT INTO category (name, last_update) VALUES (%s, %s)", (name, now))

    def update(self, category_id, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("UPDATE category SET name=%s, last_update=%s WHERE category_id=%s", (name, now, category_id))

    def delete(self, category_id):
        self.db.execute("DELETE FROM category WHERE category_id=%s", (category_id,))


class CityModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM city")
        return [City(**row) for row in result.fetchall()]

    def add(self, city, country_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("INSERT INTO city (city, country_id, last_update) VALUES (%s, %s, %s)", (city, country_id, now))

    def update(self, city_id, city, country_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("UPDATE city SET city=%s, country_id=%s, last_update=%s WHERE city_id=%s", (city, country_id, now, city_id))

    def delete(self, city_id):
        self.db.execute("DELETE FROM city WHERE city_id=%s", (city_id,))


class CountryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM country")
        return [Country(**row) for row in result.fetchall()]

    def add(self, country):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("INSERT INTO country (country, last_update) VALUES (%s, %s)", (country, now))

    def update(self, country_id, country):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("UPDATE country SET country=%s, last_update=%s WHERE country_id=%s", (country, now, country_id))

    def delete(self, country_id):
        self.db.execute("DELETE FROM country WHERE country_id=%s", (country_id,))


class CustomerModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM customer")
        return [Customer(**row) for row in result.fetchall()]

    def add(self, store_id, first_name, last_name, email, address_id, active):
        create_date = datetime.now().strftime('%Y-%m-%d')
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date, last_update)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (store_id, first_name, last_name, email, address_id, active, create_date, last_update))

    def update(self, customer_id, store_id, first_name, last_name, email, address_id, active):
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("""
            UPDATE customer SET store_id=%s, first_name=%s, last_name=%s, email=%s,
            address_id=%s, active=%s, last_update=%s
            WHERE customer_id=%s
        """, (store_id, first_name, last_name, email, address_id, active, last_update, customer_id))

    def delete(self, customer_id):
        self.db.execute("DELETE FROM customer WHERE customer_id=%s", (customer_id,))
