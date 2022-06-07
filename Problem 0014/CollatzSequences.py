# Problem 14 - Longest Collatz sequence
# https://projecteuler.net/problem=14
# 
# Need to find the longest Collatz sequence starting from a number
# less than 10^6. Seems like I can just write the obvious approach,
# and cache the intermediate values to avoid the exploding runs issue


n = 10**6

cachedSteps = {1: 0}

def stepsToOne(i):
    if i in cachedSteps: return cachedSteps[i]
    nextStep = i//2 if i%2 == 0 else 3*i+1
    cachedSteps[i] = stepsToOne(nextStep)+1
    #print("Called with i=",i,"determined there were",cachedSteps[i],"steps to one")
    return cachedSteps[i]

maxSteps = (1, 0)

for i in range(1,n):
    t = stepsToOne(i)
    if t > maxSteps[1]: 
        maxSteps = (i, t)
        print("New max step count at i =",i,"with a total of",t,"steps.")

print("Final max steps at i =",maxSteps[0],"with a total of",maxSteps[1],"steps.")

# Runs in about 4 second - not exactly 2 seconds, but I am very far from optimization here.
# Could speed it up with some optimization in the recursive function
# Could also speed it up by dynamic programming, I guess. Need to learn that.