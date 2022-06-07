# Problem 700 - Eulercoin
# https://projecteuler.net/problem=700
#
# Seems easy enough! Just need to iterate for a good while, and
# stop once we hit 1. Of course, "a good while" is the operative
# phrase.

from operator import countOf


num = 1504170715041707
den = 4503599627370517

sumOfCoins = 0
countOfCoins = 0
smallestCoin = den

i = 1

while (smallestCoin != 1):
    cand = (num*i)%den
    if cand < smallestCoin:
        countOfCoins += 1
        sumOfCoins += cand
        smallestCoin = cand
        print("Coin found at i =",i,"Total of",countOfCoins,"coins found for a sum of",sumOfCoins,"New coin is:",cand)
    i += 1

# For reference: prime factors of numerator: [17, 1249, 12043, 5882353]
# And the denominator/modulo factor is prime

# Next steps: find n where num*n == 1? Understand Fermat's little theorem? 
# What is the trick? I technically could just leave it to run overnight, but that's... distateful