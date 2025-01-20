# #15. Time Calculator
# Write a program that asks the user to enter a number of seconds and works as follows:
# • There are 60 seconds in a minute. If the number of seconds entered by the user is greater
# than or equal to 60, the program should convert the number of seconds to minutes and
# seconds.
# • There are 3,600 seconds in an hour. If the number of seconds entered by the user is
# greater than or equal to 3,600, the program should convert the number of seconds to
# hours, minutes, and seconds.
# • There are 86,400 seconds in a day. If the number of seconds entered by the user is
# greater than or equal to 86,400, the program should convert the number of seconds to
# days, hours, minutes, and seconds.

def convert_seconds(seconds):
    if seconds < 0:
        return "Error: Please enter a non-negative number of seconds."

    days = seconds // 86400
    remaining_seconds = seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    remaining_seconds %= 60

    if days > 0:
        return f"{days} days, {hours} hours, {minutes} minutes, {remaining_seconds} seconds"
    elif hours > 0:
        return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes, {remaining_seconds} seconds"
    else:
        return f"{remaining_seconds} seconds"

# Get user input
try:
    seconds = int(input("Enter the number of seconds: "))
    result = convert_seconds(seconds)
    print(f"\nConverted time: {result}")
except ValueError:
    print("Error: Please enter a valid integer for the number of seconds.")
