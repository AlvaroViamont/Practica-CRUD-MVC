import sqlite3
from sqlite3 import Error
from paths import DB_PATH


class BBDD:
    def __init__(self) -> None:
        self.con = None
        try:
            self.con = sqlite3.connect(DB_PATH)
            self.cursor = self.con.cursor()
        except Error as e:
            print(e)
    
    def build (self):
        try:
            self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS CATEGORY (
                                        CATEGORY_ID text PRIMARY KEY,
                                        CATEGORY_NAME text NOT NULL,
                                        CATEGORY_DESCRIPTION text
                                    )
                                ''')
            
            self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS PRODUCT (
                                        PRODUCT_ID text PRIMARY KEY,
                                        PRODUCT_NAME text NOT NULL,
                                        PRODUCT_PRICE text NOT NULL,
                                        PRODUCT_STOCK text NOT NULL,
                                        PRODUCT_DESCRIPTION text,
                                        PRODUCT_CATEGORY_ID text NOT NULL,
                                        FOREIGN KEY (PRODUCT_CATEGORY_ID) REFERENCES PATIENT(CATEGORY_ID)
                                    )
                                ''')
        except Error as e:
            print(e)
    
    def close_conection(self):
        self.con.close()