# Includes a variety of formulas related to primes, to save time

import math
import itertools

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