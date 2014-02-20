import sys

N=int(sys.argv[1])
largest=1

divs=[]

def isPrime(nmb):
	if nmb%2==0 and nmb!=2:
		return False
	for i in range(3,int(nmb**0.5+1),2):
		if nmb%i==0:
			return False
	return True

if isPrime(N):
	largest=N

for j in range(2,int(N**0.5+1)):
	if N%j==0:
		divs.append(j)
		divs.append(N/j)

for k in divs:
	if isPrime(k):
		largest=k


print largest



			



