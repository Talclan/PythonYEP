while True:
    print("aufgabe_ls1_02")

    a = float(input("Celsius: "))

    X = input("In welche Richtung möchtest du umwandeln? (C -> Celsius zu Fahrenheit, F -> Fahrenheit zu Celsius): ")

    if X == "C" or X == "c":
        ze = a * 1.8  # ze = Zwischenergebnis
        F = ze + 32   # F = Fahrenheit

        print("Zwischenergebnis:", ze, "°")
        print("Fahrenheit:", F)

    elif X == "F" or X == "f":
        ze = a - 32    # ze = Zwischenergebnis
        C = ze / 1.8   # C = Celsius

        print("Zwischenergebnis:", ze, "°")
        print("Celsius:", C)

    else:
        print("Ungültige Auswahl! Bitte 'C' oder 'F' eingeben.")
