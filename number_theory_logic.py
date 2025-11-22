def is_palindrome(n):
    rev_n = 0
    temp = n
    
    if n < 0:
        return False

    while temp > 0:
        d = temp % 10
        rev_n = (rev_n * 10) + d
        temp = temp // 10

    if rev_n == n:
        return True
    
    return False

def is_armstrong_number(n):
    total = 0
    temp = n
    
    if n < 0:
        return False

    while temp > 0:
        d = temp % 10
        total = total + (d * d * d)
        temp = temp // 10
        
    if total == n:
        return True
    
    return False

def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def generate_fibonacci_sequence(count):
    if count <= 0:
        return []
    
    fib_list = []
    a = 0
    b = 1
    
    if count >= 1:
        fib_list.append(a)
    if count >= 2:
        fib_list.append(b)
        
    for _ in range(2, count):
        c = a + b
        fib_list.append(c)
        a = b
        b = c
        
    return fib_list

def generate_primes_up_to(max_val):
    prime_nums = []
    for i in range(2, max_val + 1):
        found_factor = False
        
        # A common optimization
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                found_factor = True
                break
        
        if not found_factor:
            prime_nums.append(i)
            
    return prime_nums

def calculate_prime_factorization(n):
    factors = {}
    num_left = n
    d = 2
    
    while num_left > 1:
        if num_left % d == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] = factors[d] + 1
            num_left = num_left // d
        else:
            d = d + 1
            
    return factors