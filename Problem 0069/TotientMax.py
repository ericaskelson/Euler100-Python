# This is trickier. I think that I can maximize n/phi(n) by making some sort of supercomposite number
# I'll use a simple implementation for phi, and just try to narrow down my search space

from configparser import MAX_INTERPOLATION_DEPTH
import math

def relatively_prime(a,b):
    for d in range(2,(a if a<b else b)+1):
        if a%d == 0 and b%d == 0: return False
    return True

def phi(n):
    t = 1
    if n == 2: return 1
    for i in range(2,n):
        temp=relatively_prime(n,i)
        if temp: t += 1
    return t

def primes_up_to(n):
    primes = [2]
    for i in range(3,n,2):
        s=math.floor(math.sqrt(i)+1)
        prime = True
        for p in primes: 
            if i%p == 0: 
                prime = False
                break
            if p>s: break
        if prime: 
            primes.append(i)
    return primes

toCheck = 1000
target = 1*(10**5)

primelist = primes_up_to(toCheck)

j=10000
print("About to check phi speed")
print("Phi(",j,") =",phi(j))

currProd = 1
currRatio = 1
maxProd = 1
maxRatio = 1

# for i in range(toCheck):
#     currProd = currProd*primelist[i]
#     print("i =",i,"i'th prime =",primelist[i],"current product =",currProd)
#     if currProd>target: break
#     currRatio = currProd/phi(currProd)
#     if currRatio > maxRatio:
#         maxProd = currProd
#         maxRatio = currRatio
#         print("New highest ratio with n =",currProd,"and n/phi(n) ratio of",currRatio)

# TOOO SLOOOOW