from datetime import datetime
from models.Entities.Language import Language

class LanguageModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM language")
        return [Language(**row) for row in result.fetchall()]

    def add(self, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "INSERT INTO language (name, last_update) VALUES (%s, %s)",
            (name, now)
        )

    def update(self, language_id, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "UPDATE language SET name=%s, last_update=%s WHERE language_id=%s",
            (name, now, language_id)
        )

    def delete(self, language_id):
        self.db.execute("DELETE FROM language WHERE language_id=%s", (language_id,))

    def language_exists(self, name, exclude_id=None):
        if exclude_id:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM language WHERE name=%s AND language_id != %s",
                (name, exclude_id)
            )
        else:
            result = self.db.execute(
                "SELECT COUNT(*) as count FROM language WHERE name=%s",
                (name,)
            )
        return result.fetchone()['count'] > 0

    def language_id_exists(self, language_id):
        result = self.db.execute(
            "SELECT COUNT(*) as count FROM language WHERE language_id=%s",
            (language_id,)
        )
        return result.fetchone()['count'] > 0