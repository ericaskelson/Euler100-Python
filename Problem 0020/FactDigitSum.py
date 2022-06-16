# Problem 20 - Factorial digit sum
# https://projecteuler.net/problem=69
#
# Just how powerful are the arbitrary integer calculations in Python?

import math

n = 100
fact = math.factorial(100)
digitSum = 0

while fact != 0:
    digitSum += fact%10
    fact = fact//10

print("Sum of digits in ",n,"! is: ",digitSum,sep="")
