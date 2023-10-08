import sqlite3

class SQLiteWriter:
    def __init__(self, db):
        self.db = db
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id TEXT UNIQUE,
            car_manufacturer TEXT,
            car_model TEXT,
            car_year TEXT,
            car_modification TEXT,
            link_to_page TEXT,
            car_price TEXT,
            car_run TEXT,
            car_engine TEXT,
            car_gearbox TEXT,
            car_color TEXT,
            car_condition TEXT,
            car_drive TEXT
        );
        """
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(create_table_query)

    def insert_car(self, data: list):
        query = """
        INSERT INTO cars (
            car_id,
            car_manufacturer,
            car_model,
            car_year,
            car_modification,
            link_to_page,
            car_price,
            car_run,
            car_engine,
            car_gearbox,
            car_color,
            car_condition,
            car_drive
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query, data)
