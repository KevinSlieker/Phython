def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_months = days[month-1]
    if month == 2 and is_year_leap(year) == True:
        days_months = 29
    #print(days_months)
    return days_months

def day_of_year(year, month, day):
    days = 0
    for i in range(1,month):
        days += days_in_month(year, i)
    days += day
    if days_in_month(year, month) < day:
        return None
    return days

print(day_of_year(1999, 2, 31))
#print(is_year_leap(1999))
