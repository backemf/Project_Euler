"""
Euler problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
import time

with open('p67.txt','r') as f:
    triangle = f.read()

triangle_array = [[int(n) for n in line.split()] 
		   for line in triangle.split('\n')[:-1]]

##Recursive:
#def max_path(tr):
#
#    if len(tr) == 1: 
#        return tr[0][0]
#
#    else:
#        return sum([ tr[0][0], 
#                     max( max_path( [ line[1:] for line in tr[1:] ] ),
#                          max_path( [ line[:-1] for line in tr[1:] ] ) 
#                         )
#                   ])

#Iterative
def max_path(tr):
    for row in range(len(tr)-2,-1,-1):
        for col in range(0,len(tr[row]),1):
            tr[row][col] += max(tr[row+1][col], tr[row+1][col+1] )
    return 0

start = time.time()
max_path(triangle_array)
max_sum=triangle_array[0][0]
stop = time.time() - start

print("Answer = {0}".format(max_sum))
print("Elapsed time: {0:.6f}".format(stop))
