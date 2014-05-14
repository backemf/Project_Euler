"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import time

tic=time.time()

triplets = [ ((a,b,1000-(a+b)) for b in range(a+1,501-a)) for a in range(1,333) ]

print(triplets[0])

for series in triplets:
    for trip in series:
        print(trip)

prod = 0

tac=time.time()-tic

print("Answer = {0}".format(prod))
print("Elapsed time: {0}".format(tac))
