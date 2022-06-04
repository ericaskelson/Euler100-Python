# Problem 9 - Special Pythagorean triplet
# https://projecteuler.net/problem=9
# 
# Need to find a, b, and c, such that:
# a < b < c
# and a**2 + b**2 = c**2
# and a + b + c = 1000
# As usual, let's try the obvious way first

breakdance = False
n = 1000

for b in range(2,n):
    if breakdance: break
    for a in range(1,b+1):
        if breakdance: break
        c=n-a-b
        if (a**2 + b**2 == c**2): 
            print("Eureka! a =",a,"b =",b,"c =",c,"Then a+b+c = ",a+b+c,"and abc = ",a*b*c)
            breakdance = True

# Well, that was very slow. Still, looks like the right answer