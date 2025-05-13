import random
import kontrol
import sqlite3


class Student():
    def __init__(self,name='',surname='',birthday='',email='',id='',passwort=''):
        self.name=name
        self.surname=surname
        self.birthday=birthday
        self.email=email
        self.id=random.randint(10**9, 10**10-1)
        self.passwort=passwort
        self.db_conn=kontrol.get_db_connection()
        self.db_cursor=self.db_conn.cursor()
        self.create_table()
        



    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    surname TEXT,
                                    email TEXT UNIQUE,
                                    passwort TEXT,
                                    birthday TEXT)''')
        self.db_conn.commit()


    def databaseErstellen(self):

        try:
            self.db_cursor.execute("INSERT INTO student (id, name, surname, email, passwort, birthday) VALUES (?, ?, ?, ?, ?, ?)", 
                                    (self.id, self.name, self.surname, self.email, self.passwort, self.birthday))
            self.db_conn.commit()
            print(f'Student is made. Student {self.name} {self.surname}, id: {self.id} and password: {self.passwort} ')

        except sqlite3.IntegrityError:
            print("Error: This email is already used!")

    


    def studentErstellen(self):
        self.name=input('Name:')
        self.surname=input('Surname:')
        
        while True:
            try:
                eMail=input('Email:')
                self.email=kontrol.emailÜberprüft(eMail)
                break
            except:
                print("Please enter a valid email address. ")

        while True:
            try:
                birthday=input('Birthday(DD.MM.YYYY):')
                self.birthday=kontrol.geburtsdatumÜberprüft(birthday)
                break
            except ValueError as e:
                print(f"Fehler: {e}")

        while True:
            try:
                passwort=input('Passwort:')
                self.passwort=kontrol.check_password(passwort)
                break
            except:
                print("Please enter a valid password. It must be at least 8 characters long\n and include at least one uppercase letter, one lowercase letter,\n one number, and one special character.Example: Aa.123753 ")
        self.databaseErstellen()
    
      

    def databaseCheck(self, email, passwort):

        self.db_cursor.execute("SELECT id FROM student WHERE email=? AND passwort=?", (email, passwort))
        id = self.db_cursor.fetchone()
        self.studentCheck(id)
        



    def studentCheck(self, id):
        
        if id:
            print("You have successfully logged in. What would you like to do next?")
            self.showNotes(id)
        
        else:
            print("Login was unsuccessful. You are being redirected to the main menu.")
            self.whichPart()



    def studentLogin(self):
        email=input('Email:')
        passwort=input('Passwort:')
        self.databaseCheck(email, passwort)


    def whichPart(self):
        while True:
            islem=int(input('For new registration enter 1.\nFor enterance enter 2.\nFor exit enter anything else.'))
            if islem==1:
                self.studentErstellen()
            elif islem==2:
                self.studentLogin()
            else:
                break


    def showNotes(self, id):
        self.db_cursor.execute("SELECT * FROM subjects")
        subject_check = self.db_cursor.fetchall()
        subjects_ids=[row['id'] for row in subject_check]
        subject_dict = {subject['id']: subject['name'] for subject in subject_check}

        self.db_cursor.execute("SELECT * FROM notes WHERE student_id=?", (id))
        notes_check = self.db_cursor.fetchall()
        
        for i in subjects_ids:
            for row in notes_check:
                if i == int(row['subject_id']):
                    print(f'Notes of {subject_dict.get(i)}')
                    print(f"Midterm 1: {row['midterm1'] if row['midterm1'] is not None else 'Not entered yet'}")
                    print(f"Midterm 2: {row['midterm2'] if row['midterm2'] is not None else 'Not entered yet'}")
                    print(f"Final: {row['final'] if row['final'] is not None else 'Not entered yet'}")
                    print(f"Letter Grade: {row['letter_grade'] if row['letter_grade'] is not None else 'Not entered yet'}\n")