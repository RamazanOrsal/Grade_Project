# 🎓 Grade Project

Dieses Projekt ist ein modulares Python-System, das Lehrkräften ermöglicht, Schülernoten einzugeben, Durchschnittswerte zu berechnen, Analysen durchzuführen und Noten zu klassifizieren.

## 🔧 Funktionen

- Abrufen von Schülerdaten aus der Datenbank
- Noteneingabe durch Lehrkräfte
- Berechnung des Gesamtdurchschnitts
- Analyse der höchsten und niedrigsten Noten
- Klassifizierung der Noten nach Buchstabensystem (A, B, C ...)
- Modulare Struktur für einfache Weiterentwicklung und Wartung

  
# 🛠️ Verwendete Technologien
-**Programmiersprache**: Python
-**Datenbank**: SQLite
-**Bibliotheken**: sqlite3


# 📂 Projektstruktur
```bash
Grade_Project/
├── db_operations.py       # Datenbankverbindung und SQL-Abfragen
├── grade_entry.py         # Noteneingabemaske für Lehrkräfte
├── grade_analysis.py      # Analyse und Klassifizierung der Noten
├── main.py                # Einstiegspunkt der Anwendung
├── student_fetcher.py     # Abrufen von Schülerinformationen
├── utils.py               # Hilfsfunktionen
└── README.md              # Projektdokumentation
```



## 🚀 Starten des Projekts

1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/RamazanOrsal/Grade_Project.git
   cd Grade_Project

2.Führen Sie das Hauptskript aus:
  python main.py


#  ✨ Warum dieses Projekt?

Im Gegensatz zu anderen Projekten ist dieses System:
besser lesbar und erweiterbar durch klare Struktur
nach dem Prinzip „Single Responsibility“ aufgebaut – jede Datei erfüllt eine bestimmte Aufgabe
durch die modulare Bauweise leichter zu testen und zu warten

