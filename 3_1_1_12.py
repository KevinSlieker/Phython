year = int(input("Enter a year: "))

if year < 1582:
    year_type = "Not within the Gregorian calendar period"
elif year % 4 != 0:
    year_type = "common year"
elif year % 100 != 0:
    year_type = "leap year"
elif year % 400 != 0:
    year_type = "common year"
else:
    year_type = "leap year"
print(year_type)