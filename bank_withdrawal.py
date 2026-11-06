
# day09_advanced_bank.py

# 1. Initial balance
balance = 5000

# 2. Bank operations
def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        balance += amount
        print("Deposit successful!")
        print("Updated balance:", balance)

    except ValueError as error:
        print("Transaction failed:", error)


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > balance:
            raise ValueError("Insufficient balance.")

        balance -= amount

        print("Withdrawal successful!")
        print("Remaining balance:", balance)

    except ValueError as error:
        print("Transaction failed:", error)


def check_balance():
    print("Current balance:", balance)


# 3. Main banking system
while True:

    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
