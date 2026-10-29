# Handle List Index Error

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter list index (0-4): "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Index is out of range!")

except ValueError:
    print("Please enter an integer.")
