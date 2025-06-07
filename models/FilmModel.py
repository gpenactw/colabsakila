from datetime import datetime
from models.DTO.Film import Film

class FilmModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM film")
        return [Film(**row) for row in result.fetchall()]

    def film_exists(self, title, release_year, exclude_id=None):
        query = "SELECT COUNT(*) AS count FROM film WHERE title = %s AND release_year = %s"
        params = [title, release_year]
        if exclude_id:
            query += " AND film_id != %s"
            params.append(exclude_id)
        result = self.db.execute(query, tuple(params))
        row = result.fetchone()
        if row is None:
            return False
        return row['count'] > 0

    def film_id_exists(self, film_id):
        result = self.db.execute("SELECT COUNT(*) FROM film WHERE film_id = %s", (film_id,))
        return result.fetchone()[0] > 0

    def add(self, title, description, release_year, language_id, original_language_id,
            rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update):
        self.db.execute("""
            INSERT INTO film (
                title, description, release_year, language_id, original_language_id,
                rental_duration, rental_rate, length, replacement_cost,
                rating, special_features, last_update
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            title, description, release_year, language_id, original_language_id,
            rental_duration, rental_rate, length, replacement_cost,
            rating, special_features, last_update
        ))

    def update(self, film_id, title, description, release_year, language_id, original_language_id,
               rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update):
        self.db.execute("""
            UPDATE film SET
                title = %s,
                description = %s,
                release_year = %s,
                language_id = %s,
                original_language_id = %s,
                rental_duration = %s,
                rental_rate = %s,
                length = %s,
                replacement_cost = %s,
                rating = %s,
                special_features = %s,
                last_update = %s
            WHERE film_id = %s
        """, (
            title, description, release_year, language_id, original_language_id,
            rental_duration, rental_rate, length, replacement_cost,
            rating, special_features, last_update, film_id
        ))

    def delete(self, film_id):
        self.db.execute("DELETE FROM film WHERE film_id = %s", (film_id,))