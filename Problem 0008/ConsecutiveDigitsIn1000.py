# Problem 8 - Largest product in a series
# https://projecteuler.net/problem=8
# 
# Need to find the 13 consecutive digits with the largest product out of this enormous number

import math
import re

# First need to read in this enormous number
inputFile = "BigNumber.txt"

with open(inputFile) as f:
    rawFile = f.read()

bigNum = re.sub("\s","",rawFile)

#Next to get the biggest product of sequential digits
k = 13
n = len(bigNum)

biggestInput = "0000"
biggestOutput = 0

for i in range(n-k):
    t = 1
    for c in bigNum[i:i+k]:
        t = t*int(c)
    if t>biggestOutput:
        biggestOutput = t
        biggestInput = bigNum[i:i+k]
        print("New biggest product of",biggestInput,"is",biggestOutput)

print("Final biggest product is of digits",biggestInput,"and is equal to",biggestOutput)