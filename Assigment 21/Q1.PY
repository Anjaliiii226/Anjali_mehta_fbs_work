def calculator():
    try:
        # Taking first number
        num1 = float(input("Enter first number: "))
        
        # Taking second number
        num2 = float(input("Enter second number: "))
        
    except ValueError:
        print("❌ Invalid Number! Please enter a valid numeric value.")
        return  # Stop execution after error

    # Taking operator
    operator = input("Enter operator (+, -, *, /): ")

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            # Check division by zero
            result = num1 / num2
        else:
            raise Exception("Invalid Operator")

        print("Result:", result)

    except ZeroDivisionError:
        print("❌ Error: Division by Zero is not allowed.")
    except Exception as e:
        print(f"❌ {e}: Please enter only +, -, *, /")

# Run the calculator
calculator()
