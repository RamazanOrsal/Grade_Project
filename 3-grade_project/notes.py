import kontrol
import teacher_mod
import student_mod









class Notes():
    def __init__(self, midterm1='', midterm2='', final='', lettergrade='' ):
        self.midterm1=midterm1
        self.midterm2=midterm2
        self.final=final
        self.lettergrade=lettergrade
        self.lettergradelist=[]
        self.lettergradedict={}
        self.db_conn=kontrol.get_db_connection()
        self.db_cursor=self.db_conn.cursor()
        self.create_table()
        
    
    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    student_id TEXT,
                                    subject_id TEXT,
                                    midterm1 TEXT,
                                    midterm2 TEXT,
                                    final TEXT,
                                    letter_grade TEXT,
                                    FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE,
                                    FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE CASCADE)''')
        self.db_conn.commit()
    

    def newdataregistration(self, student_id, subject_id):
        self.db_cursor.execute("SELECT * FROM notes WHERE student_id = ? AND subject_id = ?", (student_id, subject_id))
        existing = self.db_cursor.fetchone()

        if existing:
            if self.midterm1 is not None:
                self.db_cursor.execute(
                "UPDATE notes SET midterm1 = ? WHERE student_id = ? AND subject_id = ?",
                (self.midterm1, student_id, subject_id)
                )
            if self.midterm2 is not None:
                self.db_cursor.execute(
                    "UPDATE notes SET midterm2 = ? WHERE student_id = ? AND subject_id = ?",
                    (self.midterm2, student_id, subject_id)
                )
            if self.final is not None:
                self.db_cursor.execute(
                    "UPDATE notes SET final = ? WHERE student_id = ? AND subject_id = ?",
                    (self.final, student_id, subject_id)
                )
            self.db_conn.commit()
        else:
            self.db_cursor.execute("""
                INSERT INTO notes (student_id, subject_id, midterm1, midterm2, final)
                VALUES (?, ?, ?, ?, ?)
            """,(
                student_id,
                subject_id,
                self.midterm1 if self.midterm1 is not None else None,
                self.midterm2 if self.midterm2 is not None else None,
                self.final if self.final is not None else None
            ))
        
            self.db_conn.commit()


    def newnoteRegistration(self,subject_id):

        self.db_cursor.execute("SELECT * FROM student")
        student_check = self.db_cursor.fetchall()

        for row in student_check:
            self.midterm1=None
            self.midterm2=None
            self.final=None
            
            islem=int(input(f'Which grade are you entering for the student named {row['name']} {row['surname']}?:\nFor 1.Midterm enter 1\nFor 2. Midterm enter 2.\nFor Final enter 3.\nFor another student 4.'))
            if islem == 1:
                self.midterm1=int(input('Enter the 1st midterm grade.'))
            elif islem==2:
                self.midterm2=int(input('Enter the 2st midterm grade.'))
            elif islem==3: 
                self.final=int(input('Enter the final grade.'))
            elif islem==4:
                pass
            self.newdataregistration(row['id'], subject_id)


    def lookingNotes(self, s_id):

        self.db_cursor.execute("SELECT * FROM student")
        student_check = self.db_cursor.fetchall()
        for row in student_check:
            self.db_cursor.execute("SELECT midterm1, midterm2, final, letter_grade from notes WHERE subject_id = ? AND student_id=?", (s_id, row[0]))
            all_notes=self.db_cursor.fetchone()
            all_notes= dict(all_notes)
          
            if not all_notes:
                print(f"{row['name']} {row['surname']} isimli öğrenciye ait hiçbir not girilmemiştir.\n")
                continue
            print(f"Grades of the student named {row['name']} {row['surname']}:")
            print(f"Midterm 1: {all_notes.get('midterm1', 'Not entered yet') if all_notes.get('midterm1') is not None else 'Not entered yet'}")
            print(f"Midterm 2: {all_notes.get('midterm2', 'Not entered yet') if all_notes.get('midterm2') is not None else 'Not entered yet'}")
            print(f"Final: {all_notes.get('final', 'Not entered yet') if all_notes.get('final') is not None else 'Not entered yet'}")
            print(f"Letter Grade: {all_notes.get('letter_grade', 'Letter Grade not entered yet')if all_notes.get('letter_grade') is not None else 'Not entered yet'}\n")




    def averageCalculate(self, s_id):
        self.db_cursor.execute("SELECT * from notes WHERE subject_id=?", (s_id,))
        result=self.db_cursor.fetchall()



        for row in result:
            
            try:
                self.lettergradedict={}
                average_cal=0.3*float(row['midterm1'])+0.3*float(row['midterm2'])+0.4*float(row['final'])
                print(average_cal)
                self.lettergradeCalculate(s_id, average_cal, row['student_id'])
                    
            except Exception:
                print(dict(row))
                raise Exception(f"Grades are missing for student with ID {row['student_id']}")
            
        self.lettergradeRegistration()   
    
    
    def lettergradeCalculate(self, subject_id, averagenote, student_id):
        if averagenote<40 :
            self.lettergrade='FF'
        elif 40<=averagenote<55:
            self.lettergrade='DD'
        elif 55<=averagenote<60:
            self.lettergrade='DC'
        elif 60<=averagenote<70:
            self.lettergrade='CC'
        elif 70<=averagenote<80:
            self.lettergrade='CB'
        elif 80<=averagenote<85:
            self.lettergrade='BB'
        elif 85<=averagenote<90:
            self.lettergrade='BA'
        elif 90<=averagenote<=100:
            self.lettergrade='AA'
        self.lettergradedict['subject_id']=subject_id
        self.lettergradedict['letter_grade']=self.lettergrade
        self.lettergradedict['student_id']=student_id
        self.lettergradelist.append(self.lettergradedict)
        print(self.lettergradelist)


    def lettergradeRegistration(self):

        for row in self.lettergradelist:
            self.db_cursor.execute(
                "UPDATE notes SET letter_grade=? WHERE student_id = ? AND subject_id = ?", 
                (row['letter_grade'], row['student_id'], row['subject_id']))
            self.db_conn.commit()




                
                    
                
            


                


                    




        
            
            
            
            
            
