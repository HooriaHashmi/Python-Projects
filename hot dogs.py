# #Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
# program that calculates the number of packages of hot dogs and the number of packages of
# hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
# should ask the user for the number of people attending the cookout and the number of hot
# dogs each person will be given. The program should display the following details:
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over

def calculate_packages(people, hotdogs_per_person):
    hotdogs_per_package = 10
    buns_per_package = 8

    total_hotdogs_needed = people * hotdogs_per_person
    total_hotdog_packages = (total_hotdogs_needed + hotdogs_per_package - 1) // hotdogs_per_package

    total_buns_needed = people * hotdogs_per_person
    total_bun_packages = (total_buns_needed + buns_per_package - 1) // buns_per_package

    hotdogs_leftover = (total_hotdog_packages * hotdogs_per_package) - total_hotdogs_needed
    buns_leftover = (total_bun_packages * buns_per_package) - total_buns_needed

    return total_hotdog_packages, total_bun_packages, hotdogs_leftover, buns_leftover

# Get user input
try:
    people = int(input("Enter the number of people attending the cookout: "))
    hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

    if people <= 0 or hotdogs_per_person <= 0:
        print("Error: Please enter valid positive integers.")
    else:
        hotdog_packages, bun_packages, hotdogs_leftover, buns_leftover = calculate_packages(people, hotdogs_per_person)

        print(f"\nMinimum number of hot dog packages required: {hotdog_packages}")
        print(f"Minimum number of hot dog bun packages required: {bun_packages}")
        print(f"Number of hot dogs left over: {hotdogs_leftover}")
        print(f"Number of hot dog buns left over: {buns_leftover}")

except ValueError:
    print("Error: Please enter valid integers.")




