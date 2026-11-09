
# Exception Handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result:", result)

finally:
    print("Program completed.")

