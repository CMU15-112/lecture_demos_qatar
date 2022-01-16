def celsiusToFahrenheit(t):
    # Functions can have any number of statements inside
#    print("converting temp")
#    print("another print")
#    b=4
    return  t * (9 / 5) + 32

# ask the user for yesterday's temp, then ask for today's temp, report the diff in F
inputFromUser = input("What was the temp yesterday (in celsius)?: ")

yesterdayTempC = int(inputFromUser)
print( "Yesterday temp in C: ", yesterdayTempC)

inputFromUser2 = input("What was the temp today (in celsius)?: ")
todayTempC = int(inputFromUser2)
print( "Today temp in C: ", todayTempC)

## 1. converting yesterdayTempC to F
yesterdayTempF = celsiusToFahrenheit(yesterdayTempC)

print("Yesterday Temp in F", yesterdayTempF)

## 2. converting todayTempC to F
todayTempF = celsiusToFahrenheit(todayTempC)

tempDiff = todayTempF - yesterdayTempF

if tempDiff > 0:
    print("Today is", tempDiff, "hotter than yesterday")
elif tempDiff < 0:
    print("Today is", tempDiff, "colder than yesterday")
else:
    print("No temp diff")
