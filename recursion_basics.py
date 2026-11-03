# Recursion basics: factorial, fibonacci, sum of digits and power


def factorial(n):
    """Return n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed) using recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    """Return the sum of digits of a number using recursion."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


def power(base, exp):
    """Return base raised to exp (exp >= 0) using recursion."""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def main():
    try:
        num = int(input("Enter a non-negative number: "))

        print(f"\nFactorial of {num} = {factorial(num)}")
        print(f"Fibonacci({num}) = {fibonacci(num)}")
        print(f"Sum of digits of {num} = {sum_of_digits(num)}")
        print(f"2 ^ {num} = {power(2, num)}")

        print("\nFirst 10 Fibonacci numbers:")
        print([fibonacci(i) for i in range(10)])

    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
