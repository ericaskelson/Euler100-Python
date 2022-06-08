# Problem 16 - Power digit sum
# https://projecteuler.net/problem=16
# 
# I need to calculate the sum of the digits of 2**1000. Need to think through binary
# representations here. Or maybe we see just how that vaunted arbitrary precision
# integer math scales?

n = 1000
bigNum = 2**n
bigStr = str(bigNum)

digitSum = 0

for c in bigStr:
    digitSum += int(c)

print("Sum of digits of 2**",n,"is",digitSum)

# HA - it just works. That's honestly just silly. Thank you Python.