"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import time

def ESieve(N):
    """Sieve of Eratosthenes
    Find all primes < N
    """
    marked=set() 
    for p in xrange(2,N+1,1) :
        if p in marked:
            continue
        for m in xrange(p**2,N+1,p):
            marked.add(m)
        yield p


tic = time.time()
prime_sum = sum(p for p in ESieve(2000000) )
tac = time.time() - tic

print("Answer = {0}".format(prime_sum))
print("Elapsed time: {0}".format(tac))
