import time

start_time = time.time()
sumsquare=0
squaresum=0

for k in range(1,101):
	sumsquare=sumsquare+k**2

for i in range(1,101):
	for j in range(i,i*100+1,i):
		squaresum=squaresum+j



elapsed_time = time.time()- start_time

print "Square of the sum is %d" %(squaresum)
print "Sum of the squares is %d" %(sumsquare)
print "Difference is %d" %(squaresum-sumsquare)
print "Elapsed time is %.3f seconds" %(elapsed_time)

