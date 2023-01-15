"""
Create a function hourDifference(currentHour, difference) that calculates the hour after a certain amount of time has passed.
The function takes in two parameters:

currentHour is an integer representing the current hour (0-23)
difference is an integer representing the amount of hours that have passed since the current hour.
The function should return the hour after the time passed (difference) has been added to the current hour.
Example:

hourDifference(8,5) will return 13
hourDifference(14,3) will return 17 
hourDifference(22,-3) will return 19
Note: The function should consider that there are only 24 hours in a day, 
so the result must be in the range 0 to 23 inclusive"
"""


def hourDifference(currentHour, difference):
    return (currentHour + difference)%24
    
assert(hourDifference(8,5) == 13)
assert(hourDifference(14,3) == 17)
assert(hourDifference(22,-3) == 19)

assert(hourDifference(15, -12) == 3)
assert(hourDifference(3, 5) == 8)
assert(hourDifference(3, -5) == 22)
assert(hourDifference(0, -5) == 19)
assert(hourDifference(23, 1) == 0)
assert(hourDifference(12, 48) == 12)
assert(hourDifference(12, -48) == 12)
assert(hourDifference(12, -40) == 20)