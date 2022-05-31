# Calculate the largest palindrome number that is the product of two three digit numbers
# Start with the dumb approach, I guess!

import math

def isPalindrome(n):
    chars = list(str(n))
    length = len(chars)
    for i in range(0,length//2):
        if chars[i]!=chars[length-i-1]: return False
    return True

largestPalindrome=0

for i in range(999,99,-1):
    for j in range(999,99,-1):
        if isPalindrome(i*j) and i*j>largestPalindrome: 
            print("Product of",i,"and",j,"is a palindrome:",i*j)
            largestPalindrome = i*j

# Seems simple enough - curious if there's a better approach