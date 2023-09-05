#Fahrenheit in Celsius umrechnen und umgekehrt


print("Fahrenheit in Celsius umrechnen und umgekehrt")
print("Bitte geben Sie die Temperatur ein:")
temperatur = input()
print("Bitte geben Sie die Einheit ein:")
einheit = input()
if einheit == "C":  
    print("Celsius:")
    print(int(temperatur) * 1.8 + 32)
elif einheit == "F":
    print("Fahrenheit:")
    print((int(temperatur) - 32) / 1.8)
else:
    print("Falsche Eingabe")
    