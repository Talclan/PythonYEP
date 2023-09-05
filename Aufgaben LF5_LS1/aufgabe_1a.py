while True:
    print("aufgabe_ls1_01")
    print("")

    a = float(input("a:"))
    b = float(input("b:"))

    print("")

    Operator = input("Wähle eine Operator aus + - * /:") #OP = Operator

    if Operator == "+":
        e = a + b           # A = Addition
    elif Operator == "-":
        e = a - b           # S = Subtraktion
    elif Operator == "*":
        e = a * b           # M = Multiplikation
    elif Operator == "/":
        e = a / b           # D = Division
    
    else:
        print("Ungültiger Operator")


    print("Ergebnis:", e )
    print("---------------")
    print("")
    


