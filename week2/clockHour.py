"""Write the function clockHour(currentHour, difference) that
takes as input the current hour, 
    now (as an integer) and interval is an integer representing
    the number of hours that have passed since the current hour. 
    The function should return the hour after
    the time passed (difference) has been added to the current hour.
    The function takes in two parameters: 
       - currentHour is an integer representing the current hour (1-12)
       - interval is an integer
    The result must be in the range 1 to 12 inclusive

Example:
clockHour(1, 3) == 4
clockHour(8, 11) == 7
clockHour(4, 13) == 5
clockHour(4, 24) == 4
"""

def clockHour(currentHour, difference):
    newHour = ((currentHour - 1) + difference) % 12 + 1

assert(clockHour(1, 3) == 4)
assert(clockHour(8, 11) == 7)
assert(clockHour(4, 13) == 5)
assert(clockHour(4, 24) == 4)