"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def gen_divs(N):
    """Generates uneven divisors"""
    for i in range(1, int(N**0.5+1),2):
        if N % i == 0:
            yield i

def is_prime(n):
    """Returns True if n is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False

    for div in range(3, int(n**0.5+1),2):
        if n % div ==0:
            return False
    else:
        return True


print( max( x for x in gen_divs(600851475143) if is_prime(x) ) )

