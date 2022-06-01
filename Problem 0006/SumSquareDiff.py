# Calculates the difference between the sum of squares and the square of sums for integers between 1 and 100
# Seems really easy? I must be missing something here.

bound = 100

def sum_of_squares(n):
    return sum([x**2 for x in range(1,n+1)])

def square_of_sum(n):
    return (n*(n+1)//2)**2

sumSq = sum_of_squares(bound)
sqSum = square_of_sum(bound)

print("For integers 1 to ",bound)
print("Sum of squares is",sumSq)
print("Square of sum is",sqSum)
print("Difference is",sqSum-sumSq)

# Ahh, I see, there is a formula for the sum of squares. I should have tried to derive that.