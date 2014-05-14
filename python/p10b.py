import time

def sieve(n):
	primes = list(range(n+1))
	max = int(n**0.5)
	
	for i in range(2,max+1):
		if primes[i]:
			primes[2*i::i] = [None] * (n//i - 1)
	
	
	return [i for i in primes[2:] if i]

tic = time.time()
print sum(sieve(2000000))
tac = time.time()-tic
print("Time elapsed: {0}".format(tac))
