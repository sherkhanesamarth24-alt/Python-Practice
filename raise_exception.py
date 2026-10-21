# Raise an Exception

age = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as error:
    print("Error:", error)
