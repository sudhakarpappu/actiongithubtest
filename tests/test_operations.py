import src.math_operation as s
def test_lcm():
    assert s.lcm(4, 6) == 12
    assert s.lcm(0, 5) == 0
    assert s.lcm(7, 3) == 21
    assert s.lcm(-4, 6) == 12
    assert s.lcm(0, 0) == 0
def test_is_prime():
    assert s.is_prime(2) == True
    assert s.is_prime(3) == True
    assert s.is_prime(4) == False
    assert s.is_prime(17) == True
    assert s.is_prime(1) == False
    assert s.is_prime(-5) == False

def test_fibonacci():
    assert s.fibonacci(0) == [0]
    assert s.fibonacci(1) == [0, 1]
    assert s.fibonacci(5) == [0, 1, 1, 2, 3]
    assert s.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]

def test_average():
    assert s.average([1, 2, 3, 4, 5]) == 3.0
    assert s.average([10, 20, 30]) == 20.0
    assert s.average([]) == 0
    assert s.average([5]) == 5.0

def test_median(): 
    assert s.median([1, 2, 3, 4, 5]) == 3.0
    assert s.median([1, 2, 3, 4]) == 2.5
    assert s.median([10, 20, 30]) == 20.0
    assert s.median([]) == 0
    assert s.median([5]) == 5.0
def test_mode():    
    assert s.mode([1, 2, 2, 3, 4]) == 2
    assert s.mode([1, 1, 2, 2, 3]) == 1
    assert s.mode([1, 2, 3]) == 0
    assert s.mode([]) == 0
    assert s.mode([5]) == 5
def test_factorial():
    assert s.factorial(0) == 1
    assert s.factorial(1) == 1
    assert s.factorial(5) == 120
    assert s.factorial(10) == 3628800

def test_gcd():
    assert s.gcd(48, 18) == 6
    assert s.gcd(0, 5) == 5
    assert s.gcd(7, 3) == 1
    assert s.gcd(-4, 6) == 2
    assert s.gcd(0, 0) == 0

def test_sqrt():
    assert s.sqrt(4) == 2
    assert s.sqrt(9) == 3
    assert s.sqrt(0) == 0
    assert s.sqrt(2) == 2 ** 0.5
def test_pow():
    assert s.pow(2, 3) == 8
    assert s.pow(5, 0) == 1
    assert s.pow(0, 5) == 0
    assert s.pow(3, -2) == 1 / 9
    assert s.pow(-2, 3) == -8
def test_mod():
    assert s.mod(5, 2) == 1
    assert s.mod(10, 5) == 0
    assert s.mod(7, 3) == 1
    assert s.mod(0, 1) == 0
    assert s.mod(5, 0) == 0
def test_div():
    assert s.div(10, 2) == 5
    assert s.div(5, 0) == 0

    assert s.div(0, 5) == 0
    assert s.div(9, 3) == 3

def test_mul():
    assert s.mul(2, 3) == 6
    assert s.mul(0, 5) == 0
    assert s.mul(-2, 3) == -6
    assert s.mul(2, -3) == -6
    assert s.mul(0, 0) == 0
def test_sub():
    assert s.sub(5, 3) == 2
    assert s.sub(0, 5) == -5
    assert s.sub(3, 3) == 0
    assert s.sub(-2, -3) == 1
    assert s.sub(0, 0) == 0    

def test_add():
    assert s.add(2, 3) == 5
    assert s.add(0, 5) == 5
    assert s.add(-2, 3) == 1
    assert s.add(2, -3) == -1
    assert s.add(0, 0) == 0

