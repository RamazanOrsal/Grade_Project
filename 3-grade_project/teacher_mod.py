import random
import kontrol
import sqlite3
import subject
import notes

subject=subject.Subjects()
note=notes.Notes()


class Teacher():
    def __init__(self,name='',surname='',birthday='',email='',id='',passwort='' , subject=''  ):
        self.name=name
        self.surname=surname
        self.birthday=birthday
        self.email=email
        self.id=random.randint(10**9, 10**10-1)
        self.passwort=passwort
        self.subject=subject
        self.db_conn=kontrol.get_db_connection()
        self.db_cursor=self.db_conn.cursor()
        self.create_table()
        



    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    surname TEXT,
                                    email TEXT UNIQUE,
                                    passwort TEXT,
                                    birthday TEXT,
                                    subject TEXT)''')
        self.db_conn.commit()



    def databaseErstellen(self):

        try:
            self.db_cursor.execute("INSERT INTO teacher (id, name, surname, email, passwort, birthday, subject) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                    (self.id, self.name, self.surname, self.email, self.passwort, self.birthday, self.subject))
            self.db_conn.commit()
            print(f'Teacher is made. Teacher {self.name} {self.surname}, id: {self.id} and password: {self.passwort} ')
            self.whichPart()
        except sqlite3.IntegrityError:
            print("Error: This email is already used!")

    
    

    def databaseCheck(self, email, passwort):

        self.db_cursor.execute("SELECT * FROM teacher WHERE email=? AND passwort=?", (email, passwort))
        result = self.db_cursor.fetchone()
        self.db_cursor.execute("SELECT * FROM subjects WHERE name=?", (result['subject'],))
        subject_id = self.db_cursor.fetchone()
        self.teacherCheck(result,subject_id[0])
        



    def teacherCheck(self, result, subject_id):
        while True:
            if result:
                print("You have successfully logged in. What would you like to do next?")
                self.whichAction(subject_id)
        
            else:
                print("Login was unsuccessful. You are being redirected to the main menu.")
                self.whichPart()
                break




    def teacherLogin(self):
        email=input('Email:')
        passwort=input('Passwort:')
        self.databaseCheck(email, passwort)



    def teacherErstellen(self):
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

        self.subject=input('Subject:')

        subject.databaseErstellen(self.subject)
                          
        self.databaseErstellen()
    


    def whichAction(self,subject_id):

        islem=int(input('For new note registration enter 1.\nFor calculate average und given letter grade 2.\nFor looking students notes 3.'))
        if islem==1:
            note.newnoteRegistration(subject_id)


        elif islem==2:
            while True:
                try:
                    note.averageCalculate(subject_id)
                    break
                except Exception as e:
                    print(f"Fehler: {e}")
                    self.whichAction(subject_id)

        elif islem == 3:

            note.lookingNotes(subject_id)

        else:
            print('Please enter valid number.')
            self.whichAction()   





    def whichPart(self):
        while True:
            islem=int(input('For new registration enter 1.\nFor enterance enter 2.\nFor exit enter anything else.'))
            if islem==1:
                self.teacherErstellen()
            elif islem==2:
                self.teacherLogin()
            else:
                break
