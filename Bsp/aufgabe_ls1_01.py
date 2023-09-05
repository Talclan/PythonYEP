while True:
    operator = input("Operator (+, -, *, /): ")

    num1 = float(input("Geben Sie die erste Zahl ein: "))
    num2 = float(input("Geben Sie die zweite Zahl ein: "))

    if operator == '+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    if operator == '/':
        result = num1 / num2

    print("Ergebnis:", result)



