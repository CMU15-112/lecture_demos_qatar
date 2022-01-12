def celsiusToFahrenheit(t):   
    return  t * (9 / 5) + 32 
    
    

""" ask the user for yesterday's temp, then ask for today's temp, report the diff in F """
input_from_user = input("What was the temp yesterday (in celsius)?: ")

yesterday_temp_c = int(input_from_user)
print( "Yesterday temp in C: ", yesterday_temp_c)

input_from_user2 = input("What was the temp today (in celsius)?: ")
today_temp_c = int(input_from_user2)
print( "Today temp in C: ", today_temp_c)

## 1. converting yesterday_temp_c to F
yesterday_temp_f = celsiusToFahrenheit(yesterday_temp_c)

#yesterday_temp_f = yesterday_temp_c * (9 / 5) + 32
print("Yesterday Temp in F", yesterday_temp_f)

## 2. converting today_temp_c to F

today_temp_f = celsiusToFahrenheit(today_temp_c)

## 3. report the difference

print("Temp diff in F ", today_temp_f - yesterday_temp_f)


#y = 9
#z = x * y
#print(z)

#z = z / 5
#print(z)

#f = z + 32
#print(f)

