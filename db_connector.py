import sqlite3

class db_connector():
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()
    def setup_tables(self):
            self.cur.execute("""CREATE TABLE logs (
                                id INTEGER PRIMARY KEY,
                                date TEXT,
                                info TEXT,
                                status TEXT)""")
            self.cur.execute("""CREATE TABLE oto_moto_cars(
                                id INTEGER PRIMARY KEY,
                                brand TEXT,
                                model TEXT,
                                full_name TEXT,
                                fuel_type TEXT,
                                price_currency TEXT,
                                price_amount INTEGER,
                                year INTEGER,
                                odometer_unit TEXT,
                                odometer_amount TEXT)"""
                            )
        
    def insert_car(self,car,target):
        self.cur.execute(f"""INSERT INTO {target} (brand, model, full_name, fuel_type, price_currency, price_amount, year, odometer_unit, odometer_amount) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",(car.brand, car.model, car.full_name, car.fuel_type, car.price['currency'], car.price['amount'], car.year, car.odometer['unit'], car.odometer['amount']))
        self.conn.commit()

if __name__=="__main__":
     db=db_connector("database/database.db")
     db.setup_tables()