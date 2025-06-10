import math
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b        
def mod(a,b):
    return a % b
def pow(a,b):
    return a ** b
def sqrt(a):
    return a ** 0.5
def factorial(n):   
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
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
    return modes if len(modes) > 1 else modes[0]
def variance(numbers):
    if not numbers:
        return 0
    mean = average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)
def standard_deviation(numbers):
    if not numbers:
        return 0
    return variance(numbers) ** 0.5
def permutation(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r) 
def combination(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))
def logarithm(x, base=10):
    if x <= 0 or base <= 1:
        raise ValueError("x must be positive and base must be greater than 1")
    return math.log(x, base)
