# Problem 69 - Totient maximum
# https://projecteuler.net/problem=69
# 
# This is probably one of those horribly recursive things, so I'll just try out
# the naive solution first and see how fast it runs

memo = {(0,0): 1}

def A(m,n):
    if (m,n) in memo: return memo[(m,n)]

    print("New call. m =",m,"n =",n)

    if m == 0: memo[(m,n)] = n+1
    elif n == 0: memo[(m,n)] = A(m-1,1)
    else: memo[(m,n)] = A(m-1, A(m,n-1))

    return memo[(m,n)]

# Yes, it's wildly recursive and explodes the stack
# A bit of research turned out a much cleaner algorithm saved in the folder. 
# Implementation is below, let's see how it works!

def AO(m,n):
    next = [0]*(m+1)
    goal = [1]*(m+1)
    goal[m] = -1

    while next[m] != n+1:
        value = next[0]+1
        transferring = True
        i = 0
        while transferring:
            if next[i] == goal[i]: goal[i] = value
            else: transferring = False
            next[i] = next[i]+1
            i += 1
    return value

n = 4

for i in range(n+1):
    for j in range(n+1):
        print("AO(",i,",",j,") = ",AO(i,j),sep="")

# Definitely faster, and it doesn't explode the stack, but still nowhere
# near fast enough for our purposes. Need to grok the logic here better
# when this migraine lets up, and then I can maybe add some memoization
# to speed up a bit more