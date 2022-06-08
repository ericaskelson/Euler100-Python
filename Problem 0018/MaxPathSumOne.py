# Problem 18 - Maximum path sum I
# https://projecteuler.net/problem=18
#
# Need to read in a triangle and find the max path. Seems like a good time to
# try some DYNAMIC PROGRAMMING

# First need to read in the triangle
inputFile = "LittleTriangle.txt"

tri = {}

with open(inputFile) as f:
    i = 0
    for l in f.readlines():
        j = 0
        for c in l.split():
            tri[(i,j)] = int(c)
            j += 1
        i += 1

size = max(x[0] for x in tri)


# Add a function to check the triangle
def printTriangle(triangle, ht, clean):
    for i in range(ht+1):
        print(" "*2*(ht-i),end="")
        for j in range(min(ht+1,i+1)):
            if clean: print(("00"+str(triangle[(i,j)]))[-2:],"  ",sep="",end="")
            else: print(triangle[(i,j)],"  ",sep="",end="")
        print()

printTriangle(tri, size, True)

# Populate bottom row of max triangle
triMax = {}
for i in range(size+1): triMax[(size,i)] = tri[(size,i)]

# Fill out rest of triangle
for i in range(size-1,-1,-1):
    for j in range(i+1):
        triMax[(i,j)] = tri[(i,j)] + max(triMax[(i+1,j)],triMax[(i+1,j+1)])

printTriangle(triMax, size, False)

print("Maximum path is:",triMax[(0,0)])

# Worked just fine! Maybe I got to involved here, but I think this algorithm will work out of the box on Part Two.
# Let's see!