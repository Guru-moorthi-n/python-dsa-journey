# Day 07 - Check Leap Year or Not

# Method 1: Using if-else statements
year = 2000

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# Method 2: Using ternary operator
def is_leap_year(year):
    return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False

year = 2000
print(f"{year} is a leap year:", is_leap_year(year))


# Method 3: Using calendar module
import calendar

year = 2000
print(f"{year} is a leap year:", calendar.isleap(year))
