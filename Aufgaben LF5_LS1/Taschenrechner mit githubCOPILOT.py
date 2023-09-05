#Taschenrechner

print("Taschenrechner") #Ausgabe Taschenrechner 
print("Bitte geben Sie die erste Zahl ein:") #Ausgabe Bitte geben Sie die erste Zahl ein:
zahl1 = input() #Eingabe erste Zahl
print("Bitte geben Sie die zweite Zahl ein:") #Ausgabe Bitte geben Sie die zweite Zahl ein: 
zahl2 = input() #Eingabe zweite Zahl
print("Bitte geben Sie die Rechenart ein:") #Ausgabe Bitte geben Sie die Rechenart ein:
rechenart = input() #Eingabe Rechenart
if rechenart == "+": #wenn rechenart = + dann
    print("Ergebnis:") #Ausgabe Ergebnis:
    print(int(zahl1) + int(zahl2)) #Ausgabe Ergebnis
elif rechenart == "-": #wenn rechenart = - dann
    print("Ergebnis:") #Ausgabe Ergebnis:
    print(int(zahl1) - int(zahl2)) #Ausgabe Ergebnis
elif rechenart == "*": #wenn rechenart = * dann
    print("Ergebnis:") #Ausgabe Ergebnis:
    print(int(zahl1) * int(zahl2)) #Ausgabe Ergebnis
elif rechenart == "/": #wenn rechenart = / dann
    print("Ergebnis:") #Ausgabe Ergebnis:
    print(int(zahl1) / int(zahl2)) #Ausgabe Ergebnis
else: #wenn rechenart nicht = +,-,*,/ dann
    print("Falsche Eingabe") #Ausgabe Falsche Eingabe