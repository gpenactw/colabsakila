from datetime import datetime
from models.DTO.FilmActor import FilmActor

class FilmActorModel:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)

    def get_all(self):
        self.cursor.execute("SELECT * FROM film_actor")
        return self.cursor.fetchall()

    def actor_exists(self, actor_id):
        self.cursor.execute("SELECT 1 FROM actor WHERE actor_id = %s", (actor_id,))
        return self.cursor.fetchone() is not None

    def film_id_exists(self, film_id):
        self.cursor.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return self.cursor.fetchone() is not None

    def film_actor_exists(self, actor_id, film_id):
        self.cursor.execute(
            "SELECT 1 FROM film_actor WHERE actor_id = %s AND film_id = %s",
            (actor_id, film_id)
        )
        return self.cursor.fetchone() is not None

    def create_film_actor(self, actor_id, film_id, last_update):
        query = """
            INSERT INTO film_actor (actor_id, film_id, last_update)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (actor_id, film_id, last_update))
        self.conn.commit()

    def update_film_actor(self, actor_id, film_id, last_update):
        query = """
            UPDATE film_actor
            SET last_update = %s
            WHERE actor_id = %s AND film_id = %s
        """
        self.cursor.execute(query, (last_update, actor_id, film_id))
        self.conn.commit()

    def delete_film_actor(self, actor_id, film_id):
        query = "DELETE FROM film_actor WHERE actor_id = %s AND film_id = %s"
        self.cursor.execute(query, (actor_id, film_id))
        self.conn.commit()