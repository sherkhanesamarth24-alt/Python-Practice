# Safe Integer Input

while True:
    try:
        number = int(input("Enter an integer: "))
        print("Square:", number ** 2)
        break

    except ValueError:
        print("Invalid input! Try again.")
