"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares 
of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.
"""

import time

start_time = time.time()
diff = sum(i * sum(j for j in range(1,101) if j != i) for i in range(1,101))
elapsed_time = time.time()- start_time

print("Answer = {0}".format(diff))
print("Elapsed time is {0:.6f} seconds".format(elapsed_time))

