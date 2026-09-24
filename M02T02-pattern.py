# Used course material pdf "10-038 Iteration" to reference for loop and if statament combinations

# Define the asterisk variable
asterisk = "*"

# Create a range of integers for the arrow height
arrow_height = range(1,9)

# Use for loop to iterate through arrow height integers
for num in arrow_height: 
    # Create a condition giving the first five rows, a quantity of asterisks equal to the value of the row
    if num < 6:
        # Define the row width variable, equal to the quantity of asterisks needed
        width = num * asterisk
        # Print each row as the program interates through the for loop
        print(width)
    # The rows tip, needs to shorten after row 5
    elif num >= 6: 
        # The number of asterisks ofter the arrows tip are equal to "10" minus the row number
        # The calculation defines the width 
        width = (10 - num) * asterisk
        # Print each row as the program iterates
        print(width)





    