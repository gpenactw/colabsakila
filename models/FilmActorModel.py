from datetime import datetime
from models.Entities.FilmActor import FilmActor

class FilmActorModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM film_actor")
        return [FilmActor(**row) for row in result.fetchall()]

    def actor_exists(self, actor_id):
        result = self.db.execute("SELECT 1 FROM actor WHERE actor_id = %s", (actor_id,))
        return result.fetchone() is not None

    def film_id_exists(self, film_id):
        result = self.db.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return result.fetchone() is not None

    def film_actor_exists(self, actor_id, film_id):
        result = self.db.execute(
            "SELECT 1 FROM film_actor WHERE actor_id = %s AND film_id = %s",
            (actor_id, film_id)
        )
        return result.fetchone() is not None

    def create_film_actor(self, actor_id, film_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = """
            INSERT INTO film_actor (actor_id, film_id, last_update)
            VALUES (%s, %s, %s)
        """
        try:
            self.db.execute(query, (actor_id, film_id, now))
            print("Insert realizado correctamente.")
        except Exception as err:
            print(f"Error al insertar film_actor: {err}")

    def update_film_actor(self, actor_id, film_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = """
            UPDATE film_actor
            SET last_update = %s
            WHERE actor_id = %s AND film_id = %s
        """
        self.db.execute(query, (now, actor_id, film_id))

    def delete_film_actor(self, actor_id, film_id):
        query = "DELETE FROM film_actor WHERE actor_id = %s AND film_id = %s"
        self.db.execute(query, (actor_id, film_id))
