# Import the math module to calculate the average
import math 

# Create empty list for numbers
list_of_numbers = []

# Request input from user and store in variable "user_number"
user_number = int(input("Enter a non-zero number here (Enter -1 to exit): "))

# Begin a while loop for the condition that negative -1 and zero isn't entered
while user_number != -1 and user_number != 0:
    # Add the number to the list if it doesn't equal zero or negative 1
    list_of_numbers.append(user_number)

    # Request the user input within the loop
    user_number = int(input("Enter a non-zero number here (Enter -1 to exit): "))
    while user_number == 0:
        # Print message to console that 0 can't be entered and request another
        # Used course material youtube video "Beginner Control Structures" for reference to repeated input
        # Found at https://www.youtube.com/watch?v=nTbiS2-KqBY
        user_number = int(input("The number can't be zero. Enter a non-zero number here (Enter -1 to exit): "))

    # Used course material "10-038 Iteration" for reference to continue statement
    if user_number == -1: 
        continue


# Define "average" as the sum of numbers, divided by the amount of numbers entered
# Used "10-017_Data Structures – The List.pdf" to reference list operations
list_average = sum(list_of_numbers)/len(list_of_numbers)

# Prints the average of the list, with a message to the console
print(f"The average of your numbers is: {list_average}")