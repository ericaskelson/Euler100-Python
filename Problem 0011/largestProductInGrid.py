# Need to read in the grid and then multiply. No speed issue, seems it's just a matter of pulling the values

import math

# First need to read in the array
inputFile = "grid.txt"

with open(inputFile) as f:
    grid = [[int(x) for x in row.split()] for row in f.read().splitlines()]
 
maxHor = 0
maxVer = 0
maxDiagR = 0
maxDiagL = 0
max = 0

n = 4

# Find largest horizontal product of n
for i in range(len(grid[:])):
    for j in range(len(grid[i])-n+1):
        subset = grid[i][j:j+n]
        t = math.prod(subset)
        if t > maxHor: 
            # print("New biggest horizontal product of four comes from row",i,"and column",j,"Product is",t,"Components are",subset)
            maxHor = t
        if t > max: max = t

# Find largest vertical product of n
for j in range(len(grid[0][:])):
    for i in range(len(grid[:])-n+1):
        subset = [row[j] for row in grid[i:i+n]]
        t = math.prod(subset)
        if t > maxVer: 
            # print("New biggest vertical product of four comes from row",i,"and column",j,"Product is",t,"Components are",subset)
            maxVer = t
        if t > max: max = t

# Stop being fancy bro - down-to-the-right 
for i in range(len(grid[:])-n+1):
    for j in range(len(grid[i])-n+1):
        dr = math.prod(grid[i+k][j+k] for k in range(4))
        dl = math.prod(grid[i+k][len(grid[i])-j-k-1] for k in range(4))
        if dr > maxDiagR: maxDiagR = dr
        if dr > max: max = dr
        if dl > maxDiagL: maxDiagL = dl
        if dl > max: max = dl

print("Biggest horizontal product is",maxHor)
print("Biggest vertical product is",maxVer)
print("Biggest diagonal right product is",maxDiagR)
print("Biggest diagonal left product is",maxDiagL)
print("Biggest product is",max)

# Well that was just excruciating. I am CERTAIN there is a more elegant way than this.