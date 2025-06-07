from datetime import datetime
from models.DTO.FilmCategory import FilmCategory

class FilmCategoryModel:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all(self):
        self.cursor.execute("SELECT * FROM film_category")
        return self.cursor.fetchall()

    def film_id_exists(self, film_id):
        self.cursor.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return self.cursor.fetchone() is not None

    def category_exists(self, category_id):
        self.cursor.execute("SELECT 1 FROM category WHERE category_id = %s", (category_id,))
        return self.cursor.fetchone() is not None

    def film_category_exists(self, film_id, category_id):
        self.cursor.execute(
            "SELECT 1 FROM film_category WHERE film_id = %s AND category_id = %s",
            (film_id, category_id)
        )
        return self.cursor.fetchone() is not None

    def create_film_category(self, film_id, category_id, last_update):
        query = """
            INSERT INTO film_category (film_id, category_id, last_update)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (film_id, category_id, last_update))
        self.conn.commit()

    def update_film_category(self, film_id, category_id, last_update):
        query = """
            UPDATE film_category
            SET last_update = %s
            WHERE film_id = %s AND category_id = %s
        """
        self.cursor.execute(query, (last_update, film_id, category_id))
        self.conn.commit()

    def delete_film_category(self, film_id, category_id):
        query = "DELETE FROM film_category WHERE film_id = %s AND category_id = %s"
        self.cursor.execute(query, (film_id, category_id))
        self.conn.commit()

from datetime import datetime
from entities import Film_Text