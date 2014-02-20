L=[]
largest=10001

def isPalin(nr):
	word=str(nr)
	for i in range(len(word)):
		if word[i]!=word[-(i+1)]:
			return False
	return True


for i in range(100,1000):
	for j in range(i,1000):
		L.append(i*j)

for k in L:
	if isPalin(k):
		if k>largest:
			largest=k


print len(L)		
print largest




