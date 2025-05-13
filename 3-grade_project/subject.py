import random
import sqlite3
import kontrol


class Subjects():
    def __init__(self, id='', name=''):
        self.id=random.randint(0, 10000)
        self.name=name
        self.db_conn=kontrol.get_db_connection()
        self.db_cursor=self.db_conn.cursor()
        self.create_table()
        
    
        

    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                                id INTEGER PRIMARY KEY,
                                name TEXT UNIQUE)''')
        self.db_conn.commit()




    
    def databaseErstellen(self, name):
        self.db_cursor.execute("SELECT id FROM subjects WHERE name = ?", (name,))
        result = self.db_cursor.fetchone()

        if result:
            print("This course is already registered.")
        else:
            self.db_cursor.execute("INSERT INTO subjects (id, name) VALUES (?, ?)", 
                                   (self.id, name))
            self.db_conn.commit()
            print("Course has been saved.")
        

