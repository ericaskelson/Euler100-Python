# Problem 13 - Large sum
# https://projecteuler.net/problem=13
# 
# Just need to sum a bunch of numbers and return the first 10 digits. 
# I suspect this will be easier in Python than most languages...

# First need to read in the list of numbers to sum
inputFile = "NumsToSum.txt"

with open(inputFile) as f:
    toSum = [int(x) for x in f.readlines()]

sum = sum(toSum)

firstTenDigits = str(sum)[0:10]

print("Sum is",sum)
print("First ten gitis are",firstTenDigits)

# Yeah, I feel like Python is cheating with the arbitrary length integers