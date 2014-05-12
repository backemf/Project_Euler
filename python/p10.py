
def isPrime(nmb):
	if nmb%2==0 and nmb!=2:
		return False
	for i in range(3,int(nmb**0.5+1),2):
		if nmb%i==0:
			return False
	return True
	

L=[2]

for i in range(3,2000000,2):
	if isPrime(i):
		L.append(i)
		
print sum(L)
