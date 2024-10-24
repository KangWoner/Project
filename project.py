def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(f"Prime factors of {number} are: {prime_factors(number)}")
