"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from itertools import count
import time

start_time = time.time()
s=-1
for i in count(20,20):
    if any(i % x != 0 for x in range(1,21) ):
        continue
    else:
        s = i
        break
elapsed_time = time.time() - start_time

print(s)
print("Elapsed time is {0:.3f} seconds".format(elapsed_time))

