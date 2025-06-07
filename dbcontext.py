import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class DbContext:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            port=int(os.getenv("DB_PORT")),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )
        self.cursor = self.conn.cursor(dictionary=True , buffered=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()
        return self.cursor

    def close(self):
        self.cursor.close()
        self.conn.close()
