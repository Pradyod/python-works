years =[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011]

leap_yr=[i for i in years if i%4==0 and i%100!=0 or i%400==0]

print(leap_yr)