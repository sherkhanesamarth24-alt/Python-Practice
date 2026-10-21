# Safe Calculator with Exception Handling

try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
    else:
        raise ValueError("Invalid operator.")

    print("Result:", result)

except ValueError as error:
    print("Input error:", error)

except ZeroDivisionError as error:
    print("Math error:", error)
