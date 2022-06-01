# The task is to find the 10,001st prime number. We should start with brute force, I think?

Nth = 10001

import math

def is_prime(n):
    if n==1: return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0: return False
    return True

i = 2
k = 1

while k < Nth:
    i += 1
    if is_prime(i): 
        k += 1
        print("Prime number",k,"is",i)

print("And the",Nth,"prime is",i)

