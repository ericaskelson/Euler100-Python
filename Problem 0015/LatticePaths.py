# This program finds all the ways you can get from the top left of an nxm grid down
# to the bottom right, assuming you can only move to the right and down

import math

def paths_to_zero_explained(a, b):
    t = 0
    if a == 0 or b == 0: t = 1
    elif a == b: t = 2*paths_to_zero_explained(a-1, b)
    else: t = paths_to_zero_explained(a-1, b) + paths_to_zero_explained(a, b-1)
    print("At point (",a,",",b,"), there ","is " if t == 1 else "are ",t," path","s" if t != 1 else ""," to (0,0)",sep="")
    return t

def paths_to_zero(a, b):
    if a == 0 or b == 0: return 1
    elif a == b: return 2*paths_to_zero(a-1, b)
    else: return paths_to_zero(a-1, b) + paths_to_zero(a, b-1)


# Too slow to use this recursive formula past 18x18, but it seems obvious that for an nxn grid
# there are (2n choose n) paths. Why? Still trying to understand this better. 

# Aha, I should have saved the results of the runs to avoid duplicates.

results = {(0,0): 1}

def paths_to_zero_fast(a, b):
    key = (a, b) if a > b else (b, a)
    if key[0] == 0 or key[1] == 0: return 1
    elif key in results: return results[key]
    # Don't even need this optimization once we add memoization:
    # elif key[0] == key[1]: 
    #     results[key] = 2*paths_to_zero_fast(key[0]-1, key[1])
    #     return results[key]
    else: 
        results[key] = paths_to_zero_fast(key[0]-1, key[1]) + paths_to_zero_fast(key[0], key[1]-1)
        return results[key]

size = 20

# Works out to absurd sizes:
# size = 100

for i in range(size+1):
    n = i
    m = n
    print("On a ",n,"x",m," grid, the path count from origin to end per algorithm is ",paths_to_zero_fast(n,m),sep="")
    print("On a ",n,"x",m," grid, the path count from origin to end per formula   is ",math.comb(2*n,n),sep="")

#print(results)
print("Elements in memo dict:",len(results))

# Yeah, that's about the right speed...