import time

tic=time.time()

def isPrime(nmb):
	if nmb%2==0 and nmb!=2:
		return False
	for i in range(3,int(nmb**0.5+1),2):
		if nmb%i==0:
			return False
	return True



n=1
i=3    
while(n < 10001):
    if isPrime(i):
        n += 1
    i += 2
    

tac=time.time() - tic

print("Answer = {0}".format(i) )
print("Elapsed time = {0:.3f}".format(tac) )
	
