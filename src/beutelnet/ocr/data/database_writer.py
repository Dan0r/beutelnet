import sqlite3
from ocr.process_ocr import ProcessOcr 
from ocr.process_image import ProcessImage
from config import DATABASE_PATH

class DatabaseWriter:

    def __init__(self, database_path):
        self.database_path = database_path

    """Pushes {vacuum-name, bag size, supermarket name}"""
    def push_data(self, data: list[dict[str, str]]):
        query =  "INSERT INTO bags (supermarket, bag, vacuum) VALUES (:supermarket, :bag, :vacuum)"
        with sqlite3.connect(self.database_path) as con:
            cur = con.cursor()
            cur.executemany(query, data)
            con.commit()

    def create_table(self):
        table_query = """
        CREATE TABLE IF NOT EXISTS bags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supermarket TEXT NOT NULL,
            bag TEXT NOT NULL,
            vacuum TEXT NOT NULL
        );
        """

        with sqlite3.connect(self.database_path) as con:
            cur = con.cursor()
            cur.execute(table_query)
            con.commit()
        print("Created Table")
