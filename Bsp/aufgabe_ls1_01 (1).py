print("=============Taschenrechner=============")
print("=======================================")

print("Welcher Operator soll verwendet werden?")
operator = input("(+,-,*,/): ")
print("=======================================")
print("Mit welchen beiden Zahlen soll gerechnet werden?")
num1 = float(input("Zahl 1: "))
num2 = float(input("Zahl 2: "))
print("=======================================")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Diesen Operator gibt es nicht!")


print("Das Ergebnis ist: ", result)