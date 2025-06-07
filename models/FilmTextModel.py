from datetime import datetime
from models.DTO.FilmText import FilmText

class FilmTextModel:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all(self):
        self.cursor.execute("SELECT * FROM film_text")
        return self.cursor.fetchall()

    def film_id_exists(self, film_id):
        self.cursor.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return self.cursor.fetchone() is not None

    def film_text_exists(self, film_id):
        self.cursor.execute("SELECT 1 FROM film_text WHERE film_id = %s", (film_id,))
        return self.cursor.fetchone() is not None

    def create_film_text(self, film_id, title, description):
        query = """
            INSERT INTO film_text (film_id, title, description)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (film_id, title, description))
        self.conn.commit()

    def update_film_text(self, film_id, title, description):
        query = """
            UPDATE film_text
            SET title = %s, description = %s
            WHERE film_id = %s
        """
        self.cursor.execute(query, (title, description, film_id))
        self.conn.commit()

    def delete_film_text(self, film_id):
        self.cursor.execute("DELETE FROM film_text WHERE film_id = %s", (film_id,))
        self.conn.commit()