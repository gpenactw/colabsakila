class CategoryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM category")
        return [Category(**row) for row in result.fetchall()]

    def add(self, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("INSERT INTO category (name, last_update) VALUES (%s, %s)", (name, now))

    def update(self, category_id, name):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("UPDATE category SET name=%s, last_update=%s WHERE category_id=%s", (name, now, category_id))

    def delete(self, category_id):
        self.db.execute("DELETE FROM category WHERE category_id=%s", (category_id,))