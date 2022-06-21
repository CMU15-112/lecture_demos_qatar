# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}

# I can print it
print(gulfCapitals)

while True:
    choice = int(input("Menu: 1. Ask capital, 2 Add new country, 3.Exit "))
    if choice == 3:
        break
    elif choice == 1:
        country = input("Enter a country:")
        if country in gulfCapitals:
            print(f"Capital of {country}: {gulfCapitals[country]}")
        else:
            print(f"Country {country} not found")
    elif choice == 2:
        country = input("Enter a country:")
        city = input("Enter a city:")
        gulfCapitals[country] = city
    else:
        print("Invalid choice")
        
        