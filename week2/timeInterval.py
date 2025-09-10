"""
Write the function timeInterval(t1, t2) which, given two non-negative integers t1, t2, that encode two 24-hour times in the format hhmm, returns the time interval, in minutes, between those two times. If t2 < t1, you should assume that t2 refers to a next day time. You can assume that 0 < hh < 24 is the hour, and 0 < mm < 60 are the minutes. If hh > 0, then mm is always a two-digit number. If hh == 0, then mm can be either a one or a two-digit number, depending on its value.
1503 is 15 hours, 3 minutes, or 3:03pm.
849 is 8 hours, 49 minutes, or 8:49am.
0 is 0 hours, 0 minutes, or 12:00am midnight.
59 is 0 hours, 59 minutes, or 12:59am.
101 is 1 hour, 1 minute, or 1:01am.
For example...
timeInterval(1400, 1545) returns the time interval between 14 o'clock and 15:45 (same day) which is 105 minutes.
timeInterval(2359, 31) returns the time interval between 23:59 and 00:31 (next day), which is 32 minutes.
timeInterval(31, 2359) returns the time interval between 00:31 and 23:59 (same day), which is 1408 minutes.
timeInterval(1200, 0) returns the time interval between noon and midnight (next day), which is 720 minutes.
Hint: There are 1440 minutes in a day.
"""

def timeInterval(t1, t2):
    pass