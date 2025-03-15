def Calculator():
    while True:
        # Gets first number
        while True:
            try:
                Num1 = int(input("Please provide your first number: "))
                break
            except ValueError:
                print("Please provide a valid number.")

        # Gets operation symbol
        while True:
            Symbol = input("Please provide a symbol (+, -, *, /): ")
            if Symbol in ["+", "-", "*", "/"]:
                break
            else:
                print("Invalid symbol! Please use one of: '+, -, *, /'.")

        # Gets second number
        while True:
            try:
                Num2 = int(input("Please provide your second number: "))
                if Symbol == "/" and Num2 == 0:
                    print("Cannot divide by zero! Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Please provide a valid number.")

        # Performs Calculation
        if Symbol == "+":
            result = Num1 + Num2
        elif Symbol == "-":
            result = Num1 - Num2
        elif Symbol == "*":
            result = Num1 * Num2
        elif Symbol == "/":
            result = Num1 / Num2

        print(f"Your result is: {result}")

        # Asks if user wants to continue
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

# Runs the calculator
Calculator()
