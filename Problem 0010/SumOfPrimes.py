# Need to sum all primes below n. Going to try sieve method. Maybe too many?
import math

n = 2*(10**6)
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

print("Found all primes below",n)
print("Total number of primes is",len(primes))
print("Sum of primes is",sum(primes))