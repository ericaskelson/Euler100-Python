# Problem 19 - Counting Sundays
# https://projecteuler.net/problem=19
#
# I'm sure there is a formula to solve this, but why not take the easy approach
# first? We'll just make a dictionary for each day from 1901 to 2000 with the info
# we need.

from dataclasses import dataclass
import copy

@dataclass
class Date:
    year: int
    month: int
    day: int
    # weekdays are from 0-6, 0 is Sunday
    weekday: int

currDate = Date(1901, 1, 1, 2)

#days = {0 : copy.deepcopy(currDate)}

def is_leap_year(year):
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)

#for i in range(1900,2001):
#    print("Year is",i,"and","it IS a leap year" if is_leap_year(i) else "it is NOT a leap year")

daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

firstSundays = 0

while currDate.year < 2001:
    nextDate = copy.deepcopy(currDate)
    nextDate.weekday = (currDate.weekday + 1)%7

    if daysInMonth[currDate.month] + (1 if is_leap_year(currDate.year) and currDate.month == 2 else 0) == currDate.day:
        nextDate.day = 1
        if currDate.month == 12:
            nextDate.year = currDate.year + 1
            nextDate.month = 1
        else:
            nextDate.month = currDate.month+1
    else:
        nextDate.day = currDate.day+1

    if nextDate.day == 1 and nextDate.weekday == 0: 
        firstSundays += 1
        print(nextDate.month,"/",nextDate.day,"/",nextDate.year," is a first Sunday. Total count of:",firstSundays)
    
    currDate = copy.deepcopy(nextDate)

print("Final count of first Sundays:",firstSundays)

# Nice, got it first try. Obviously could have been simpler, but it was good to figure
# out how dataclasses work.