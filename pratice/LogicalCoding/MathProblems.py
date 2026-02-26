from sympy import *


def fibonacci(n):
    prev1 = current = 0
    prev2 = 1
    sequence = [prev1, prev2]

    for _ in range(2, n):
        current = prev1 + prev2
        sequence.append(current)
        prev1 = prev2
        prev2 = current
    print(sequence)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        value = 1
        for i in range(2, n + 1):
            value *= i
        return value
        # return n * factorial(n-1) // same as above but with recursion


def is_prime(n):
    isPrime = True

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    # return isPrime
    return isprime(n)  # using sympy library


fibonacci(10)
print(factorial(5))
print(is_prime(12))
