class CountryModel:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        result = self.db.execute("SELECT * FROM country")
        return [Country(**row) for row in result.fetchall()]

    def add(self, country):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("INSERT INTO country (country, last_update) VALUES (%s, %s)", (country, now))

    def update(self, country_id, country):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.execute("UPDATE country SET country=%s, last_update=%s WHERE country_id=%s", (country, now, country_id))

    def delete(self, country_id):
        self.db.execute("DELETE FROM country WHERE country_id=%s", (country_id,))