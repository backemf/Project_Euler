import time

start_time = time.time()

s=1
k=range(0,500000000,20)
k.remove(0)

for i in k:
	for j in range(1,21):
		if i%j!=0:
			break
	else:
		s=i
		break
elapsed_time = time.time() - start_time

print s
print 'Elapsed time is %.3f seconds' %(elapsed_time)

