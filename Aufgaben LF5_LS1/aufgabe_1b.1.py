#Aufgabe1b

while True:
    
    choice = input("Welche Umwandlung möchten Sie vornehmen Celius ---> Fahrenheit oder Fahrenheit ---> Celius? \n (gebe z.B. ein CF für Celisus in Fahrenheit)")

    if choice == "CF":
        Celsius = float(input("Celius ---> Fahrenheit:"))
        Celsius_to_Fahrenheit = Celsius * 1.8 + 32
        print("Ergebnis:", Celsius_to_Fahrenheit)
        
        
    elif choice == "FC":
        Fahrenheit = float(input("Fahrenheit ---> Celsius:"))
        Fahrenheit_to_Celsius = (Fahrenheit - 32) * 5/9
        print("Ergebnis:", Fahrenheit_to_Celsius)

    else:
        print("Ungültige Eingabe!")



    
    