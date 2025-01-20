# # Money Counting Game
# Create a change-counting game that gets the user to enter the number of coins required
# to make exactly one dollar. The program should prompt the user to enter the number of
# pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
# dollar, the program should congratulate the user for winning the game. Otherwise, the
# program should display a message indicating whether the amount entered was more than
# or less than one dollar.

def money_counting_game(pennies, nickels, dimes, quarters):
    total_value = pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25

    if total_value == 1.0:
        print("\nCongratulations! You've won the game. You made exactly one dollar!")
    elif total_value < 1.0:
        print(f"\nSorry, the total value entered ({total_value:.2f} dollars) is less than one dollar.")
    else:
        print(f"\nSorry, the total value entered ({total_value:.2f} dollars) is more than one dollar.")

# Get user input
try:
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))

    if pennies < 0 or nickels < 0 or dimes < 0 or quarters < 0:
        print("Error: Please enter valid non-negative integers for the coin counts.")
    else:
        money_counting_game(pennies, nickels, dimes, quarters)

except ValueError:
    print("Error: Please enter valid integers for the coin counts.")
