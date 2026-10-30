# Bank Withdrawal with Exception Handling

balance = 5000

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
