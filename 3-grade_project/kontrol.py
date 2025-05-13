import re
from datetime import datetime
import sqlite3

turkce_karakter = r'[üÜöÖçÇğĞşŞıİ]'
def check_password(psw):
    if len(psw)<8 :
        raise Exception(" Paralo en az 8 karakter olmalidir.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola kücük harf icermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf icermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam icermelidir.")
    elif not re.search("[^a-zA-Z0-9]", psw): 
        raise Exception("Parola alpha numaric karakter icermelidir.")
    elif re.search(r'\s', psw):
        raise Exception("Parola bosluk icermemelidir.")
    elif re.search(turkce_karakter,psw):
        raise Exception("Parola türkce karakter icermemelidir.")
    return psw
    


def emailÜberprüft(email):
    muster = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(muster, email):
        raise Exception("Lütfen gecerli bir email giriniz.")
    return email
    
    


def geburtsdatumÜberprüft(geburtsdatum):
    while True:
        try:    
            # GG.AA.YYYY formatını datetime objesine çevir
            date_obj = datetime.strptime(geburtsdatum, "%d.%m.%Y")
            # YYYY-MM-DD formatında string'e çevir
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Bitte geben Sie ein gültiges Datumsformat ein. Beispiel: 25.12.1995")

            

def get_db_connection():
    db_conn=sqlite3.connect("Punkte.sqlite")
    db_conn.row_factory=sqlite3.Row
    return db_conn