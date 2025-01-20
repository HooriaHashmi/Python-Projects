#The colors red, blue, and yellow are known as the primary colors because they cannot
#be made by mixing other colors. When you mix two primary colors, you get a secondary
# color, as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary colors to mix. If
# the user enters anything other than “red,” “blue,” or “yellow,” the program should display
# an error message. Otherwise, the program should display the name of the secondary color
# that results

def mix_colors(color1, color2):
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        return "Purple"
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        return "Orange"
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        return "Green"
    else:
        return "Error: Please enter valid primary colors (red, blue, yellow)."

# Get user input
color1 = input("Enter the first primary color (red, blue, yellow): ").lower()
color2 = input("Enter the second primary color (red, blue, yellow): ").lower()

# Check and display result
result = mix_colors(color1, color2)
print(result)




