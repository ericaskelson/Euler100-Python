# Problem 3 - Largest prime factor
# https://projecteuler.net/problem=3
# 
# Goal is to find the largest prime factor of the number 600851475143.
# First things first, let's see just how horribly slow it would be for us to take the naive
# approach

import math

def is_prime(n):
    if n==1: return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0: return False
    return True

# To double check...
print(is_prime(5))

# Not prime, need to keep going
# for i in range(10,1,-2):
#     if 600851475143%i==0 and is_prime(i):
#         print("Largest prime factor is",i)
#         break

# Horrifyingly slow, would have to run over night. Let's... be cleverer?

toDecompose=600851475143
residue=toDecompose
highestPrimeFactor=1

while not is_prime(residue):
    for i in range(2,math.ceil(math.sqrt(residue))+1):
        if residue%i==0:
            if i>highestPrimeFactor: highestPrimeFactor=i
            print("Residue of",residue,"divisible by",i,"Highest prime factor seen is",highestPrimeFactor)
            residue=residue//i
            break

if residue > highestPrimeFactor: highestPrimeFactor = residue

print("Final residue is",residue)
print("Final highest prime factor of",toDecompose,"is",highestPrimeFactor)