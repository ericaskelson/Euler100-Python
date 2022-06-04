# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12
# 
# As usual, let's try the dumb approach first

import math
import itertools

def tri(n): return n*(n+1)//2

def countFactors(n):
    sum = 1
    for i in range(1,n):
        sum += 0 if n%i != 0 else 1
    return sum

maxTr = 0
maxDivisors = 0

# for i in range(1,1000):
#     tr = tri(i)
#     factors = countFactors(tr)
#     if factors > max:
#         max = factors
#         print("New max factors at triangle number",i,"which is",tr,"and has",factors,"divisors")

# Nope, way too slow, unfortunately. Maybe if we make the factor counter faster

factDict = {1: {1}}

def listFactors(n):
    if n in factDict: return factDict[n]
    factors = {1}
    for i in range(1,n):
        if n%i == 0: factors = factors | {i} | listFactors(i)
    factors.add(n)
    factDict[n] = factors
    return factors

# for i in range(1000):
#     print("Integer",i+1,"is divisible by this many divisors:",len(listFactors(i+1)))

# i = 0

# while maxDivisors < 500:
#     i += 1
#     tr = tri(i)
#     if i%2 == 0:
#         factors = listFactors(
#     factors = len(listFactors(tr))
#     if factors > maxDivisors:
#         maxTr = tr
#         maxDivisors = factors
#         print("New max factors at triangle number",i,"which is",tr,"and has",factors,"divisors")
# STILL TOO SLOW AAAAAAA

# Okay. Forget listing all factors - we list PRIME factors, memoize, split, then recalculate all factors. Maybe faster? Who knows.

primeFacts = {2: [2]}

def listPrimeFactors(n):
    factors = []
    input = n
    while n != 1:
        cap = math.ceil(math.sqrt(n))+1
        for i in range(2,cap+1):
            if i == cap:
                factors.append(n)
                n = 1
            if n%i == 0:
                factors.append(i)
                n = n//i
                break
        if n in primeFacts:
            factors = factors + primeFacts[n]
            n = 1
    primeFacts[input] = factors
    return factors

def listAllFactors(primeFactorList):
    allFactors = set()
    for i in range(1,len(primeFactorList)+1):
        allFactors = allFactors | {math.prod(x) for x in itertools.combinations(primeFactorList,i)}
    return allFactors

maxFactors = 0
maxFactorSet = {}

i = 0

while maxFactors < 500:
    i += 1
    tr = tri(i)
    if i%2 == 0:
        primeFactors = listPrimeFactors(i//2) + listPrimeFactors(i+1)
    else:
        primeFactors = listPrimeFactors(i) + listPrimeFactors((i+1)//2)
    allFactors = listAllFactors(primeFactors)
    if len(allFactors) > maxFactors: 
        maxFactors = len(allFactors)
        print("New biggest factors at triangle number",i,"which is",tr,"and has",maxFactors)

# Ohhhh, man. Okay. Maybe there was a better way, but that worked, and it was fast!

# Well, reading the solution, the obvious thing I missed is that, given a prime factorization you can
# get the number of possible factors by taking the product of the exponents on the primes.