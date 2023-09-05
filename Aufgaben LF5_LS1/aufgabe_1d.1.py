import math         # Mathe Bibliothek die du vorher einfügen musst um z.B. um Pi einzufügen (math.pi)

while True:

    print("Kreisberechnungen")
    print("-----------------")

    choice = (input("Möchten Sie die 'Oberfläche' berechnen oder das 'Volumen'? :  "))

    if choice == "Oberfläche":
        # Berechnung der Oberfläche eines Kreises
        radius = float(input("Geben Sie den Radius des Kreises ein: "))
        oberflaeche = math.pi * radius ** 2
        oberflaeche = round(oberflaeche, 3) # rundet das Ergebnis auf 3 Nachkommastellen
        print("Oberfläche:", oberflaeche)
       
    
    elif choice == "Volumen":
        # Berechnung des Volumens einer Kugel mit gegebenem Radius
        radius = float(input("Geben Sie den Radius des Kreises ein: "))
        volumen = 4/3 * math.pi * radius ** 3
        volumen = round(volumen, 3) # rundet das Ergebnis auf 3 Nachkommastellen
        print("Volumen:", volumen)
        
    
    else:
        print("Ungültige Eingabe")

    

    

    
    
    
