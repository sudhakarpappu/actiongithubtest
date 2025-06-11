import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 0  # or raise ValueError("Cannot divide by zero")
    return a / b

def mod(a, b):
    if b == 0:
        return 0  # or raise ValueError("Cannot mod by zero")
    return a % b

def pow(a, b):
    return a ** b

def sqrt(a):
    return a ** 0.5

def factorial(n):   
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return [0]
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return min(modes)  # return smallest if multiple modes

def variance(numbers):
    if not numbers:
        return 0
    mean = average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5

def permutation(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def logarithm(x, base=10):
    if x <= 0 or base <= 1:
        raise ValueError("x must be positive and base must be greater than 1")
    return math.log(x, base)
