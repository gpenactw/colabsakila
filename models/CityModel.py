from datetime import datetime
from models.DTO.City import City

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
