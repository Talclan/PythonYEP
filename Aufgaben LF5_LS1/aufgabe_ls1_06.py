# Dateipfad zur Textdatei auf dem Desktop festlegen
desktop_pfad = r"C:\Users\Ozan\Desktop\sad.txt"  # Du kannst hier den Pfad entsprechend deinem System anpassen

try:
    # Textdatei öffnen und den Inhalt ausgeben
    with open(desktop_pfad, 'r') as datei:
        inhalt = datei.read()
        print("Dateiinhalt:")
        print(inhalt)
except FileNotFoundError:
    print(f"Die Datei '{desktop_pfad}' wurde nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {str(e)}")
