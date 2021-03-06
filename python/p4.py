"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import combinations_with_replacement as combs

def is_palin(n):
    return str(n) == str(n)[::-1]

products = (x*y for x,y in combs(range(100,1000),2))

print( max (x for x in products if is_palin(x)  ) )








