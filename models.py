from datetime import datetime
from entities import Actor

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
