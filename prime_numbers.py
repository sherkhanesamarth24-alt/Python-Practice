# Prime numbers: check a number, list primes up to N, and find prime factors


def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes_up_to(limit):
    """Return a list of all primes from 2 to limit."""
    return [num for num in range(2, limit + 1) if is_prime(num)]


def prime_factors(n):
    """Return the prime factors of n as a list."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


def main():
    try:
        num = int(input("Enter a number: "))

        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

        if num >= 2:
            print(f"Prime factors of {num}: {prime_factors(num)}")

        limit = int(input("\nList all primes up to: "))
        print(f"Primes up to {limit}: {primes_up_to(limit)}")

    except ValueError:
        print("Please enter a valid whole number")


if __name__ == "__main__":
    main()
