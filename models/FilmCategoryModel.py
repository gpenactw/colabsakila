from datetime import datetime
from models.DTO.FilmCategory import FilmCategory

class FilmCategoryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM film_category")
        return [FilmCategory(**row) for row in result.fetchall()]

    def film_id_exists(self, film_id):
        result = self.db.execute("SELECT 1 FROM film WHERE film_id = %s", (film_id,))
        return result.fetchone() is not None

    def category_exists(self, category_id):
        result = self.db.execute("SELECT 1 FROM category WHERE category_id = %s", (category_id,))
        return result.fetchone() is not None

    def film_category_exists(self, film_id, category_id):
        result = self.db.execute(
            "SELECT 1 FROM film_category WHERE film_id = %s AND category_id = %s",
            (film_id, category_id)
        )
        return result.fetchone() is not None

    def add(self, film_id, category_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute(
            "INSERT INTO film_category (film_id, category_id, last_update) VALUES (%s, %s, %s)",
            (film_id, category_id, now)
        )

    def update(self, film_id, category_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = self.db.execute(
            "UPDATE film_category SET last_update = %s WHERE film_id = %s AND category_id = %s",
            (now, film_id, category_id)
        )
        # Debug: verificar cuántas filas fueron afectadas
        rows_affected = result.rowcount
        print(f"[DEBUG] Filas afectadas por el UPDATE: {rows_affected}")
        if rows_affected == 0:
            print(f"[DEBUG] No se actualizó ninguna fila. Verificando si existe la relación...")
            check_result = self.db.execute(
                "SELECT * FROM film_category WHERE film_id = %s AND category_id = %s",
                (film_id, category_id)
            )
            existing = check_result.fetchone()
            if existing:
                print(f"[DEBUG] La relación existe: {existing}")
            else:
                print(f"[DEBUG] La relación NO existe en la base de datos")

    def delete(self, film_id, category_id):
        self.db.execute("DELETE FROM film_category WHERE film_id = %s AND category_id = %s", (film_id, category_id))
