while True:
    print("aufgabe_ls1_03")
    
    R1 = float(input("R1:"))
    R2 = float(input("R2:"))

    Rges = 1 / (1/R1 + 1/R2)            # Formel für Parallelschaltung mit zwei Widerständen einliest um Gesamwiderstand auszugeben
    
    print("Rges:", Rges)
    print("---------------")
    print("")
