def hourDifference(currentHour, difference):
    return (currentHour + difference)%24
    
    
print(hourDifference(15, -12) == 3)
print(hourDifference(3, 5) == 8)
print(hourDifference(3, -5) == 22)
print(hourDifference(0, -5) == 19)
print(hourDifference(23, 1) == 0)
print(hourDifference(12, 48) == 12)
print(hourDifference(12, -48) == 12)
print(hourDifference(12, -40) == 20)