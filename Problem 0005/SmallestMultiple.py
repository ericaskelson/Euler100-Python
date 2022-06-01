# Find the smallest positive number evenly divisible by all numbers from 1 to 20
# Clean way is to get the union of the unique decompositions of everything from 1 to 20

import math

n=100

factors = []

for i in range(2,n+1):
    for fact in factors:
        if i%fact == 0: i = i//fact
    factors.append(i)

print("Smallest positive integer divisible by all numbers from 1 to",n,"is",math.prod(factors))