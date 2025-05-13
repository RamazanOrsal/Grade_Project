import sqlite3
import teacher_mod
import student_mod


teacher_mod=teacher_mod.Teacher()
student_mod=student_mod.Student()

def mainMenu():
    while True:
        islem=int(input('For teacher enter 1,\nFor student enter 2,\nFor exit enter anything else.'))
        if islem==1:
            teacher_mod.whichPart()
        elif islem==2:
            student_mod.whichPart()
        else:
            break

mainMenu()


