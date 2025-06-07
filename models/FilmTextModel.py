from datetime import datetime
from models.DTO.FilmText import FilmText

class FilmTextModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM film_text")
        return [FilmText(**row) for row in result.fetchall()]

    def film_id_exists(self, film_id):
        result = self.db.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return result.fetchone() is not None

    def film_text_exists(self, film_id):
        result = self.db.execute("SELECT 1 FROM film_text WHERE film_id = %s", (film_id,))
        return result.fetchone() is not None

    def add(self, film_id, title, description):
        self.db.execute(
            "INSERT INTO film_text (film_id, title, description) VALUES (%s, %s, %s)",
            (film_id, title, description)
        )

    def update(self, film_id, title, description):
        self.db.execute(
            "UPDATE film_text SET title = %s, description = %s WHERE film_id = %s",
            (title, description, film_id)
        )

    def delete(self, film_id):
        self.db.execute("DELETE FROM film_text WHERE film_id = %s", (film_id,))