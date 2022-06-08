# Problem 17 - Number letter counts
# https://projecteuler.net/problem=17
#
# Need to convert numbers in digits to numbers in words, then count digits
# Could skip the intermediate words and lookup lengths? That seems doable

a = [0 for x in range(100)]

a[1] = len("one")
a[2] = len("two")
a[3] = len("three")
a[4] = len("four")
a[5] = len("five")
a[6] = len("six")
a[7] = len("seven")
a[8] = len("eight")
a[9] = len("nine")
a[10] = len("ten")
a[11] = len("eleven")
a[12] = len("twelve")
a[13] = len("thirteen")
a[14] = len("fourteen")
a[15] = len("fifteen")
a[16] = len("sixteen")
a[17] = len("seventeen")
a[18] = len("eighteen")
a[19] = len("nineteen")
a[20] = len("twenty")
a[30] = len("thirty")
a[40] = len("forty")
a[50] = len("fifty")
a[60] = len("sixty")
a[70] = len("seventy")
a[80] = len("eighty")
a[90] = len("ninety")

for i in range(21,100):
    if a[i] == 0:
        a[i] = a[i%10]+a[i//10*10]

sum = len("onethousand")

for i in range(1000):
    sum += a[i%100]
    if i%100 != 0 and i > 99: sum += len("and")
    if i > 99: sum += a[i//100]+len("hundred")

print(sum)

# Bit of an annoying problem, but easy enough. 