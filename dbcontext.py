import mysql.connector

class DbContext:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="pythonuser",
            port=3307,
            password="2930",
            database="sakila"
        )
        self.cursor = self.conn.cursor(dictionary=True , buffered=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def close(self):
        self.cursor.close()
        self.conn.close()
