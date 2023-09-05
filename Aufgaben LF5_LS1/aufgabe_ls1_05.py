"""Aufgabe_ls1_05_orginal - Logische Grundfunktionen (Orginal Version)
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  18.06.2022
    """

while True:
    print("Logische Grundfunktionen")
    print("------------------------")
    print("")
    print("(1) UND-Funktion")
    print("(2) ODER-Funktion")
    print("(3) NICHT-Funktion")
    print("(4) NAND-Funktion")
    print("(5) NOR-Funktion")
    print("(6) aquivalenz-Funktion")
    print("(7) antivalenz-Funktion")
    print("(e) Ende")
    befehl = input("Auswahl: ")

    if befehl == "e":
        print("Logische Grundfunktionen beendet")
        break
    if befehl == "1":
        # UND-Funktion
        print("UND-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = x and y
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    elif befehl == "2":
        # ODER-Funktion
        print("ODER-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = x or y
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    elif befehl == "3":
        # NICHT-Funktion
        print("NICHT-Verknüpfung")
        print("---------------")
        print("")
        print("X  |  Z")
        print("-------+---")
        for x in range(0, 2):
            z = not x
            z = int(z)
            print(str(x) + "  |  " + str(z))
        print("")
    elif befehl == "4":
        # NAND-Funktion
        print("NAND-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = not (x and y)
                z = int(z)
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    elif befehl == "5":
        # NOR-Funktion
        print("NOR-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = not (x or y)
                z = int(z)
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    elif befehl == "6":
        # aquivalenz-Funktion
        print("aquivalenz-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = not (x ^ y)
                z = int(z)
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    elif befehl == "7":
        # antivalenz-Funktion
        print("antivalenz-Verknüpfung")
        print("---------------")
        print("")
        print("X   Y  |  Z")
        print("-------+---")
        for x in range(0, 2):
            for y in range(0, 2):
                z = x ^ y
                z = int(z)
                print(str(x) + "   " + str(y) + "  |  " + str(z))
        print("")
    else:
        print("Unbekannter Befehl: " + str(befehl))
        print("")
        continue
