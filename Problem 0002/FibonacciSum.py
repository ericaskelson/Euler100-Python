# This program is intended to calculate the sum of all even valued terms
# in the Fibonacci sequence which do not exceed 4 million.

def fibRecurse(n):
    if n==0: return 1
    elif n==1: return 2
    else: return fibRecurse(n-1)+fibRecurse(n-2)

for i in range(10):
    print("For n =",i,", fibRecurse(n) =",fibRecurse(i))

# Note, this is way too slow, since it's basically setting of a fork bomb. 
# We need to do it iteratively instead.

fibEvensSum=2
limit=4000000
oneBack=2
twoBack=1
fibValue=0

while fibValue<=limit:
    fibValue=oneBack+twoBack
    twoBack=oneBack
    oneBack=fibValue
    if fibValue%2==0: fibEvensSum+=fibValue
    print("Curr val is:",fibValue," Current sum of even values is:",fibEvensSum)