# Calculates the sum of all multiples of 3 or 5 below 1000
# First we do the obvious way:

sumEasy = 0

for i in range(1,1000):
    if i%3==0: sumEasy+=i
    elif i%5==0: sumEasy+=i

print("Easy sum comes to:",sumEasy)

# Next a quicker way, just iterate over the multiples:

n=0
sumHard = 0

for i in range(3,1000,3):
    sumHard+=i
    n+=1

for i in range(5,1000,5):
    if i%3!=0: sumHard+=i
    n+=1

print("Hard sum comes to:",sumHard)
print("Total iterations:",n)

# Finally, can we directly prove what the value should be?
# There are n/1000 numbers <= 1000 divisible by n. The sum of all integers from
# 1 to m is m*(m+1)/2, so the sum of the multiples from 3 to 1000 by 3s should be
# 333*334/2*3. That is,

def sum_multiples(multiple,max):
    up=max//multiple
    return multiple*(up)*(up + 1)//2

threes=sum_multiples(3,1000)
fives=sum_multiples(5,1000)
fifteens=sum_multiples(15,1000)
sumFormula=threes+fives-fifteens

print("Sum of threes: ",threes)
print("Sum of fives: ",fives)
print("Sum of fifteens: ",fifteens)

print("Total via formula: ",sumFormula)