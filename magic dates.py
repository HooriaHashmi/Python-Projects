# #6. Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the
# month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit year. The program should then determine whether the month times the day equals the
# year. If so, it should display a message saying the date is magic. Otherwise, it should display
# a message saying the date is not magic.

def is_magic_date(month, day, year):
    return month * day == year

# Get user input
try:
    month = int(input("Enter the month (numeric form): "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the two-digit year: "))

    if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 99:
        if is_magic_date(month, day, year):
            print("\nThe date is magic!")
        else:
            print("\nThe date is not magic.")
    else:
        print("Error: Please enter valid values for month, day, and two-digit year.")

except ValueError:
    print("Error: Please enter valid integers for month, day, and two-digit year.")
        
