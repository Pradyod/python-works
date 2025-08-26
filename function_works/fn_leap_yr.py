def leap_yr(year):
    if year%100!=0 and year%4==0 or year%400==0:
        return f"{year} is leap year"
    else:
        return f"{year} not a leap year" 

print(leap_yr(1992))