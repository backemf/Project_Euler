"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time

def enter_divs(N):
    d = dict( zip(range(1,N),[0]*(N-1)) )
    for x in range(1,N//2 + 1):
        for y in range(2*x,N,x):
            d[y] += x
    return d 

def gen_ams(N):
    """Generate amicable numbers < N"""
    d = enter_divs(N)
    for n in range(2,N):
        if d[n] != n and d[n] in d and d[d[n]] == n:
            yield n

start = time.time()
ans = sum(am for am in gen_ams(10000) )
stop = time.time() - start

print("Answer = {0}".format(ans))
print("Elapsed time: {0}".format(stop))
