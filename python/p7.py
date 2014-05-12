import time
import sys

#Find the Nth prime

N=int(sys.argv[1])
i=0
k=1

def isPrime(nmb):
	if nmb%2==0 and nmb!=2:
		return False
	for i in range(3,int(nmb**0.5+1),2):
		if nmb%i==0:
			return False
	return True
	
while i<N:
	k=k+1
	if isPrime(k):
		i=i+1
	

print k
	
